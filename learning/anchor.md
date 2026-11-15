# Educational anchor

[Learning overview](README.md) · [Source-to-project bridge](bridge.md) · [30 milestones](milestones.md) · [Scientific account](../science/README.md)

The selected source is **Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, 17 April 2025**: [author-hosted PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf).

Use the dated version above. Page numbers below are the printed numbers; the PDF has eight preceding pages. The source develops algorithms and lower-bound ideas. The [bridge](bridge.md) supplies the additional channel, specimen-access and injection-harmonic steps needed for this project.

| Source location | Printed pages | Connection to this project |
|---|---:|---|
| §19.3 | 88–89 | Understand the two reflections that make amplitude amplification possible, then identify which access a specimen does not supply. |
| §§21.1–21.4 | 97–99 | Specify a query interface and separate a charged input operation from the surrounding computation. |
| §11.1 | 47–49 | Organize a symmetry action into invariant representation spaces. |
| §§15.1–15.2 | 63–65 | See how symmetry sectors organize many-register states and how their weights can carry information. |
| §§23.1–23.2 | 109–113 | Use overlaps between different hidden inputs as a lower-bound object. |

Start with §19.3 and the [bridge's concrete example](bridge.md#one-label-measurement-and-the-cost-of-retrying). Read the symmetry sections when reaching the lower-bound route. Reading the entire notes is not a prerequisite.

## What is supplied here

The source does not prove the specimen theorem. The bridge defines arbitrary quantum channels and their isometric representation, explains the mathematical register that labels possible injections, and connects their Gram matrices to the harmonic comparison. The [source proof](../science/input_harmonics.md) and [output proof](../science/output_harmonics.md) contain the specialist derivations.

The injection representation formulas and spherical-function ingredients come from the research literature, especially [Lindzey–Rosmanis](../references/RELATED_WORK.md#index-erasure-and-its-symmetry-machinery). They are proof dependencies, rather than another educational anchor. Neither Schur sampling nor a physical measurement of the proof's harmonic projector is required by the [upper algorithm](../science/construction.md).

Continue to the [bridge](bridge.md), then use the [milestone map](milestones.md) to connect the components into the complete result.
