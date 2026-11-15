# Why an erased output has little matching harmonic weight

The [input calculation](input_harmonics.md) shows that a small supply of labeled samples has most of its harmonic weight in equal-tail representations. This page proves that an ideal erased output, even when accompanied by arbitrary function-dependent garbage, has little weight there. The [copy lower bound](copy_lower_bound.md) compares the two statements.

The argument uses the injection-space decomposition of Lindzey and Rosmanis [LR22, arXiv v3, Theorem 4.6 and Definition 4.9](https://arxiv.org/pdf/1902.07336v3). The earlier index-erasure proof develops a related final-Gram comparison in Section 6 and Claim 7.1. All estimates needed at the linear cutoff below are derived here; their earlier square-root cutoff is not used as a premise.

## Statement and notation

Use the [model](model.md): $`\mathcal F`$ is the set of injections $`f:[N]\to[M]`$, and $`L=|\mathcal F|=(M)_N`$. For $`f,g\in\mathcal F`$, put

```math
B(f,g)=|\operatorname{im}f\cap\operatorname{im}g|,
\qquad
H_{f,g}=\langle s_f|s_g\rangle=\frac{B(f,g)}N.
```

The action of $`S_N\times S_M`$ on $`\mathbb C[\mathcal F]`$ is multiplicity-free. Its irreducibles are the admissible pairs $`\lambda\otimes\mu`$ with $`\mu/\lambda`$ a horizontal strip. Write $`E_{\lambda,\mu}`$ for the corresponding orthogonal projector and $`d_{\lambda,\mu}`$ for its rank. The normalized primitive Gram matrix is

```math
T_{\lambda,\mu}=\frac{L}{d_{\lambda,\mu}}E_{\lambda,\mu}.
```

For $`\lambda=(N-\ell,\nu)`$, define $`\bar\lambda=(M-\ell,\nu)`$. These equal-tail pairs are called minimal. For an integer $`K\ge0`$, set

```math
\Pi_K=
\sum_{\substack{0\le\ell\le K\\\nu\vdash\ell}}
E_{(N-\ell,\nu),(M-\ell,\nu)},
```

including only valid partitions. A garbage Gram matrix means any positive semidefinite matrix $`T`$ indexed by $`\mathcal F`$ with $`T_{f,f}=1`$. It can have any rank, corresponding to an unrestricted garbage dimension.

**Output harmonic bound.** If $`N\ge64`$, $`M\ge N^4`$, and $`1\le K\le N/32`$, then every garbage Gram matrix satisfies

```math
\operatorname{Tr}\!\left[\Pi_K\frac{H\circ T}{L}\right]
\le \frac NM+\frac{3K+2}{N}+4N^{-4}.
\tag{1}
```

Here $`\circ`$ is the entrywise product. In particular, the bound does not assume that the garbage is fixed, known, classical, or independent of $`f`$.

## Remove the target's known uniform component

Let $`|u_M\rangle=M^{-1/2}\sum_y|y\rangle`$. Every target has the same overlap $`\langle u_M|s_f\rangle=\sqrt{N/M}`$. Its normalized component orthogonal to $`|u_M\rangle`$ has Gram matrix

```math
Q_{f,g}
=\frac{H_{f,g}-N/M}{1-N/M}
=\frac{M B(f,g)-N^2}{N(M-N)}.
```

Consequently,

```math
H=\frac NM J+\left(1-\frac NM\right)Q,
\tag{2}
```

where $`J`$ is the all-ones Gram matrix. The feature vectors for $`Q`$ lie in the standard representation of $`S_M`$, and the domain group $`S_N`$ acts trivially on them. Multiplicity-freeness therefore identifies

```math
Q=T_{(N),(M-1,1)}.
```

The explicit formula gives an especially useful pointwise inequality:

```math
Q_{f,g}\le \frac{B(f,g)}N\le1.
\tag{3}
```

The first inequality is equivalent to $`B(f,g)\le N`$. Negative entries of $`Q`$ are permitted; $`Q`$ itself is a positive semidefinite Gram matrix.

## Reduce arbitrary garbage to one primitive block

Average $`T`$ under $`S_N\times S_M`$. Since $`H`$ and $`\Pi_K`$ are invariant, this leaves the left side of (1) unchanged. The average remains positive semidefinite with diagonal one. The multiplicity-free decomposition writes it as a convex combination

```math
T=\sum_{\lambda,\mu} c_{\lambda,\mu}T_{\lambda,\mu},
\qquad c_{\lambda,\mu}\ge0,
\qquad \sum_{\lambda,\mu}c_{\lambda,\mu}=1.
```

It suffices to bound a primitive term. The $`J`$ part of (2) contributes at most $`N/M`$, because $`T/L`$ is a density matrix.

For the $`Q`$ part, the Schur product $`T_{\lambda,\mu}\circ Q`$ is the Gram matrix of tensor-product feature vectors. The features of $`Q`$ are domain-trivial, so tensoring with them preserves the $`S_N`$ label $`\lambda`$. Thus its trace against $`\Pi_K`$ is zero if $`N-\lambda_1>K`$. Otherwise, only $`E_{\lambda,\bar\lambda}`$ can contribute.

This domain-label argument is the content of the reduction used in [LR22, arXiv v3, Proposition 6.2](https://arxiv.org/pdf/1902.07336v3); the tensor-feature proof also explains why it applies to arbitrary garbage.

## Nonminimal garbage blocks are suppressed by dimension

Fix $`\lambda=(N-\ell,\nu)`$ with $`\ell\le K`$ and an admissible $`\mu\ne\bar\lambda`$. Symmetry of the entrywise-product trace gives

```math
\begin{aligned}
&\operatorname{Tr}\!\left[
E_{\lambda,\bar\lambda}
\frac{T_{\lambda,\mu}\circ Q}{L}\right]\\
&\qquad=
\frac{d_{\bar\lambda}}{d_\mu}
\operatorname{Tr}\!\left[
E_{\lambda,\mu}
\frac{T_{\lambda,\bar\lambda}\circ Q}{L}\right]
\le\frac{d_{\bar\lambda}}{d_\mu}.
\end{aligned}
\tag{4}
```

The last trace lies in $`[0,1]`$: the Schur product divided by $`L`$ is a density matrix. The common domain dimension $`d_\lambda`$ cancels in the ratio.

We now bound that ratio uniformly. Horizontal-strip interlacing gives $`\mu_{i+1}\le\lambda_i`$, so the tail $`\theta=(\mu_2,\mu_3,\ldots)`$ has at most $`N`$ boxes. It contains $`\nu`$ entrywise. Grow $`\nu`$ to $`\theta`$ by addable boxes, moving one box at each step from the first row. All intermediate shapes are valid because their first row is at least $`M-N>N`$.

For $`\alpha=(M-q,\theta)`$, $`|\theta|=q`$, the hook formula separates into

```math
d_\alpha=\binom Mq\frac{d_\theta}{P_\alpha},
\qquad
P_\alpha=
\prod_{c=1}^{\theta_1}
\left(1+\frac{\theta'_c}{M-q-c+1}\right).
\tag{5}
```

All hooks below the first row are exactly those of $`\theta`$. This proves (5) directly. The hook formula and Young branching are also recorded in [LR22, arXiv v3, Theorems 4.1–4.2](https://arxiv.org/pdf/1902.07336v3).

If $`\beta=(M-q-1,\theta^+)`$ is the next shape and $`q+1\le N`$, branching gives $`d_{\theta^+}\ge d_\theta`$. Moreover,

```math
P_\alpha\ge1,
\qquad
\log P_\beta\le\frac{N}{M-2N}\le\frac16,
\qquad P_\beta<\frac32.
```

The last two inequalities already hold for $`M\ge8N`$. Hence

```math
\frac{d_\beta}{d_\alpha}
\ge\frac23\frac{M-N}{N}
\ge\frac{M}{2N}.
```

A nonminimal $`\mu`$ requires at least one move, and every move has ratio greater than one. We obtain

```math
\frac{d_{\bar\lambda}}{d_\mu}\le\frac{2N}{M}.
\tag{6}
```

This finite bound replaces a fixed-rank asymptotic estimate.

## Minimal garbage blocks: a weighted overlap tail

Now let $`E=E_{\lambda,\bar\lambda}`$ and $`d=\operatorname{rank}E`$. Transitivity makes every diagonal entry $`d/L`$. Define the real spherical function

```math
\omega(f,g)=\frac Ld E_{f,g}.
```

The elementary projector identities imply

```math
|\omega(f,g)|\le1,
\qquad
\frac dL\sum_g|\omega(f,g)|^2=1.
\tag{7}
```

The first follows from positive semidefiniteness of $`E`$; the second is the diagonal entry of $`E^2=E`$. These are the spherical-function bounds recorded in [LR22, arXiv v3, Propositions 4.7–4.8](https://arxiv.org/pdf/1902.07336v3), here obtained from the projector normalization.

Fix the identity injection $`f_0(x)=x`$. Expanding the trace and using invariance gives the exact expression

```math
\operatorname{Tr}\!\left[E\frac{T_{\lambda,\bar\lambda}\circ Q}{L}\right]
=\frac dL\sum_{g\in\mathcal F}
|\omega(f_0,g)|^2 Q_{f_0,g}.
\tag{8}
```

Let $`B_g=|\operatorname{im}g\cap[N]|`$. For any integer $`1\le t\le N`$, split the sum at $`B_g=t`$. On the first part, (3) bounds $`Q`$ by $`t/N`$, and the weights in (7) sum to one. On the second, use $`Q\le1`$ and $`|\omega|\le1`$. Thus

```math
\operatorname{Tr}\!\left[E\frac{T_{\lambda,\bar\lambda}\circ Q}{L}\right]
\le\frac tN+d\,\Pr(B_g\ge t),
\tag{9}
```

where $`g`$ is uniform over injections. This does not require identifying cycle-path strata or taking an ordered limit.

The image of $`g`$ is a uniform $`N`$-subset of $`[M]`$. A union bound over fixed $`t`$-subsets of $`[N]`$ yields

```math
\Pr(B_g\ge t)
\le\binom Nt\frac{(N)_t}{(M)_t}
\le\left(\frac{N^2}{M-N}\right)^t.
\tag{10}
```

For the dimension, the standard-tableau count gives $`d_\lambda\le\binom N\ell d_\nu`$ and $`d_{\bar\lambda}\le\binom M\ell d_\nu`$. Since $`d_\nu^2\le\ell!`$, their product satisfies

```math
d=d_\lambda d_{\bar\lambda}\le(MN)^\ell.
\tag{11}
```

The inequality $`d_\nu^2\le\ell!`$ follows by decomposing the regular representation of $`S_\ell`$; (11) is also the dimension bound in [LR22, arXiv v3, Proposition 4.3](https://arxiv.org/pdf/1902.07336v3).

Choose $`t=3\ell+2`$. Because $`\ell\le K\le N/32`$ and $`N\ge64`$, this is at most $`N`$. Using $`M-N\ge M/2`$, (10)–(11) give

```math
\begin{aligned}
d\Pr(B_g\ge3\ell+2)
&\le(MN)^\ell\left(\frac{2N^2}{M}\right)^{3\ell+2}\\
&=\frac{4\,8^\ell N^{7\ell+4}}{M^{2\ell+2}}\\
&\le4N^{-4}\left(\frac8N\right)^\ell
\le4N^{-4}.
\end{aligned}
```

Together with (9), this bounds every minimal primitive term by $`(3K+2)/N+4N^{-4}`$. The nonminimal estimate (6) is smaller than this bound. Convexity and the $`N/M`$ term from (2) prove (1).

The cutoff, finite-$`M`$ estimates, and arbitrary-garbage reduction are now explicit. Proceed to the [approximation comparison](copy_lower_bound.md), which turns the harmonic mismatch into the copy lower bound.
