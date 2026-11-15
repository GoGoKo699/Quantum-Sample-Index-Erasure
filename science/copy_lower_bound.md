# Linear copy complexity for sample index erasure

The task has a simple implementation with copies: project the label register of a fresh sample onto the uniform state, and repeat when it fails. The success probability is $`1/N`$. The point of the lower bound is that arbitrary joint processing of many samples cannot improve the fixed-error order.

This page combines the [source harmonic lemma](input_harmonics.md) and the [output harmonic bound](output_harmonics.md). Those pages give the representation-theoretic arguments and exact primary-source dependencies. The [model](model.md) fixes the supplied access and output conventions; the [construction](construction.md) and [resources](resources.md) give the matching implementation and its costs.

## The theorem

Let $`N\ge64`$ and $`M\ge N^4`$. An unknown injection $`f:[N]\to[M]`$ supplies independent copies of

```math
|a_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|x\rangle|f(x)\rangle.
```

The desired output is

```math
|s_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|f(x)\rangle.
```

Let $`\mathcal A`$ be any $`f`$-independent completely positive trace-preserving map from $`k`$ copies of the supplied state to one $`M`$-dimensional output. It may use unrestricted ancillary memory, joint operations, intermediate measurements, classical adaptation, and discarded registers. It receives no evaluation oracle, preparation unitary, inverse, source reflection, or $`f`$-dependent advice.

Write

```math
\rho_f=\mathcal A\!\left(|a_f\rangle\langle a_f|^{\otimes k}\right),
\qquad
\overline F=\frac1{|\mathcal F|}\sum_{f\in\mathcal F}
\langle s_f|\rho_f|s_f\rangle,
```

where $`\mathcal F`$ is the set of all such injections. Fidelity to a pure target means this squared overlap.

**Theorem.** If $`\overline F\ge2/3`$, then

```math
\boxed{k>N/32.}
```

In particular, the same lower bound holds for a worst-case fidelity guarantee. Together with the [postselection construction](construction.md), the fixed-constant-error hard-budget copy complexity is $`\Theta(N)`$.

The lower bound is average-case over uniform injections, whereas the upper construction works for every injection. No claim of an exact optimal success probability or a matching vanishing-error copy law is made.

## A processor preserves the label Gram matrix

Let $`L=|\mathcal F|=(M)_N`$, and take a Stinespring isometry for $`\mathcal A`$. Write its pure output, including every retained or discarded auxiliary register, as

```math
|\Omega_f\rangle_{BE}=U|a_f\rangle^{\otimes k}.
```

The isometry is the same for every $`f`$. Its total-output Gram matrix is therefore exactly the source Gram

```math
G_k(f,g)=\langle a_f|a_g\rangle^k
=\left(\frac{|\{x:f(x)=g(x)\}|}{N}\right)^k.
```

Put $`p_f=\langle s_f|\rho_f|s_f\rangle`$. When $`p_f>0`$, define a normalized auxiliary state by projecting the desired output:

```math
|t_f\rangle_E=
\frac{(\langle s_f|_B\otimes I_E)|\Omega_f\rangle_{BE}}
{\sqrt{p_f}}.
```

If $`p_f=0`$, choose any normalized $`|t_f\rangle`$. In either case,

```math
\langle\Omega_f|s_f,t_f\rangle=\sqrt{p_f}.
```

These auxiliary states can depend arbitrarily on $`f`$. Their Gram matrix $`T_{f,g}=\langle t_f|t_g\rangle`$ is positive semidefinite with diagonal one and can be complex.

Introduce a mathematical register whose orthonormal labels are the injections themselves. The following two normalized pure states are used only in the proof:

```math
|\Xi\rangle=\frac1{\sqrt L}\sum_f|f\rangle|\Omega_f\rangle,
\qquad
|Z\rangle=\frac1{\sqrt L}\sum_f|f\rangle|s_f\rangle|t_f\rangle.
```

The processor is not given this register or a coherent superposition of different instances. Their overlap obeys

```math
\langle\Xi|Z\rangle
=\frac1L\sum_f\sqrt{p_f}
\ge\frac1L\sum_fp_f
=\overline F.
\tag{1}
```

Taking the partial trace over the physical registers gives, respectively,

```math
\sigma=\frac{G_k^{\mathsf T}}L,
\qquad
\tau=\frac{(H\circ T)^{\mathsf T}}L,
\qquad
H(f,g)=\langle s_f|s_g\rangle.
```

Here $`\mathsf T`$ denotes matrix transpose, not the auxiliary Gram matrix. With half trace distance $`D(\rho,\sigma)=\tfrac12\Vert\rho-\sigma\Vert_1`$, pure-state trace distance and contractivity imply

```math
D(\sigma,\tau)
\le\sqrt{1-|\langle\Xi|Z\rangle|^2}
\le\sqrt{1-\overline F^2}.
\tag{2}
```

Thus high output fidelity would force the unchanged source Gram state to be close to a target-times-garbage Gram state. This conclusion includes arbitrary final garbage, rather than assuming a clean return.

## The harmonic probabilities disagree

Suppose, for contradiction, that $`1\le k\le N/32`$. Let $`\Pi_k`$ be the equal-tail projector defined in the [source proof](input_harmonics.md). It is real and symmetric: the permutation action is real, and irreducible characters of the symmetric groups are real, so its central isotypic projectors can be chosen real. Therefore transposing the Gram matrices leaves their traces against $`\Pi_k`$ unchanged. This also handles complex auxiliary overlaps.

The source lemma gives

```math
\mathrm{Tr}(\Pi_k\sigma)
\ge1-\frac{k}{N-k+1}
>\frac{30}{31}.
\tag{3}
```

The output lemma applies to the arbitrary Gram matrix $`T`$ and gives

```math
\begin{aligned}
\mathrm{Tr}(\Pi_k\tau)
&\le\frac NM+\frac{3k+2}{N}+4N^{-4}\\
&\le N^{-3}+\frac3{32}+\frac2N+4N^{-4}
<0.126.
\end{aligned}
\tag{4}
```

All inequalities hold uniformly for the stated finite regime $`N\ge64`$, $`M\ge N^4`$. The probability difference in this one projective measurement is consequently greater than $`0.841`$. By the variational characterization of half trace distance,

```math
D(\sigma,\tau)>0.841.
```

If $`\overline F\ge2/3`$, (2) instead gives

```math
D(\sigma,\tau)
\le\sqrt{1-(2/3)^2}
=\frac{\sqrt5}{3}
<0.746,
```

a contradiction. The constants are conservative; their role is to prove a uniform linear lower bound.

For $`k=0`$, a fixed output cannot meet the average guarantee either. The average target state is invariant under range permutations, with largest eigenvalue $`N/M`$ on the global uniform vector. This is smaller than $`2/3`$ in the stated regime. The theorem follows.

## Error conventions and scope

The theorem uses squared fidelity. A half-trace-distance guarantee $`D(\rho_f,|s_f\rangle\langle s_f|)\le1/3`$ implies fidelity at least $`2/3`$ by the two-outcome measurement containing $`|s_f\rangle\langle s_f|`$. The implication also holds after averaging over instances. Conversely, fidelity $`2/3`$ alone need not imply half trace distance $`1/3`$; the proof does not use that converse.

A hard-budget heralded protocol that produces the exact target with success probability at least $`2/3`$ also meets the theorem's unconditional fidelity premise after its flag is discarded, regardless of its failure output. Hence heralding with constant success does not evade the lower bound.

The statement is a limit on a precise input/output interface. It does not assert a lower bound for ordinary function-oracle access, which has the inherited $`\Theta(\sqrt N)`$ query complexity in this range, or for a preparation circuit together with its inverse. It also does not make the classical sampling task hard: measuring the image register of one supplied sample already returns a uniform image element. The additional requirement is the coherent, unlabeled image state.
