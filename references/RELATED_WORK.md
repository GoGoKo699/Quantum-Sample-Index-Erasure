# Related work and attribution

[Scientific account](../science/README.md) · [Bibliography](references.bib)

The question here concerns **supplied quantum specimens**. For an unknown injection $`f:[N]\to[M]`$, each input is the coherent graph state $`N^{-1/2}\sum_x|x,f(x)\rangle`$; the desired output is the pure image sample $`N^{-1/2}\sum_x|f(x)\rangle`$. The [model](../science/model.md) permits arbitrary joint processing and discarded work, while supplying no evaluation, preparation or inverse oracle.

## Index erasure and its symmetry machinery

[Ambainis, Magnin, Roetteler and Roland (2011)](https://doi.org/10.1109/CCC.2011.24) established a matching square-root query lower bound for index erasure when the auxiliary memory must return to a fixed state. Their hybrid-adversary and symmetry methods are foundational state-generation tools.

[Lindzey and Rosmanis (2022)](https://www.rintonpress.com/xxqic22/qic-22-78/0594-0626.pdf), [arXiv:1902.07336v3](https://arxiv.org/abs/1902.07336v3), proved the same query order when function-dependent auxiliary memory may remain. Their theorem requires a sufficiently large codomain, including the present regime $`M\ge N^4`$. Thus the ordinary-oracle $`\Theta(\sqrt N)`$ comparison is inherited.

Their injection association scheme also supplies the proof's representation framework: multiplicity-free decomposition, equal-tail minimal irreducibles, dimension estimates, spherical-function bounds and the target-Gram decomposition. In the arXiv version, the relevant locations are Theorem 4.6, Definition 4.9, Propositions 4.3, 4.7–4.8 and 6.2, and the spherical expression used in Claim 7.1. Numbering differs in the journal version.

The addition here is the high minimal-sector mass of the **copy-input Gram**, together with a finite-cutoff final-state estimate and an approximation argument for unrestricted processors. These establish the linear specimen lower bound. The matching index-projection/retry upper bound is elementary. The earlier oracle lower bound alone transfers only a square-root specimen lower bound, because one oracle call can prepare one specimen.

## Why generic sample-based search is not the restricted lower bound

[Kimmel, Lin, Low, Ozols and Yoder (2017)](https://doi.org/10.1038/s41534-017-0013-7), [arXiv:1608.00281](https://arxiv.org/abs/1608.00281), already showed that the square-root search advantage can disappear when a starting-state unitary is replaced by copies. Their Lemma 3 treats a decision promise on the weight $`w`$ of an arbitrary unknown starting state in a known target subspace, with copy cost $`\Theta(\log(1/\epsilon)/w)`$.

That generic distinction is prior work. It does not prove the present bound for injection graph states. The usual normalized-projection obstruction can use two source states with a common rejected component and different accepted components. For graph states with disjoint target images, the entire source states are already orthogonal, so that construction does not satisfy this input promise. The copy lower bound here therefore needs the injection-family argument, rather than substituting $`w=1/N`$ into a theorem for arbitrary sources.

## Choi programs and known-input state preparation

[Muguruza and Speelman (2024)](https://quantum-journal.org/papers/q-2024-12-18-1573/), [arXiv:2402.18356v2](https://arxiv.org/abs/2402.18356v2), study port-based state preparation and universal programmable hybrid processors. Their Theorem 4.1 uses copies of an unknown unitary's Choi state to prepare its action on a classically specified input, with squared fidelity $`1-(1-1/d)^k`$ for $`k`$ ports in dimension $`d`$. This already supplies an analogous linear-copy projection mechanism.

The optimality theorems for the maximally entangled port resource retain Bob's port-selection/discard restriction. Their broader processor-memory lower bound instead ranges over all unknown unitaries and known inputs. Neither statement directly yields an unrestricted-processor lower bound for the present discrete injection promise. A graph specimen is a rectangular isometry program with positive computational-basis columns, and only one fixed input superposition is requested.

## Ensemble cloning asks for a different output

[Du, Cheng, Zhao, Ma and Yuan (2026)](https://doi.org/10.1038/s41467-026-74924-x), [arXiv:2606.27756v1](https://arxiv.org/abs/2606.27756v1), prove hardness results for cloning conditional states of a projected ensemble and estimating nonlinear ensemble properties from purification copies. The conditional-state cloning task retains a classical outcome label; its hardness applies to general unknown conditional states, including the paper's Haar-purification family.

For the injection specialization, the conditional states are the known basis rays $`|f(x)\rangle`$. Their labeled two-copy ensemble can be produced from **one** graph specimen by coherently copying its image register into a fresh basis register and then measuring the index. This outputs a classical mixture, not the pure image sample required here. Thus neither theorem subsumes the other: this project removes the index while preserving inter-label coherence, whereas ensemble cloning repeats a conditional state and retains its classical label.

## Scope of the contribution

The result identifies the specimen cost of one structured quantum-data conversion. It does not claim that copies and reversible access were previously interchangeable, that every erasure or ensemble transformation has the same cost, or that the oracle comparison establishes an application-level speedup. The finite large-codomain and fixed-error qualifications remain in the [theorem's model](../science/model.md).

The comparisons above identify the inherited conclusions and the remaining theorem. They are not an exhaustive priority certificate. Publication metadata and source versions are recorded in the [BibTeX file](references.bib).
