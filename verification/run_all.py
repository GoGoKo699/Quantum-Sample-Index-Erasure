#!/usr/bin/env python3
"""Finite diagnostics for copy-only index erasure; Python standard library only.

Exact arithmetic is used unless a field is explicitly labelled modular.
The tests do not build a large injection Gram or prove an asymptotic theorem.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial, prod
from pathlib import Path
import argparse
import json


def partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    for a in range(min(n, n if cap is None else cap), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def hooks(shape):
    return [shape[i]-j + sum(t > j for t in shape[i+1:])
            for i in range(len(shape)) for j in range(shape[i])]


def dim(shape):
    return factorial(sum(shape)) // prod(hooks(shape))


def content(shape):
    return sum(j-i for i, length in enumerate(shape) for j in range(length))


def horizontal(big, small):
    if len(small) > len(big):
        return False
    b = big + (0,)
    s = small + (0,) * (len(big)-len(small))
    return all(b[i] >= s[i] >= b[i+1] for i in range(len(big)))


def falling(n, r):
    return prod(range(n-r+1, n+1))


def stirling(k, r):
    row = [1] + [0]*r
    for _ in range(k):
        row = [0] + [j*row[j] + row[j-1] for j in range(1, r+1)]
    return row[r]


def projection_checks():
    cases = []
    for n, m in [(2, 3), (3, 5), (4, 6)]:
        count = 0
        for f in permutations(range(m), n):
            # Independently inspect the union of the identity and f matchings.
            # Parallel equal-colour-position edges still count twice in degree.
            adjacency = defaultdict(list)
            for x,y in enumerate(f):
                for target in (x,y):
                    adjacency[('d',x)].append(('r',target))
                    adjacency[('r',target)].append(('d',x))
            unseen = set(adjacency)
            nontrivial_paths = 0
            while unseen:
                stack=[unseen.pop()]; component=[]
                while stack:
                    v=stack.pop(); component.append(v)
                    for neighbor in adjacency[v]:
                        if neighbor in unseen:
                            unseen.remove(neighbor); stack.append(neighbor)
                if any(len(adjacency[v]) == 1 for v in component):
                    assert sum(len(adjacency[v]) == 1 for v in component) == 2
                    nontrivial_paths += 1
            overlap = len(set(f).intersection(range(n)))
            assert nontrivial_paths == n-overlap
            # Scale both source and projector by their known normalizations.
            # Projected range coefficients are 1/N on the image, zero elsewhere.
            projected = [F(int(y in f), n) for y in range(m)]
            success = sum(a*a for a in projected)
            assert success == F(1, n)
            # Inner product with the unnormalized target is exactly one.
            # Squared normalized fidelity is (sum coefficients)^2/(N*success).
            fidelity = sum(projected)**2 / (n*success)
            assert fidelity == 1
            # A deliberately nonuniform known index vector has the SAME success
            # probability but generally fails to give the erased target.
            weights = tuple(range(1, n+1))
            norm2 = sum(w*w for w in weights)
            weighted_success = F(norm2, n*norm2)
            weighted_fidelity = F(sum(weights)**2, n*norm2)
            assert weighted_success == F(1, n)
            assert weighted_fidelity < 1
            # A fixed fallback |0> yields half-trace distance squared at most
            # failure^2; target overlap is 1/N iff zero is in the image.
            k = n+1
            failure = F(n-1, n)**k
            distance_squared = failure**2 * (1-F(int(0 in f), n))
            assert distance_squared <= failure**2
            count += 1
        cases.append(dict(N=n, M=m, injections_enumerated=count,
                          projection_success=str(F(1, n)),
                          deliberately_wrong_one_over_M=str(F(1, m)),
                          nonuniform_index_fidelity=str(weighted_fidelity),
                          conditioned_target_fidelity="1",
                          matching_union_path_identity_checked=True))
    # Directly average small target density matrices, then check their two
    # eigenspaces rather than merely evaluating the stated eigenvalue formula.
    averaged = []
    for n, m in [(2, 3), (3, 5)]:
        fs = list(permutations(range(m), n))
        rho = [[sum(F(int(i in f and j in f), n) for f in fs)/len(fs)
                for j in range(m)] for i in range(m)]
        assert all(sum(row) == F(n, m) for row in rho)
        for j in range(1, m):
            vector = [F(int(i == 0)-int(i == j)) for i in range(m)]
            image = [sum(a*b for a,b in zip(row,vector)) for row in rho]
            assert image == [F(m-n, m*(m-1))*v for v in vector]
        averaged.append(dict(N=n, M=m, uniform_eigenvalue=str(F(n,m)),
                             orthogonal_eigenvalue=str(F(m-n,m*(m-1)))))
    return dict(projection_cases=cases, zero_copy_average_targets=averaged)


def occupancy_checks():
    cases = 0
    for n in range(2, 13):
        for k in range(1, n//2+1):
            weights = [F(stirling(k,r)*falling(n,r), n**k) for r in range(1,k+1)]
            assert all(w >= 0 for w in weights) and sum(weights) == 1
            for a in range(n+1):
                value = sum(w*F(falling(a,r), falling(n,r))
                            if a >= r else 0 for r,w in enumerate(weights,1))
                assert value == F(a,n)**k
                cases += 1
    return dict(exact_scalar_Gram_identity_cases=cases,
                N_range=[2,12], k_range="1..floor(N/2)", A_range="0..N")


def sparse_mul(a, b):
    out = []
    for row in a:
        result = defaultdict(int)
        for k,x in row.items():
            for j,y in b[k].items():
                result[j] += x*y
        out.append({j:x for j,x in result.items() if x})
    return out


def trace(a):
    return sum(row.get(i,0) for i,row in enumerate(a))


def charpoly_from_moments(moments, size):
    # Newton/Faddeev-LeVerrier identities, coefficients in descending order.
    coefficients = [1]
    for j in range(1,size+1):
        numerator = -sum(coefficients[j-i]*moments[i-1] for i in range(1,j+1))
        assert numerator % j == 0
        coefficients.append(numerator//j)
    return coefficients


def polynomial_from_spectrum(spectrum):
    p = [1]
    for eigenvalue,multiplicity in sorted(spectrum.items()):
        for _ in range(multiplicity):
            q = [0]*(len(p)+1)
            for i,v in enumerate(p):
                q[i] += v
                q[i+1] -= eigenvalue*v
            p = q
    return p


def rank_mod(matrix, prime):
    a = [[row.get(j,0) % prime for j in range(len(matrix))] for row in matrix]
    rank = 0
    for col in range(len(matrix)):
        pivot = next((i for i in range(rank,len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank],a[pivot] = a[pivot],a[rank]
        inv = pow(a[rank][col],-1,prime)
        a[rank] = [(x*inv)%prime for x in a[rank]]
        for i in range(rank+1,len(a)):
            factor = a[i][col]
            if factor:
                a[i] = [(x-factor*y)%prime for x,y in zip(a[i],a[rank])]
        rank += 1
    return rank


def tuple_case(n,r):
    tuples = list(permutations(range(n),r))
    lookup = {x:i for i,x in enumerate(tuples)}
    size = len(tuples)
    Q = [defaultdict(int) for _ in tuples]
    CN = [defaultdict(int) for _ in tuples]
    CR = [defaultdict(int) for _ in tuples]
    # Build sum D_j^*D_j by actual deletion fibers.
    for j in range(r):
        fibers = defaultdict(list)
        for i,x in enumerate(tuples):
            fibers[x[:j]+x[j+1:]].append(i)
        for indices in fibers.values():
            for i in indices:
                for k in indices:
                    Q[i][k] += 1
    # Independently build the central group actions.
    for i,x in enumerate(tuples):
        for a in range(n):
            for b in range(a+1,n):
                y = tuple(b if z == a else a if z == b else z for z in x)
                CN[i][lookup[y]] += 1
        for a in range(r):
            for b in range(a+1,r):
                y = list(x); y[a],y[b] = y[b],y[a]
                CR[i][lookup[tuple(y)]] += 1
    shift = comb(n-r,2)-r
    for i in range(size):
        for j in range(size):
            assert Q[i].get(j,0) == CN[i].get(j,0)-CR[i].get(j,0)-shift*(i==j)
    spectrum = Counter()
    zero_blocks = []
    for lam in partitions(n):
        for mu in partitions(r):
            if horizontal(lam,mu):
                q = content(lam)-content(mu)-shift
                multiplicity = dim(lam)*dim(mu)
                assert q >= 0
                assert (q == 0) == (lam[0] == n-r)
                s = r-(n-lam[0])
                if s >= 1:
                    assert q >= s*(n-2*r+s+1)
                spectrum[q] += multiplicity
                if not q:
                    zero_blocks.append((lam,mu))
    assert sum(spectrum.values()) == size
    direct_top = sum(dim((n-r,)+nu)*dim(nu) for nu in partitions(r))
    assert direct_top == spectrum[0]
    power = [{i:1} for i in range(size)]
    number_moments = size if size <= 30 else 3
    moments = []
    for p in range(1,number_moments+1):
        power = sparse_mul(power,Q)
        value = trace(power)
        assert value == sum(mult*eigen**p for eigen,mult in spectrum.items())
        moments.append(value)
    if size <= 30:
        assert charpoly_from_moments(moments,size) == polynomial_from_spectrum(spectrum)
    modular = {}
    for prime in (1000003,1000033):
        rank = rank_mod(Q,prime)
        assert size-rank == spectrum[0]
        modular[str(prime)] = size-rank
    assert F(spectrum[0],size) >= 1-F(r,n-r+1)
    return dict(N=n,r=r,tuple_dimension=size,
                exact_deletion_central_identity=True,
                Pieri_dimension_sum=size,
                predicted_integer_spectrum={str(k):v for k,v in sorted(spectrum.items())},
                exact_characteristic_polynomial_checked=(size<=30),
                exact_trace_moments_checked=number_moments,
                modular_kernel_dimensions=modular,
                top_kernel_dimension=spectrum[0],
                top_kernel_fraction=str(F(spectrum[0],size)),
                rank_bound_fraction=str(1-F(r,n-r+1)))


def tuple_checks():
    return [tuple_case(n,r) for n,r in [(4,1),(4,2),(5,2),(6,2),(6,3),(7,3),(8,3)]]


def hypergeom_tail(n,m,t):
    denominator = comb(m,n)
    numerator = sum(comb(n,j)*comb(m-n,n-j)
                    for j in range(max(t,2*n-m,0),n+1))
    return F(numerator,denominator)


def hypergeom_checks():
    toy = 0
    scoped = []
    for n in range(1,7):
        for m in range(n,25):
            for t in range(1,n+1):
                actual = hypergeom_tail(n,m,t)
                moment = F(comb(n,t)*falling(n,t),falling(m,t))
                loose = F(n*n,m-n)**t if m > n else None
                assert actual <= moment
                if loose is not None:
                    assert moment <= loose
                toy += 1
    for n in (64,128,256):
        m = n**4
        for t in sorted({2,5,3*(n//32)+2}):
            actual = hypergeom_tail(n,m,t)
            moment = F(comb(n,t)*falling(n,t),falling(m,t))
            loose = F(n*n,m-n)**t
            assert actual <= moment <= loose
            scoped.append(dict(N=n,M=m,t=t,actual_tail_float=float(actual),
                               factorial_moment_bound_float=float(moment),
                               loose_bound_float=float(loose),
                               comparisons="exact rational"))
    cutoff = 0
    for n in (64,96,128,256,1024):
        for m in (n**4,n**4+1,2*n**4):
            for ell in range(n//32+1):
                t = 3*ell+2
                assert t <= n
                dimension_times_loose = (m*n)**ell * F(2*n*n,m)**t
                bound = F(4,n**4)
                assert dimension_times_loose <= bound
                cutoff += 1
    return dict(toy_exact_tail_comparisons=toy,scoped_exact_tail_cases=scoped,
                scoped_dimension_times_tail_comparisons=cutoff)


def addable(shape):
    for i in range(len(shape)+1):
        if i == len(shape):
            yield shape+(1,)
        elif i == 0 or shape[i] < shape[i-1]:
            result = list(shape); result[i] += 1
            yield tuple(result)


def stable_dim(m,tail):
    q = sum(tail)
    correction = prod(F(m-q-c+1+sum(row>=c for row in tail),m-q-c+1)
                      for c in range(1,(tail[0] if tail else 0)+1))
    result = F(comb(m,q)*dim(tail),1)/correction
    assert result.denominator == 1
    return result.numerator


def direct_hook_move_ratio(m,tail,larger):
    # Cancel common hook factors directly; do not divide two dimension formulas.
    q = sum(tail); first = m-q
    changed_row = next(i for i in range(len(larger))
                       if i >= len(tail) or larger[i] != tail[i])
    changed_column = larger[changed_row]
    width = larger[0]
    result = F(first-width)
    for c in range(1,width+1):
        old_col = sum(row>=c for row in tail)
        new_col = sum(row>=c for row in larger)
        result *= F(first-c+1+old_col, first-c+new_col)
    for i,row in enumerate(tail):
        for j in range(row):
            old_hook = row-j+sum(t>j for t in tail[i+1:])
            new_hook = larger[i]-j+sum(t>j for t in larger[i+1:])
            result *= F(old_hook,new_hook)
    assert changed_column >= 1
    return result


def representative_tails(q):
    if not q:
        return [()]
    shapes = {(q,), (1,)*q}
    if q >= 2:
        shapes.add(((q+1)//2,q//2))
    # A staircase-like shape with exactly q boxes.
    remaining=q; cap=max(1,int((2*q)**.5)); tail=[]
    while remaining:
        a=min(cap,remaining); tail.append(a); remaining-=a; cap=a
    shapes.add(tuple(tail))
    return sorted(shapes)


def hook_checks():
    toy = 0
    for m in range(4,23):
        for q in range(min(m//2,6)+1):
            for tail in partitions(q):
                if tail and m-q < tail[0]:
                    continue
                assert stable_dim(m,tail) == dim((m-q,)+tail)
                for larger in addable(tail):
                    if m-q-1 < larger[0]:
                        continue
                    ratio = direct_hook_move_ratio(m,tail,larger)
                    assert ratio == F(dim((m-q-1,)+larger),dim((m-q,)+tail))
                    toy += 1
    scoped = []
    count=0; smallest=None
    for n in (64,128,256):
        for m in (n**4,n**4+1,2*n**4):
            for q in sorted({0,1,2,4,8,16,n//2-1,n-1}):
                for tail in representative_tails(q):
                    for larger in addable(tail):
                        ratio = direct_hook_move_ratio(m,tail,larger)
                        factorized_ratio = F(stable_dim(m,larger),stable_dim(m,tail))
                        assert ratio == factorized_ratio
                        conservative = F(m-q,q+1)*(1-F(q+1,m-2*q-1))
                        assert ratio >= conservative >= F(m,2*n)
                        relative = ratio/F(m,2*n)
                        smallest = relative if smallest is None else min(smallest,relative)
                        count += 1
            scoped.append(dict(N=n,M=m,max_tail_size_tested=n-1))
    return dict(small_direct_full_hook_comparisons=toy,
                scoped_direct_cancelled_hook_comparisons=count,
                scoped_parameters=scoped,
                minimum_ratio_to_claimed_lower_bound=str(smallest),
                warning="Representative tails only; not all partitions up to size255.")


def constant_checks():
    cases=[]
    for n in (64,65,96,128,256,1024,4096):
        k=n//32; m=n**4
        source=1-F(k,n-k+1)
        output=F(n,m)+F(3*k+2,n)+F(4,n**4)
        gap=source-output
        assert source > F(30,31)
        assert output < F(1251,10000)
        assert gap > F(8426,10000)
        assert gap > 0 and gap**2 > F(5,9)
        cases.append(dict(N=n,M=m,k=k,source_lower=str(source),
                          ideal_output_upper=str(output),gap=str(gap),
                          gap_float=float(gap),
                          average_fidelity_allowance_squared="5/9",
                          positive_gap_squared_exceeds_allowance=True))
    return cases


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true',help='Check saved results without rewriting them')
    args=parser.parse_args()
    results=dict(schema_version=1,status="passed",arithmetic="Python stdlib integers and Fraction; modular ranks explicitly labelled",
                 projection=projection_checks(),occupancy=occupancy_checks(),
                 tuple_modules=tuple_checks(),hypergeometric=hypergeom_checks(),
                 hook_dimensions=hook_checks(),constant_gap=constant_checks(),
                 limitations=["No large-range injection Gram was constructed.",
                              "Finite diagnostics do not prove the asymptotic copy lower bound or priority.",
                              "Full exact characteristic polynomials only for tuple dimensions<=30; larger cases use exact identities/trace moments and two modular ranks.",
                              "Scoped hook tests use representative tails, not an exhaustive partition sweep.",
                              "Fidelity means target overlap <s|rho|s>; trace distance means half the trace norm."])
    destination=Path(__file__).with_name('results.json')
    encoded=json.dumps(results,indent=2,sort_keys=True)+'\n'
    if args.check:
        assert destination.read_text()==encoded, 'Saved results differ; inspect before updating.'
    else:
        destination.write_text(encoded)
    print(json.dumps(dict(status='passed',results=str(destination),
                          tuple_cases=len(results['tuple_modules']),
                          projection_injections=sum(c['injections_enumerated'] for c in results['projection']['projection_cases']),
                          occupancy_checks=results['occupancy']['exact_scalar_Gram_identity_cases'],
                          hypergeom_checks=results['hypergeometric']['toy_exact_tail_comparisons'],
                          scoped_hook_checks=results['hook_dimensions']['scoped_direct_cancelled_hook_comparisons']),indent=2))


if __name__=='__main__':
    main()
