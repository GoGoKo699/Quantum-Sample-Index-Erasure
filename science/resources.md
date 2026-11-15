# Resource accounting and access comparison

## Specimen preparation

The input model counts each independently supplied graph-state copy as one consumed specimen. If physically acquiring a copy costs $`C_a`$ gates, a delivery time $`\tau_a`$, or other resources, those costs multiply the actual number consumed. The theorem does not build an unknown classical table into a free circuit.

For a hard budget $`k=\lceil N\log(1/\varepsilon)\rceil`$, the [construction](construction.md) makes at most $`k`$ source acquisitions and $`k`$ index measurements, including failed attempts. It has worst-case serial source latency $`k\tau_a`$ when the copies are delivered one at a time. Parallel delivery can change elapsed time and memory but does not reduce the specimen lower bound.

Let $`n=\lceil\log_2 N\rceil`$ and $`m=\lceil\log_2 M\rceil`$. Each input has $`n+m`$ qubits. For power-of-two $`N`$, known address controls cost $`O(kn)`$ elementary Clifford gates and measurements, in addition to source acquisition and classical stopping control. Peak coherent storage is $`n+m`$ input/output qubits, plus any known uniform-preparation ancillas. A classical budget counter uses $`O(\log k)`$ bits. No quantum bank of $`k`$ copies is needed by the upper algorithm.

For general known $`N`$, the interval-prefix uniform preparation in [construction](construction.md) uses polynomially many gates and arithmetic operations in $`n`$ and the rotation precision. These are known-instance controls, not queries to $`f`$. If the full measurement instrument in each trial is approximated within half diamond error $`\delta`$, a hybrid over the at-most-$`k`$ trials bounds the error of the complete adaptive output instrument by $`k\delta`$. Use the ideal algorithm with failure allowance $`\varepsilon/2`$ and choose $`\delta\le\varepsilon/(2k)`$ to keep total half-trace error at most $`\varepsilon`$. This budgets unconditional error; no unproved conditional-success stability is assumed.

No thermodynamic cost, error-correction overhead, geometry, or physical source construction is optimized. The sample theorem allows arbitrary processing, while the explicit upper is deliberately a simple streaming implementation.

## Ordinary evaluation access

An ordinary function oracle acts reversibly on an address and a padded value register, for example

```math
O_f|x,z\rangle=|x,z\mathbin{\oplus}f(x)\rangle.
```

On valid addresses it prepares $`|a_f\rangle`$ from $`|+_N\rangle|0\rangle`$ in one query. Padding behavior is fixed and supplies no extra information. The established index-erasure upper and lower bounds give $`\Theta(\sqrt N)`$ oracle calls at fixed accuracy in the range regime used here [AMRR11, LR22]. Those calls are not consumed examples: the algorithm can select and uncompute coherent oracle inputs.

The established oracle upper cleans the address through quantum search/uncomputation. The corresponding query lower bound permits arbitrary final garbage. These facts are credited predecessors, not new theorems of this account; see [related work](../references/RELATED_WORK.md).

## Source circuits and arbitrary completions

Suppose a stronger interface supplies a unitary $`U_f`$ with

```math
U_f|0\rangle=|a_f\rangle
```

and its inverse. A source reflection $`U_f(2|0\rangle\langle0|-I)U_f^\dagger`$ costs two source-circuit calls. The known success projector $`P_N\otimes I`$ has weight $`1/N`$. Amplitude amplification therefore gives the coherent image with $`O(\sqrt N)`$ preparation/inverse calls at fixed accuracy. The known source index factors from the successful output.

This upper works for every valid completion of the preparation unitary. A matching lower is a worst-case statement over completions. Explicitly choose

```math
U_f=O_f(W_N\otimes I).
```

One use of $`U_f`$ or $`U_f^\dagger=(W_N^\dagger\otimes I)O_f^\dagger`$ is simulated with one ordinary evaluation-oracle call and known controls. An algorithm working uniformly over all valid completions would work on this family and would contradict the inherited $`\Omega(\sqrt N)`$ evaluation lower bound if it used fewer calls. A specially informative completion need not be hard; no per-completion lower claim is made.

The comparison isolates executable, reversible access as a resource. It is not a classical-versus-quantum runtime claim, since both interfaces and both processors are quantum.

