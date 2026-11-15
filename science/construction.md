# A matching specimen algorithm

The [model](model.md) supplies copies of a coherent graph state, but no source reflection. A measurement on the known index space suffices for a simple linear-cost preparation.

## One attempt

Let

```math
|+_N\rangle=\frac1{\sqrt N}\sum_{x=1}^N|x\rangle,
\qquad P_N=|+_N\rangle\langle+_N|.
```

Apply the two-outcome measurement $`\{P_N,I-P_N\}`$ to the index of one fresh source copy. The unnormalized accepted state is

```math
(P_N\otimes I)|a_f\rangle
=\frac1{\sqrt N}|+_N\rangle|s_f\rangle.
```

The success probability is exactly $`1/N`$, independent of $`f`$. Conditional on success, the value register is exactly the desired coherent state and factors from the measured index. No value or matched address is measured.

On failure discard the entire failed copy and use a fresh one. This disposal is allowed in the specimen model. It does not assert that erasing an unknown input register coherently is free.

## A bounded, unconditional output

Try at most $`k`$ independent copies and stop on the first success. If all attempts fail, output any fixed known state $`\sigma_0`$. The resulting channel has output

```math
\rho_f=(1-q_k)|s_f\rangle\langle s_f|+q_k\sigma_0,
\qquad q_k=(1-1/N)^k.
```

Therefore

```math
\frac12\Vert\rho_f-|s_f\rangle\langle s_f|\Vert_1
\le q_k\le e^{-k/N}.
```

Choosing $`k=\lceil N\log(1/\varepsilon)\rceil`$ proves the upper bound. All failed attempts and the total-failure output are included. The theorem concerns this unconditional output, rather than a good conditional state produced with an uncharged small success probability.

Without a hard budget, the first-success stopping time has mean exactly $`N`$. This observation describes the construction; the principal lower theorem is stated for fixed copy budgets.

## Controls and memory

A known uniform-state preparation $`W_N|0\rangle=|+_N\rangle`$ implements the index measurement by applying $`W_N^\dagger`$ and testing the all-zero outcome. For $`N=2^n`$, $`W_N=H^{\otimes n}`$ after the known relabeling from $`[N]`$ to binary strings. Thus a trial needs $`n`$ Hadamards and a computational-basis measurement on the address.

For other known $`N`$, pad to $`2^{\lceil\log_2 N\rceil}`$ and prepare the uniform superposition on the known initial interval. A binary-prefix construction chooses each next bit according to the number of interval elements extending that prefix. Complete subtrees need only Hadamards, and at most one partial interval continues at each depth. The required counts and rotations depend only on $`N`$; their arithmetic and finite-precision synthesis are charged in [resources](resources.md). There is no table of the unknown function.

Only one graph-state copy is live at a time. The accepted value register is retained; failed source registers can be measured or released. Thus linear specimen cost does not imply linear coherent peak memory. This distinction matters because the [converse](copy_lower_bound.md) nevertheless allows all copies to be retained and processed jointly.

## Four addresses

For the injection $`f(1)=2,f(2)=7,f(3)=1,f(4)=9`$, the source is a superposition of the four labeled pairs. Measuring the two-qubit index after Hadamards accepts the all-zero outcome with probability $`1/4`$. Its value register is

```math
\frac12\bigl(|2\rangle+|7\rangle+|1\rangle+|9\rangle\bigr).
```

Simply tracing out the original index instead gives the equal mixture of these four values. Both states have the same computational-basis sampling law, but only the first retains the cross terms required by the output contract.

