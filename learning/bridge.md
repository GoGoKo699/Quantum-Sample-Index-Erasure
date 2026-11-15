# From quantum algorithms to sample index erasure

[Learning overview](README.md) · [Selected anchor](anchor.md) · [30 milestones](milestones.md) · [Model and theorem](../science/model.md)

An example can contain an address and its value. A coherent quantum example contains a superposition of these pairs. The task asks whether the address can be removed while the values remain in a pure superposition.

For an unknown injection $`f:[N]\to[M]`$, the supplied specimen and desired output are

```math
|a_f\rangle=\frac1{\sqrt N}\sum_x|x\rangle|f(x)\rangle,
\qquad
|s_f\rangle=\frac1{\sqrt N}\sum_x|f(x)\rangle.
```

Injectivity means distinct addresses have distinct values. Simply discarding the address gives

```math
\operatorname{Tr}_{X}|a_f\rangle\langle a_f|
=\frac1N\sum_x|f(x)\rangle\langle f(x)|.
```

This mixture has the correct probabilities when measured in the value basis, but lacks the off-diagonal terms of $`|s_f\rangle\langle s_f|`$. The extra requirement is coherence between different values. One specimen already suffices for ordinary classical sampling.

## One label measurement and the cost of retrying

Take four addresses with values $`2,7,1,9`$. Apply Hadamards to the two address qubits and measure them. The all-zero outcome occurs with probability $`1/4`$ and leaves the value register in

```math
\frac12\bigl(|2\rangle+|7\rangle+|1\rangle+|9\rangle\bigr).
```

The values were never measured. For general known $`N`$, project the index onto $`|+_N\rangle=N^{-1/2}\sum_x|x\rangle`$. The accepted component is

```math
(|+_N\rangle\langle+_N|\otimes I)|a_f\rangle
=\frac1{\sqrt N}|+_N\rangle|s_f\rangle.
```

Its squared norm is $`1/N`$, so the mean number of fresh attempts is $`N`$. After at most $`k`$ attempts, total failure has probability $`(1-1/N)^k`$. Including a fixed output on that branch gives the [unconditional error bound](../science/construction.md); unsuccessful specimens are part of the cost. The four-address example illustrates the operation, not the large-range lower theorem.

## Locate the missing reflection

Childs §19.3 explains how amplitude amplification can turn a small marked component into a large one. It requires a reflection about the prepared starting state as well as a reflection marking success. Here the index success projector is known. A supplied circuit $`A_f|0\rangle=|a_f\rangle`$ together with its inverse would also provide

```math
R_{a_f}=A_f(2|0\rangle\langle0|-I)A_f^\dagger.
```

But a specimen is an output of a preparation, not permission to run or reverse its circuit. The copy model supplies neither $`A_f`$ nor $`A_f^\dagger`$. The lower theorem includes any strategy that tries to manufacture useful operations from copies, even with all specimens retained and processed jointly.

Childs §§21.1–21.4 provide the useful habit: state the input interface before comparing complexity. In this project, $`k`$ counts consumed graph specimens. In the established oracle problem, the count measures reversible evaluations. They are different resources. The [resource account](../science/resources.md) makes the inherited square-root oracle comparison and the preparation/inverse convention precise. The preparation/inverse upper bound works for every valid unitary completion, while its matching lower bound is a worst case over completions; a specially informative completion can be easier.

## Include every possible quantum processor

A completely positive trace-preserving map, abbreviated CPTP, describes a deterministic quantum operation after any unreported outcomes and auxiliary registers are forgotten. It includes measurements, adaptive classical decisions and discarding. Thus the specimen model does not restrict the processor to the simple retry circuit.

A Stinespring representation writes any such processor as one isometry $`U`$ followed by discarding a register $`E`$. The isometry preserves inner products; $`E`$ contains all retained or discarded work in this proof. For $`k`$ copies, write

```math
|\Omega_f\rangle_{BE}=U|a_f\rangle^{\otimes k}.
```

If the desired output on $`B`$ were exact, purity would force $`|\Omega_f\rangle=|s_f\rangle|t_f\rangle`$. The auxiliary vector $`|t_f\rangle`$ may depend arbitrarily on $`f`$. The proof must allow that dependence; demanding its return to a fixed state would prove a weaker statement.

## Put overlaps into a mathematical label register

Childs §§23.1–23.2 motivate tracking overlaps across possible hidden inputs. Here collect the $`k`$-copy input overlaps into a Gram matrix:

```math
G_k(f,g)=\langle a_f|a_g\rangle^k
=\left(\frac{A(f,g)}N\right)^k,
\qquad A(f,g)=|\{x:f(x)=g(x)\}|.
```

For the target, instead,

```math
H(f,g)=\langle s_f|s_g\rangle
=\frac{B(f,g)}N,
\qquad B(f,g)=|\operatorname{im}f\cap\operatorname{im}g|.
```

The source records agreement at the same addresses; the target records common values regardless of their addresses. Exact processing would therefore require $`G_k=H\circ T`$, where $`T(f,g)=\langle t_f|t_g\rangle`$ and $`\circ`$ multiplies corresponding entries. Allowing arbitrary positive semidefinite, diagonal-one $`T`$ allows arbitrary final garbage.

Let $`L`$ be the number of injections. A conceptual superposition $`L^{-1/2}\sum_f|f\rangle|\Omega_f\rangle`$ has label-register state $`G_k^{\mathsf T}/L`$. This converts the overlaps into a normalized density operator. The algorithm is **not** supplied the enormous register $`|f\rangle`$; it exists only in the lower-bound argument.

## Use symmetry to find a probability that cannot agree

Relabeling the domain and range acts on possible injections through $`S_N\times S_M`$. Childs §11.1 and §§15.1–15.2 supply the idea of decomposing a symmetry action into invariant sectors. The particular decomposition here is the injection representation, rather than the tensor-power Schur decomposition in the notes. Its formulas and research-level dependencies are supplied in [input harmonics](../science/input_harmonics.md).

A sector is called minimal when its two partition labels have the same tail: $`(N-\ell,\nu)`$ and $`(M-\ell,\nu)`$. The tail $`\nu`$ contains $`\ell`$ boxes below the long first row. Let $`\Pi_k`$ project onto these sectors with $`\ell\le k`$. Its role is a proof witness: ask what probability this projector would have on the two label states.

The [input argument](../science/input_harmonics.md) first separates repeated addresses from distinct-address tuples, then uses deletion maps and the injection decomposition. It proves

```math
\operatorname{Tr}\!\left(\Pi_k\frac{G_k^{\mathsf T}}L\right)
\ge1-\frac{k}{N-k+1}.
```

The [output argument](../science/output_harmonics.md) bounds the same probability on a target-times-garbage state, uniformly over all allowable $`T`$:

```math
\operatorname{Tr}\!\left(\Pi_k\frac{(H\circ T)^{\mathsf T}}L\right)
\le\frac NM+\frac{3k+2}{N}+4N^{-4}.
```

For $`N\ge64`$, $`M\ge N^4`$ and $`1\le k\le N/32`$, the first probability exceeds $`30/31`$, while the second is below $`0.126`$. A processor cannot preserve the first Gram state and simultaneously produce an accurate version of the second.

Neither the upper algorithm nor the lower proof requires the experimenter to implement Schur sampling or measure $`\Pi_k`$. These are mathematical tools for analyzing unrestricted processing.

## Turn the mismatch into a constant-error theorem

The [final proof](../science/copy_lower_bound.md) handles approximation using the isometric outputs. Define mean pure-target fidelity by $`\overline F=L^{-1}\sum_f\langle s_f|\rho_f|s_f\rangle`$. Fidelity here is this target population, and half trace distance is $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$.

Projecting each $`|\Omega_f\rangle`$ onto its target gives an auxiliary family $`|t_f\rangle`$ for which

```math
D\!\left(\frac{G_k^{\mathsf T}}L,
\frac{(H\circ T)^{\mathsf T}}L\right)
\le\sqrt{1-\overline F^{\,2}}.
```

If $`\overline F\ge2/3`$, this distance is below $`0.746`$. The harmonic probability difference is greater than $`0.841`$, which is impossible because any one measurement's probability difference is bounded by half trace distance. Hence $`k>N/32`$. Combined with the retry construction, this gives the linear copy law at fixed accuracy.

## Keep the endpoint and its boundary together

The theorem is a $`\Theta(N)`$ specimen law in the stated large-codomain regime, including arbitrary collective operations and garbage. The square-root reversible-oracle law is inherited prior work. The result does not provide a sharp vanishing-error law or an application runtime advantage. If $`M=N`$, the image is the entire known range and its uniform state needs no specimens; this is why the codomain promise matters.

For the complete story, follow the [30 milestones](milestones.md). For specialist details, use the [scientific index](../science/README.md), [related-work comparison](../references/RELATED_WORK.md) and [finite verification](../verification/README.md). The selected Childs notes remain the single educational anchor; the linked research papers supply the exact inherited proof ingredients.
