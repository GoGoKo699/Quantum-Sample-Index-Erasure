# Quantum Sample Index Erasure

**Can supplied quantum examples replace an executable oracle when removing address labels while preserving coherence?** For a standard positive-amplitude encoding of an unknown classical injection, the optimal fixed-accuracy cost is linear in the number of addresses, even with unrestricted collective processing. The established evaluation-oracle version needs only a square-root number of calls.

An injection $`f:[N]\to[M]`$ supplies copies of

```math
|a_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|x\rangle|f(x)\rangle.
```

The requested output is the pure coherent image

```math
|s_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|f(x)\rangle.
```

Tracing out the address gives an ordinary mixture of values. The task requires the cross terms between distinct values as well.

## Main result

Let $`N\ge64`$ and $`M\ge N^4`$. Every processor achieving mean target fidelity at least $`2/3`$ over uniformly random injections requires more than $`N/32`$ source copies. The lower bound permits arbitrary joint quantum operations, unlimited auxiliary memory, adaptive measurements, and function-dependent discarded garbage.

A known projection of one address register onto its uniform state succeeds with probability $`1/N`$ and gives the exact target. At most $`\lceil N\log(1/\varepsilon)\rceil`$ attempts give unconditional half-trace error at most $`\varepsilon`$, including every failed attempt. Thus, at fixed accuracy in the stated range regime, the optimal specimen cost is $`\Theta(N)`$.

| Access to the unknown function | Fixed-accuracy cost | Attribution and qualification |
|---|---:|---|
| Supplied coherent graph-state copies | $`\Theta(N)`$ specimens | Linear copy lower bound developed here; upper by known index projection |
| Reversible function-evaluation oracle | $`\Theta(\sqrt N)`$ queries | Established index-erasure theorem [AMRR11, LR22] |
| Preparation unitary and its inverse | $`\Theta(\sqrt N)`$ queries in the worst case over completions | Amplitude-amplification upper and an explicit reduction to the established oracle lower bound |

The [precise theorem](science/model.md) distinguishes fidelity from half trace distance. The [resource account](science/resources.md) states preparation, known gates, memory, failure and precision costs, and explains why a specially informative source-unitary completion need not be hard. No QRAM or free function table is supplied.

## Why collective processing cannot remove the bottleneck

The proof compares representation sectors of the source and target Gram matrices. A new tuple-harmonic calculation shows that a sublinear supply of graph-state copies retains almost all its weight in matching domain/range sectors. An accurate coherent image, even with arbitrary garbage, has little weight there. Finite hook bounds and an elementary hypergeometric image-overlap tail make the contradiction uniform at a linear copy cutoff.

The injection-space representation theory and the oracle theorem are inherited foundations. [Related work](references/RELATED_WORK.md) identifies the added specimen result and explains why generic unknown-state projection or unitary-program lower bounds do not directly imply it for this positive classical encoding.

## Read the science

| Question | Authoritative account |
|---|---|
| What is supplied, requested and optimized? | [Model and theorem](science/model.md) |
| How are all failures and the output error accounted for? | [Matching construction](science/construction.md) |
| Why do copies retain matching harmonic weight? | [Input harmonics](science/input_harmonics.md) |
| Why can arbitrary output garbage not repair the mismatch? | [Output harmonics](science/output_harmonics.md) |
| How does the mismatch imply a linear copy bound? | [Approximation and lower bound](science/copy_lower_bound.md) |
| What do circuits, source acquisition and memory cost? | [Resources](science/resources.md) |
| What does the separation mean, and where does it stop? | [Interpretation](science/interpretation.md) |

The [science overview](science/README.md) connects these pages. The [retrieval guide](llms.txt) maps reader questions to the same authoritative routes.

## Reproduce the finite checks

Use Python 3.10 or later; the suite needs only its standard library.

```bash
python3 verification/run_all.py
```

The [verification guide](verification/README.md) describes exact rational checks, finite-field rank diagnostics, tested dimensions and limitations. The analytical asymptotic claim rests on the proof, not on agreement of small examples.

## Scope

The matching sample law concerns fixed accuracy and $`M\ge N^4`$. It is not an all-range theorem: at $`M=N`$, the target is the known uniform state and no copies are needed. A sharp vanishing-error law and optimal heralded-success frontier are not asserted.

The comparison separates two quantum input interfaces. It establishes no application-level classical-versus-quantum runtime advantage, hardware crossover or thermodynamic erasure cost. Source copies and executable oracles must each be physically supplied and charged.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

