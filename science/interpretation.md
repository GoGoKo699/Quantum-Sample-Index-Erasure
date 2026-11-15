# Meaning and boundaries

## Coherent examples are data, not executable access

Each supplied example already contains a coherent superposition of all address-value pairs. Nevertheless, a processor cannot generally turn a sublinear number of these examples into a coherent superposition of the values. The [linear lower bound](copy_lower_bound.md) includes unlimited collective processing, quantum memory, measurements, and discarded garbage.

The obstruction is not an unknown phase convention. All source amplitudes are equal and positive, and the unknown object is an ordinary classical injection. Nor is it explained by restricting the processor to independent measurements. The proof identifies representation components retained by source copies that are nearly absent from any accurate target output, even after arbitrary garbage is allowed.

An executable oracle can instead query and uncompute on chosen coherent inputs. Its established square-root query law therefore supplies a sharp separation between two quantum input interfaces on the same standard state-generation problem.

## Why discarding an address does not solve the task

Tracing out the index gives

```math
\mathrm{Tr}_X|a_f\rangle\langle a_f|
=\frac1N\sum_x|f(x)\rangle\langle f(x)|.
```

The target density operator additionally contains all cross terms $`|f(x)\rangle\langle f(x')|/N`$ with $`x\ne x'`$. The mixture is enough to produce ordinary image samples; it is not the requested quantum state. In this account, index erasure names that coherence-preserving state-generation task and makes no statement about heat or physical memory erasure.

## The range promise matters

If $`M=N`$, every image is the full known range and the target can be prepared without source copies. More generally, a fixed uniform state on the full range has fidelity $`N/M`$ with every target. The lower theorem consequently keeps $`M\ge N^4`$ visible. Its proof uses the rarity of overlap between two random image sets in that regime; it is not a proof of the same linear law at every range size.

The representation argument is finite at each $`N,M`$. The asymptotic fixed-accuracy statement follows by taking $`N\to\infty`$ while maintaining $`M\ge N^4`$. No order of limits in accuracy is hidden: a sharp vanishing-error law is not established.

## Source, processing, and output sizes

For $`M=N^4`$, a source copy occupies only $`O(\log N)`$ qubits. The lower bound is therefore linear in domain cardinality rather than in register width. The attaining algorithm uses logarithmic coherent memory because it processes one copy at a time. Collective storage is allowed by the converse but cannot remove the sample bottleneck.

Producing or executing a function oracle can itself be expensive. The [resource account](resources.md) keeps those costs explicit and compares interfaces without assuming free data loading. No application-level crossover follows merely from the sample/query separation.

