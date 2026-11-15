# Model and main result

## From labeled examples to a coherent image

An ordinary random example of a function contains an address and its value. A quantum example can retain a coherent superposition of all such pairs. Removing the address by a partial trace removes the coherence between distinct values as well. The task here asks for the coherent image state, rather than that classical mixture.

Let $`N\le M`$ be known positive integers and let $`f:[N]\to[M]`$ be an unknown injection, with $`[N]=\{1,\ldots,N\}`$. A source supplies independent copies of

```math
|a_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|x\rangle|f(x)\rangle.
```

The requested output is

```math
|s_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|f(x)\rangle.
```

The input amplitudes are positive and exactly equal. The unknown information is the classical injection; arbitrary unknown phases are not part of the promise.

## Supplied resources and allowed processing

The processor receives copies of $`|a_f\rangle`$ and the classical sizes $`N,M`$. It receives no function-evaluation oracle, preparation circuit, inverse circuit, reflection about the source, or instance-dependent advice. It may perform arbitrary function-independent quantum channels, use arbitrary ancillas and classical randomness, keep quantum memory, process all copies collectively, measure adaptively, and discard function-dependent garbage. The lower bound places no computational, connectivity, or memory restriction on this processing.

The charged input resource is the number of consumed source copies. A fixed budget $`k`$ bounds the number on every branch. An algorithm that uses fewer copies on some branches can be padded by discarding unused supplied copies. Source preparation and delivery are physical input costs; no data-loading or QRAM oracle is implicit in the specimen model.

For output $`\rho_f`$, define target fidelity and half trace distance by

```math
F_f=\langle s_f|\rho_f|s_f\rangle,
\qquad
D_f=\frac12\Vert\rho_f-|s_f\rangle\langle s_f|\Vert_1.
```

Thus fidelity means the population of the pure target, not its square root. A uniform half-trace guarantee $`D_f\le\varepsilon`$ implies $`F_f\ge1-\varepsilon`$, by measuring the target projector. The lower bound below is stronger than a uniform-input assertion: it applies to mean fidelity for a uniformly random injection.

## Theorem: optimal fixed-accuracy copy cost

Let $`N\ge64`$ and $`M\ge N^4`$. Every processor whose mean fidelity over uniform injections is at least $`2/3`$ must consume more than $`N/32`$ copies. In particular, this applies to a processor attaining fidelity at least $`2/3`$ on every injection, or half trace error at most $`1/3`$ on every injection.

Conversely, for every $`1\le N\le M`$ and $`0<\varepsilon<1`$, a known index projection and at most

```math
k=\left\lceil N\log\frac1\varepsilon\right\rceil
```

copies produce an unconditional output with $`D_f\le\varepsilon`$ for every injection. For $`N=1`$, discarding the known address already gives the exact target.

Consequently, at any fixed half-trace accuracy $`0<\varepsilon\le1/3`$, the worst-case specimen complexity in the stated large-range regime is

```math
C_\varepsilon(N,M)=\Theta_\varepsilon(N).
```

The upper bound and its complete failure accounting are in [construction](construction.md). The lower bound is proved in [copy lower bound](copy_lower_bound.md), with the two load-bearing components in [input harmonics](input_harmonics.md) and [output harmonics](output_harmonics.md).

## Compare access models on the same task

| Input interface | Fixed-accuracy complexity | Scope |
|---|---:|---|
| Supplied graph-state copies | $`\Theta(N)`$ copies | This account; arbitrary collective processing and garbage, $`M\ge N^4`$ |
| Ordinary reversible evaluation oracle | $`\Theta(\sqrt N)`$ calls | Established index-erasure result [LR22, AMRR11]; same large-range regime |
| Preparation circuit and its inverse | $`\Theta(\sqrt N)`$ calls in the worst case over valid completions | Upper by amplitude amplification; lower by the explicit oracle-to-source reduction in [resources](resources.md) |

The last row is a worst-case access-model statement. A specially helpful completion of a preparation unitary can reveal more than its first column. The result does not assign the same lower bound to each individual completion.

An evaluation oracle generates one graph-state copy with one call. This does not make the interfaces interchangeable: an evaluation algorithm can choose fresh coherent query inputs and uncompute them, whereas a specimen processor receives the fixed source state. The new lower bound concerns that restricted source family; the ordinary oracle law and the representation-theoretic foundations are credited in [related work](../references/RELATED_WORK.md).

## What remains outside the theorem

The matching law is for fixed accuracy and a range at least $`N^4`$. It is not a sharp classification for all $`M`$, a matching vanishing-error law, an optimal heralded-success formula, or an application-level runtime advantage. In particular, if $`M=N`$, every injection is a permutation and the target is the known uniform state; no samples are needed. This boundary rules out an unqualified all-range linear law.

