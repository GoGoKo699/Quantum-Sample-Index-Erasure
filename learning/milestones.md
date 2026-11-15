# The 30-milestone understanding map

The selected anchor is Childs, _Lecture Notes on Quantum Algorithms_, **17 April 2025**; see [anchor](anchor.md) for its exact version and [bridge](bridge.md) for the translation to this project. References to Childs below use that version's section numbering. The injection decomposition and other imported research ingredients are separately credited in the scientific pages and [related work](../references/RELATED_WORK.md).

There are **14 background/preliminary milestones and 16 narrative/innovation milestones**. The first phase connects individual states, operations, and representations into a common proof language. The second connects the actual algebraic mechanism into the theorem, its attaining algorithm, and its limits. Dependencies point to earlier targets; source links supply the corresponding definitions and derivations.

## Background/preliminaries — M01–M14

### M01 — A coherent example of an injection

**Central question.** What information is supplied by one labeled graph-state sample?

**Understanding targets.** Identify the known sizes, unknown classical injection, address register, and value register. Explain the equal positive amplitudes and the independence of fresh source copies.

**Dependencies and story role.** Starting point: connect an ordinary address-value example to its coherent encoding.

**Conceptual connection.** A supplied state and an executable evaluation oracle are different input interfaces, even when one oracle call can prepare that state.

**Sources.** [Model: supplied resources](../science/model.md); [bridge](bridge.md); Childs §§21.1–21.2, _Quantum query complexity_ and _Quantum queries_.

### M02 — The image sample and the image superposition

**Central question.** Why does discarding the address fail to produce the requested output?

**Understanding targets.** Compare the reduced mixture with the target's cross terms. Explain why both produce the same computational-basis sampling law but differ as quantum states.

**Dependencies and story role.** Requires M01. Move from the input's individual registers to the operational output contract.

**Conceptual connection.** Coherence is part of a state-generation task; a correct classical marginal distribution alone does not fulfill that task.

**Sources.** [Meaning of address disposal](../science/interpretation.md); [construction: four addresses](../science/construction.md); [bridge](bridge.md).

### M03 — A known projection with a rare accepted outcome

**Central question.** How can one source copy sometimes yield the exact coherent image?

**Understanding targets.** Follow the uniform-index projection, its unnormalized accepted vector, and the resulting probability $`1/N`$. Explain why the accepted index factors from the value state.

**Dependencies and story role.** Requires M01–M02. Identify the local operation used by the complete upper algorithm.

**Conceptual connection.** A useful conditional output must be accompanied by its success probability and consumed input.

**Sources.** [Construction: one attempt](../science/construction.md); [bridge: projection example](bridge.md); Childs §19.3, _Amplitude amplification and quantum counting_, for the role of an accepted subspace.

### M04 — Failed attempts and an unconditional output

**Central question.** What does a finite copy budget guarantee after all failures are counted?

**Understanding targets.** Explain the total-failure probability, fixed fallback output, and half-trace-distance bound. Distinguish a hard copy budget from the mean first-success stopping time.

**Dependencies and story role.** Requires M03. Assemble local projection attempts into a complete channel with an output on every branch.

**Conceptual connection.** Conditional exactness and unconditional accuracy are separate quantities; the construction accounts for both.

**Sources.** [Construction: bounded unconditional output](../science/construction.md); [model: error conventions](../science/model.md); [resources](../science/resources.md).

### M05 — What amplitude amplification can access

**Central question.** Which extra operations allow the rare projection outcome to be amplified?

**Understanding targets.** Identify the known success reflection and the source reflection. Explain how preparation and inverse calls construct the latter, and why state copies alone do not supply it for free.

**Dependencies and story role.** Requires M03–M04. Connect the familiar algorithmic primitive to this task's explicit access contract.

**Conceptual connection.** The quadratic improvement changes when reversible executable access is supplied; it cannot be charged as an operation already contained in a specimen.

**Sources.** Childs §19.3; [resources: source circuits and completions](../science/resources.md); [bridge](bridge.md).

### M06 — Channels, target population, and distance

**Central question.** How is the success of an arbitrary quantum processor measured?

**Understanding targets.** Interpret a completely positive trace-preserving map, squared fidelity to a pure target, half trace distance, and averaging over injections. Keep the implication from a trace-error guarantee to a fidelity guarantee in the correct direction.

**Dependencies and story role.** Requires M02 and M04. Replace the particular upper circuit by the unrestricted class to which the converse applies.

**Conceptual connection.** The theorem constrains an input/output channel, including its discarded registers, rather than one chosen measurement architecture.

**Sources.** [Model](../science/model.md); [copy lower bound: error conventions](../science/copy_lower_bound.md); [bridge: channel foundations](bridge.md).

### M07 — Gram matrices as records of a state family

**Central question.** How can pairwise overlaps represent an entire collection of inputs?

**Understanding targets.** Explain positive semidefiniteness, unit diagonal, and the normalized Gram density matrix. Recognize the source overlap as the fraction of addresses on which two injections agree.

**Dependencies and story role.** Requires M01 and M06. Introduce the mathematical object that the proof can follow through a processor.

**Conceptual connection.** Pairwise geometry, rather than identification of the unknown function, can obstruct a state-generation channel.

**Sources.** [Input harmonics: notation](../science/input_harmonics.md); [copy lower bound: preserved Gram matrix](../science/copy_lower_bound.md); [bridge](bridge.md). Childs §23.1, _Quantum adversaries_, provides broader overlap-based lower-bound context.

### M08 — Permuting addresses and values

**Central question.** Which symmetries preserve the family of injection instances?

**Understanding targets.** Explain the separate domain and range permutation actions, an invariant subspace, and an isotypic projector. Understand a projector's trace against a density matrix as a measurable sector probability.

**Dependencies and story role.** Requires M07. Organize the large Gram matrix by the symmetries of its actual input promise.

**Conceptual connection.** Instance symmetry reduces a channel comparison without restricting the processor's original freedom.

**Sources.** Childs §11.1, _A brief introduction to representation theory_, and §21.4, _Symmetrization_; [input harmonics: projector](../science/input_harmonics.md); [bridge](bridge.md).

### M09 — Young diagrams and the injection decomposition

**Central question.** Which representation pairs can occur for injections between two finite sets?

**Understanding targets.** Interpret a partition, its first row and tail, a horizontal strip, and the multiplicity-free admissible-pair rule. Distinguish this injection decomposition from a generic Schur transform.

**Dependencies and story role.** Requires M08. Translate symmetry into the labels used throughout the converse.

**Conceptual connection.** Matching tails define the particular sectors that the proof compares; the labels are not arbitrary categories of examples.

**Sources.** [Input harmonics: projector and tuple modules](../science/input_harmonics.md); LR22, arXiv v3, Theorem 4.6 and Definition 4.9, linked there. Childs §15.1, _The Schur decomposition_, supplies related representation language but not this imported theorem.

### M10 — Transposition sums and diagram contents

**Central question.** How can a sum of elementary permutations detect a diagram's shape?

**Understanding targets.** Read a cell's content and the total content of a Young diagram. Explain why a central transposition sum acts by a scalar on an irreducible block.

**Dependencies and story role.** Requires M08–M09. Supply the local spectral tool needed for the deletion-kernel calculation.

**Conceptual connection.** Counting how permutations change tuples will become a positive operator whose zero sectors are exactly identified.

**Sources.** [Input harmonics: central transpositions and contents](../science/input_harmonics.md), including the Jucys primary credit; [bridge](bridge.md). Childs §11.1 supplies the general irreducible-representation viewpoint.

### M11 — Dimensions and the first-row hook factor

**Central question.** How does moving a box from a long first row affect representation dimension?

**Understanding targets.** Interpret the hook formula, branching monotonicity, and separation of first-row hooks from tail hooks. Explain why finite dimension ratios can be bounded uniformly rather than at fixed tail size.

**Dependencies and story role.** Requires M09. Prepare the quantitative comparison of minimal and nonminimal output blocks.

**Conceptual connection.** The size of a symmetry block limits how much normalized probability can move into a much smaller block.

**Sources.** [Output harmonics: nonminimal blocks](../science/output_harmonics.md); LR22, arXiv v3, Theorems 4.1–4.2 and Proposition 4.3, credited there; [bridge](bridge.md).

### M12 — Overlap of random image sets

**Central question.** How unlikely is a large overlap between a random image and a fixed set?

**Understanding targets.** Recognize the image of a uniform injection as a uniform subset. Explain the union bound over fixed small subsets and the role of the range-size promise in its tail bound.

**Dependencies and story role.** Requires M01 and M04. Connect elementary sampling without replacement to a uniform estimate used in the converse.

**Conceptual connection.** A rare classical overlap event will bound a weighted quantum harmonic sum, without treating that sum as an ordinary measurement of the image.

**Sources.** [Output harmonics: weighted overlap tail](../science/output_harmonics.md); [model: range promise](../science/model.md); [bridge](bridge.md).

### M13 — Purifying a processor and its error

**Central question.** How can measurements and discarded garbage be included in one overlap argument?

**Understanding targets.** Explain a Stinespring isometry, arbitrary auxiliary output, projection onto a pure target, and contractivity under partial trace. Distinguish the proof's injection-label register from a resource supplied to the processor.

**Dependencies and story role.** Requires M06–M07. Build the channel-level framework that makes an unrestricted converse possible.

**Conceptual connection.** An ideal target with arbitrary residual registers has a target-times-garbage Gram matrix; approximation controls the distance to it.

**Sources.** [Copy lower bound: preserved Gram matrix](../science/copy_lower_bound.md); [bridge: Stinespring and Gram comparison](bridge.md). These foundations are supplied locally rather than assigned to an unstated Childs section.

### M14 — The complete language of the comparison

**Central question.** What must be compared to prove a lower bound on this input interface?

**Understanding targets.** Assemble the source, target, allowed channel, accuracy convention, invariant sector probability, and access comparison. Explain why an ordinary query lower bound alone does not establish a linear specimen lower bound.

**Dependencies and story role.** Requires M01–M13. Integrate the background into the full framework needed for the project's proof.

**Conceptual connection.** The converse will preserve the source family's Gram geometry while showing that every accurate target output has incompatible sector weights.

**Sources.** [Model](../science/model.md); [scientific route](../science/README.md); [bridge](bridge.md); Childs §§21.1–21.4 and §§23.1–23.2 for the surrounding query-model and lower-bound perspective.

## Narrative/innovation — M15–M30

### M15 — Occupancy inside the copy Gram matrix

**Central question.** How can powers of the source overlap be separated by the number of distinct addresses?

**Understanding targets.** Interpret the falling-factorial expansion and its nonnegative occupancy weights. Explain why it is an identity of Gram matrices and does not assume that the processor measures collision patterns.

**Dependencies and story role.** Requires M07 and M14. Start the new mechanism with a local algebraic identity.

**Conceptual connection.** Repeated addresses are accounted for exactly, so the argument remains valid when the number of copies grows linearly with the domain.

**Sources.** [Input harmonics: distinct-index expansion](../science/input_harmonics.md); [bridge](bridge.md).

### M16 — Distinct tuples and a uniform domain marginal

**Central question.** What makes the distinct-tuple source convenient for measuring sector weight?

**Understanding targets.** Explain its normalization and why injectivity makes its reduced address state maximally mixed on the ordered-tuple module. Convert a subspace dimension into a physical probability.

**Dependencies and story role.** Requires M02, M09, and M15. Replace each occupancy component by a source whose domain geometry is explicit.

**Conceptual connection.** Injectivity links the quantum marginal to an exact counting space, rather than an estimated distribution.

**Sources.** [Input harmonics: distinct tuples and reduced state](../science/input_harmonics.md); [model](../science/model.md).

### M17 — Deletion maps count tuple replacements

**Central question.** Which positive operator detects dependence on fewer tuple coordinates?

**Understanding targets.** Explain coordinate-summing deletion maps and the common kernel. Reconstruct the identity connecting their positive sum to value transpositions, coordinate swaps, unused-symbol transpositions, and the diagonal term.

**Dependencies and story role.** Requires M10 and M16. Identify the local operator that isolates the needed domain sectors.

**Conceptual connection.** A combinatorial replacement count becomes a spectral statement through the commuting permutation actions.

**Sources.** [Input harmonics: deletion maps and transposition identity](../science/input_harmonics.md); [bridge](bridge.md).

### M18 — The kernel is exactly the top domain degree

**Central question.** Why do the deletion kernels select precisely first row $`N-r`$?

**Understanding targets.** Use the tuple-module decomposition and content difference to identify zero eigenvalues. Explain why every lower-degree block has a strictly positive bound when $`N\ge2r`$.

**Dependencies and story role.** Requires M09–M10 and M17. Turn the positive-operator identity into an exact characterization, including its parameter condition.

**Conceptual connection.** The first-row label now describes the domain component retained by copies, rather than serving only as abstract notation.

**Sources.** [Input harmonics: top-degree characterization](../science/input_harmonics.md), with the imported Pieri and content identities credited there.

### M19 — From top degree to a matching pair of tails

**Central question.** Why must a top domain component have the same tail on the image side?

**Understanding targets.** Combine output degree at most $`r`$ with admissibility and diagram containment. Explain the equivariant intertwiner identity that equates physical isotypic probability with normalized Gram weight, including physical multiplicities.

**Dependencies and story role.** Requires M08–M09, M16, and M18. Connect the domain calculation to the joint projector used by the converse.

**Conceptual connection.** A large domain subspace alone is insufficient; equivariance and the output-degree bound provide the required joint-sector conclusion.

**Sources.** [Input harmonics: equal-tail pairs and physical/Gram weights](../science/input_harmonics.md); LR22 Theorem 4.6, credited there.

### M20 — A uniform source harmonic bound

**Central question.** How much matching harmonic weight survives in the full $`k`$-copy source?

**Understanding targets.** Use the deletion-map rank bound, tuple marginal, nested projectors, and occupancy weights to obtain the source estimate. Explain its uniformity in $`M\ge N`$ and its allowed linear-copy regime.

**Dependencies and story role.** Requires M15–M19. Integrate the input-side mechanism into the first load-bearing inequality.

**Conceptual connection.** The proof now controls the original unrestricted source family, with no imposed independent-measurement strategy.

**Sources.** [Input harmonics: source-weight lemma and final averaging](../science/input_harmonics.md); [copy lower bound](../science/copy_lower_bound.md).

### M21 — Separate the target's known uniform part

**Central question.** What part of the target family is already known without a source sample?

**Understanding targets.** Project target vectors onto the uniform state on the full range. Explain the standard-component Gram matrix, its domain-trivial action, and the pointwise bound by image overlap.

**Dependencies and story role.** Requires M02, M07–M09, and M12. Begin the output-side mechanism with the target's own structure.

**Conceptual connection.** The known component contributes the explicit $`N/M`$ term and anticipates the boundary where the target becomes known entirely.

**Sources.** [Output harmonics: uniform target component](../science/output_harmonics.md); [interpretation: range promise](../science/interpretation.md).

### M22 — Arbitrary garbage and primitive blocks

**Central question.** How can every possible auxiliary output be included without guessing its form?

**Understanding targets.** Interpret an arbitrary garbage Gram matrix, symmetry averaging, and its convex primitive decomposition. Explain why tensoring the domain-trivial target component preserves the domain representation label.

**Dependencies and story role.** Requires M06–M09, M13, and M21. Reduce the unrestricted output account to a precise family of representation blocks.

**Conceptual connection.** Symmetrization simplifies the proof's witness while preserving the processor's freedom and allowing complex auxiliary overlaps.

**Sources.** [Output harmonics: arbitrary garbage reduction](../science/output_harmonics.md); Childs §21.4; LR22 Proposition 6.2, credited in the scientific derivation.

### M23 — Nonmatching blocks lose weight by dimension

**Central question.** Why can a nonminimal garbage block contribute only a small matching weight?

**Understanding targets.** Follow the symmetric Schur-product trace and cancellation of the common domain dimension. Use the finite hook-factor growth along an admissible tail path, rather than a fixed-tail asymptotic.

**Dependencies and story role.** Requires M11, M19, and M22. Resolve the nonminimal case of the output estimate.

**Conceptual connection.** Diagram containment supplies the move path, and normalization supplies the dimension-ratio suppression.

**Sources.** [Output harmonics: nonminimal garbage blocks](../science/output_harmonics.md), including the explicit hook formula and its source credit.

### M24 — A primitive projector defines normalized weights

**Central question.** How does an isotypic projector produce the weighted overlap sum in the minimal case?

**Understanding targets.** Derive the constant diagonal, bounded normalized entries, and row-square normalization from transitivity, positivity, and idempotence. Explain the exact trace expression without importing a cutoff from an earlier query proof.

**Dependencies and story role.** Requires M07–M08, M20–M22. Identify the mathematical object remaining after nonminimal blocks have been controlled.

**Conceptual connection.** Elementary projector identities supply the spherical-function properties actually needed by this argument.

**Sources.** [Output harmonics: minimal garbage blocks](../science/output_harmonics.md); LR22 Propositions 4.7–4.8 and the comparison with its Section 6, credited there.

### M25 — A finite overlap cutoff at linear rank

**Central question.** How does a rare image overlap control the weighted minimal-block sum uniformly?

**Understanding targets.** Split the sum into small and large overlaps, combine the elementary hypergeometric tail with the dimension bound, and explain the cutoff $`3\ell+2`$. Keep $`M\ge N^4`$ and the rank range visible throughout.

**Dependencies and story role.** Requires M11–M12 and M24. Supply the quantitative step that permits a linear copy lower bound.

**Conceptual connection.** The estimate is finite and uniform in the growing diagram tail; it does not inherit the earlier oracle proof's square-root cutoff.

**Sources.** [Output harmonics: weighted overlap tail and cutoff arithmetic](../science/output_harmonics.md); [model: parameter regime](../science/model.md).

### M26 — Every ideal erased output has little matching weight

**Central question.** How do the target decomposition and both garbage cases combine into one bound?

**Understanding targets.** Assemble the known uniform contribution, nonminimal dimension ratio, minimal overlap bound, and convexity. Explain why the resulting output inequality covers arbitrary auxiliary dimension and function dependence.

**Dependencies and story role.** Requires M21–M25. Integrate the output-side mechanism into the second load-bearing inequality.

**Conceptual connection.** The source and ideal output are now bounded in the same projector, making a channel-level contradiction possible.

**Sources.** [Output harmonic bound](../science/output_harmonics.md); [copy lower bound](../science/copy_lower_bound.md).

### M27 — Approximate outputs still force close Gram states

**Central question.** Why cannot a small output error hide the harmonic mismatch?

**Understanding targets.** Project a Stinespring output onto its target, normalize the resulting garbage, and form the proof-only label purifications. Explain the average-overlap inequality and the square-root trace-distance bound, including complex Gram transposes.

**Dependencies and story role.** Requires M06–M07, M13, M20, and M26. Connect ideal harmonic statements to an approximate arbitrary processor.

**Conceptual connection.** The argument obtains a target-times-garbage comparison from actual fidelity; it never assumes exact output factorization for an imperfect processor.

**Sources.** [Copy lower bound: preserved Gram matrix](../science/copy_lower_bound.md); [bridge: approximation comparison](bridge.md).

### M28 — The quantitative contradiction

**Central question.** Which two probabilities cannot coexist when only a small linear number of copies is supplied?

**Understanding targets.** Compare the source and output sector bounds for $`k\le N/32`$ with the fidelity-based trace-distance bound. Explain the average-case theorem and the separate zero-copy endpoint without treating conservative constants as optimal.

**Dependencies and story role.** Requires M20, M26, and M27. Join the local proof components into the linear specimen converse.

**Conceptual connection.** One mathematically defined projector witnesses an incompatibility for every allowed processor, including those with unlimited memory and garbage.

**Sources.** [Copy lower bound: theorem and harmonic disagreement](../science/copy_lower_bound.md); [model: main result](../science/model.md).

### M29 — A matching law with paid access and controls

**Central question.** What exactly is matched by the linear upper and lower bounds?

**Understanding targets.** Combine the hard-budget construction with the fixed-accuracy converse. Account for source acquisitions, known controls, precision, streaming memory, and the distinction between evaluation calls and copies; explain the worst-case-over-completions qualifier for source circuits.

**Dependencies and story role.** Requires M03–M06 and M28. Turn the proved inequality into a complete operational resource comparison.

**Conceptual connection.** The attaining algorithm needs little coherent memory, while the converse permits much more; an input-interface gap is not an application runtime advantage.

**Sources.** [Construction](../science/construction.md); [resources](../science/resources.md); Childs §19.3 and §§21.1–21.2; [related work](../references/RELATED_WORK.md).

### M30 — The whole result and its boundary

**Central question.** What can now be concluded, after inherited ingredients and all qualifiers are stated?

**Understanding targets.** Explain the all-positive injection source, linear copy requirement, arbitrary-processor scope, and inherited square-root executable-access comparison as one scientific story. Use $`M=N`$ to expose the need for the range promise, and distinguish fixed accuracy from unproved optimal vanishing-error or heralded laws.

**Dependencies and story role.** Requires M14 and M15–M29. Integrate the narrative into the contribution, its significance, and its actual limits.

**Conceptual connection.** Coherent examples contain quantum data, yet their presence does not supply the reversible operations that quantum algorithms may require.

**Sources.** [Model](../science/model.md); [interpretation](../science/interpretation.md); [related work](../references/RELATED_WORK.md); [scientific route](../science/README.md); [anchor and bridge](anchor.md).
