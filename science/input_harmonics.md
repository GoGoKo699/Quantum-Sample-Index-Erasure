# Source copies retain minimal harmonic weight

[Model](model.md) · [Output harmonic bound](output_harmonics.md) · [Copy lower bound](copy_lower_bound.md)

The source supplies copies of a labelled superposition. This page identifies a part of its symmetry decomposition that remains large until the copy count is linear in the domain size. The [output bound](output_harmonics.md) shows why an erased image state, even with arbitrary residual registers, has little weight in the same part.

Throughout, let $`\mathcal F`$ be the injections $`f:[N]\to[M]`$, let $`L=(M)_N`$, and use the [model's conventions](model.md):
 
```math
|a_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|x\rangle|f(x)\rangle,
\qquad
|s_f\rangle=\frac1{\sqrt N}\sum_{x=1}^N|f(x)\rangle.
```

Here $`(z)_r=z(z-1)\cdots(z-r+1)`$ denotes a falling factorial. Write

```math
A(f,g)=|\{x:f(x)=g(x)\}|,
\qquad
G_k(f,g)=\langle a_f|a_g\rangle^k
=\left(\frac{A(f,g)}N\right)^k.
```

The matrix $`G_k/L`$ is positive semidefinite with trace one. The target Gram matrix is $`H(f,g)=\langle s_f|s_g\rangle=B(f,g)/N`$, where $`B(f,g)=|\operatorname{im}f\cap\operatorname{im}g|`$; it is used on the [output side](output_harmonics.md).

## The projector and the statement

The group $`S_N\times S_M`$ acts on injections by

```math
(\sigma,\tau)\cdot f=\tau\circ f\circ\sigma^{-1}.
```

Its permutation representation on $`\mathbb C[\mathcal F]`$ is multiplicity-free. Its irreducibles are the pairs $`\lambda\otimes\eta`$ for which $`\lambda\vdash N`$, $`\eta\vdash M`$, and $`\eta/\lambda`$ is a horizontal strip. A horizontal strip contains at most one box in each column. This is the injection-module decomposition in [LR22, Theorem 4.6](https://arxiv.org/pdf/1902.07336v3), using the arXiv version's numbering.

A pair is **minimal** when its two diagrams have the same tail:

```math
\lambda=(N-\ell,\nu),
\qquad
\overline\lambda=(M-\ell,\nu),
\qquad
\nu\vdash\ell.
```

Let $`E_{\lambda,\eta}`$ be its orthogonal isotypic projector. For $`K\le N/2`$, define

```math
\Pi_K
=\sum_{\substack{0\le\ell\le K\\\nu\vdash\ell}}
E_{(N-\ell,\nu),(M-\ell,\nu)},
```

with only valid partitions included. This is the equal-tail convention of [LR22, Definition 4.9](https://arxiv.org/pdf/1902.07336v3).

**Source-weight lemma.** For integers $`M\ge N`$ and $`1\le k\le N/2`$,

```math
\boxed{
\operatorname{Tr}\!\left(\Pi_k\frac{G_k}{L}\right)
\ge 1-\frac{k}{N-k+1}.
}
```

The proof below concerns the supplied states themselves. It places no restriction on how a subsequent processor uses its copies.

## 1. Separate the numbers of distinct indices in the Gram matrix

Let $`\left\{\begin{smallmatrix}k\\r\end{smallmatrix}\right\}`$ be a Stirling number of the second kind. The falling-factorial identity gives

```math
A^k
=\sum_{r=1}^k
\left\{\begin{matrix}k\\r\end{matrix}\right\}(A)_r.
```

Consequently,

```math
G_k=\sum_{r=1}^k w_r J_r,
\qquad
w_r=
\left\{\begin{matrix}k\\r\end{matrix}\right\}
\frac{(N)_r}{N^k},
\qquad
J_r(f,g)=\frac{(A(f,g))_r}{(N)_r}.
```

The weights are nonnegative and sum to one, by the same identity at $`A=N`$. Each $`J_r`$ is the Gram matrix of the normalized distinct-tuple states

```math
|\Phi_f^{(r)}\rangle
=\frac1{\sqrt{(N)_r}}
\sum_{\substack{x_1,\ldots,x_r\in[N]\\
x_1,\ldots,x_r\ \mathrm{distinct}}}
|x_1,\ldots,x_r\rangle
|f(x_1),\ldots,f(x_r)\rangle.
```

Thus this is a convex identity of Gram matrices. It does not assume that the processor measures equality patterns, removes registers, or discards coherence between different patterns.

Let $`V_r(N)`$ be the space with orthonormal basis the ordered distinct $`r`$-tuples from $`[N]`$. Since $`f`$ is injective, the output tuples in $`|\Phi_f^{(r)}\rangle`$ are orthogonal. Its reduced domain state is therefore exactly

```math
\operatorname{Tr}_Y
|\Phi_f^{(r)}\rangle\langle\Phi_f^{(r)}|
=\frac{I_{V_r(N)}}{(N)_r}.
```

This maximally mixed marginal will turn a dimension estimate into a source-weight estimate.

## 2. Identify the top domain degree by deletion maps

For $`j\in[r]`$, define the linear deletion map $`D_j:V_r(N)\to V_{r-1}(N)`$ by

```math
D_j|x_1,\ldots,x_r\rangle
=|x_1,\ldots,x_{j-1},x_{j+1},\ldots,x_r\rangle.
```

On coefficient vectors, this sums over the deleted coordinate. Set

```math
\mathscr H_r(N)=\bigcap_{j=1}^r\ker D_j,
\qquad
\mathcal D_r=\sum_{j=1}^rD_j^\dagger D_j.
```

The rank inequality immediately gives

```math
\begin{aligned}
\operatorname{codim}\mathscr H_r(N)
&\le\sum_{j=1}^r\operatorname{rank}D_j\\
&\le r(N)_{r-1},
\end{aligned}
```

so

```math
\frac{\dim\mathscr H_r(N)}{(N)_r}
\ge 1-\frac{r}{N-r+1}.
```

We next show that, when $`N\ge2r`$, this kernel consists precisely of the $`S_N`$ components whose diagram has first row $`N-r`$.

### The exact transposition identity

Let $`C_N`$ denote the action on $`V_r(N)`$ of the sum of all transpositions in $`S_N`$. Let $`C_r`$ denote the sum of all swaps of tuple positions, the commuting $`S_r`$ action. Counting the effects of transpositions on a basis tuple gives

```math
\boxed{
\mathcal D_r
=C_N-C_r-
\left[\binom{N-r}{2}-r\right]I.
}
```

There are three cases. Transposing two unused symbols fixes the tuple and contributes $`\binom{N-r}{2}I`$. Transposing two used symbols swaps their positions and contributes $`C_r`$. Transposing a used symbol with an unused one makes one coordinate replacement. The latter replacements are $`\mathcal D_r-rI`$, because every $`D_j^\dagger D_j`$ also includes the unchanged tuple once. This accounts for the diagonal term $`rI`$.

### The contents calculation

Apply the injection-module decomposition again, now to $`S_r\times S_N`$ acting on ordered $`r`$-tuples. It gives

```math
V_r(N)
\cong
\bigoplus_{\substack{\lambda\vdash N,\ \mu\vdash r\\
\lambda/\mu\ \mathrm{horizontal}}}
S^\lambda\otimes S^\mu.
```

This is [LR22, Theorem 4.6](https://arxiv.org/pdf/1902.07336v3) with the smaller domain size $`r`$. For $`N\ge2r`$, write

```math
\lambda=(N-\ell,\nu),
\qquad
\nu\vdash\ell,
\qquad
0\le\ell\le r.
```

The horizontal-strip condition is equivalent to $`\mu/\nu`$ being a horizontal strip of size $`s=r-\ell`$. This follows directly from the interlacing inequalities; the long first row is at least $`r`$.

For a partition $`\alpha`$, let

```math
c(\alpha)=\sum_{(i,j)\in\alpha}(j-i)
```

be the sum of its box contents. The central sum of transpositions acts on $`S^\alpha`$ by $`c(\alpha)`$. In particular,

```math
c(\lambda)
=\binom{N-\ell}{2}+c(\nu)-\ell.
```

The displayed operator identity therefore gives the following eigenvalue on the $`(\lambda,\mu)`$ block:

```math
\begin{aligned}
d(\lambda,\mu)
&=c(\lambda)-c(\mu)
-\binom{N-r}{2}+r\\
&=s(N-r)+\frac{s(s+1)}2
-\bigl[c(\mu)-c(\nu)\bigr].
\end{aligned}
```

If $`s=0`$, then $`\mu=\nu`$ and this eigenvalue is zero. If $`s\ge1`$, the added boxes occupy $`s`$ distinct columns of a diagram with $`r`$ boxes. Their contents are bounded above by the contents of the final $`s`$ columns of a first row of length $`r`$. Hence

```math
c(\mu)-c(\nu)
\le (r-s)+\cdots+(r-1)
=sr-\frac{s(s+1)}2,
```

and

```math
d(\lambda,\mu)
\ge s(N-2r+s+1)>0.
```

Because $`\mathcal D_r=\sum_jD_j^\dagger D_j`$, its kernel is exactly $`\mathscr H_r(N)`$. The zero blocks are precisely $`\ell=r`$, which establishes the top-degree characterization. The inherited contents identity is the degree-one case of Jucys's content-eigenvalue result for symmetric polynomials in the Jucys–Murphy elements: the first symmetric polynomial is the sum of all transpositions. See [Jucys, Reports on Mathematical Physics 5, 107–112 (1974)](https://doi.org/10.1016/0034-4877(74)90019-6). The use here is the explicit deletion-operator calculation and its kernel estimate.

The reduced-state formula now yields

```math
\left\|
(P_{\mathscr H_r(N)}\otimes I)
|\Phi_f^{(r)}\rangle
\right\|^2
=\frac{\dim\mathscr H_r(N)}{(N)_r}
\ge1-\frac{r}{N-r+1}.
```

## 3. Top domain degree forces an equal-tail pair

The source's output register belongs to $`V_r(M)`$. Every $`S_M`$ irrep occurring there has first row at least $`M-r`$, again by the injection-module decomposition.

Suppose a joint component of $`|\Phi_f^{(r)}\rangle`$ has its domain part in $`\mathscr H_r(N)`$. Its domain diagram is therefore

```math
\lambda=(N-r,\nu),
\qquad \nu\vdash r.
```

Only pairs admissible in $`\mathbb C[\mathcal F]`$ can occur in the source family. Thus the output diagram $`\eta`$ contains $`\lambda`$, and its tail contains $`\nu`$, with at least $`r`$ boxes. On the other hand, $`\eta_1\ge M-r`$ bounds that tail by $`r`$ boxes. Both conditions can hold only when

```math
\eta=(M-r,\nu).
```

Consequently every such top-degree component is a minimal pair of level $`r`$.

### Physical probabilities and normalized Gram weights

Define the linear map

```math
T_r:\mathbb C[\mathcal F]
\longrightarrow V_r(N)\otimes V_r(M),
\qquad
T_r|f\rangle=|\Phi_f^{(r)}\rangle.
```

It is an intertwiner: domain permutations act on the physical index tuple, and range permutations act on the physical image tuple. Explicitly,

```math
|\Phi_{\tau f\sigma^{-1}}^{(r)}\rangle
=(P_\sigma^X\otimes P_\tau^Y)
|\Phi_f^{(r)}\rangle.
```

Let $`E`$ be an isotypic projector on the function-label space, and let $`P`$ be the projector onto the matching joint isotypic component of the physical space, including all physical multiplicities. Intertwining gives $`PT_r=T_rE`$. Since $`T_r^\dagger T_r=J_r`$,

```math
\operatorname{Tr}\!\left(E\frac{J_r}{L}\right)
=
\operatorname{Tr}\!\left(P\frac{T_rT_r^\dagger}{L}\right).
```

The right side is the average physical probability of the corresponding component. Thus the reduced-domain dimension bound transfers to the normalized Gram weight exactly, including any multiplicities in the physical representation.

Since the top-degree part lies in $`\Pi_r`$,

```math
\operatorname{Tr}\!\left(\Pi_r\frac{J_r}{L}\right)
\ge1-\frac{r}{N-r+1}.
```

## 4. Average over the occupancy weights

For $`r\le k`$, the projector $`\Pi_k`$ includes $`\Pi_r`$. Positivity, the convex Gram identity, and monotonicity of $`r/(N-r+1)`$ give

```math
\begin{aligned}
\operatorname{Tr}\!\left(\Pi_k\frac{G_k}{L}\right)
&=\sum_{r=1}^k
w_r\operatorname{Tr}\!\left(\Pi_k\frac{J_r}{L}\right)\\
&\ge\sum_{r=1}^k
w_r\left(1-\frac{r}{N-r+1}\right)\\
&\ge1-\frac{k}{N-k+1}.
\end{aligned}
```

This proves the source-weight lemma. The estimate is uniform in $`M\ge N`$ and allows $`k`$ to grow linearly with $`N`$ within its stated range. The [copy lower bound](copy_lower_bound.md) combines it with the [output harmonic estimate](output_harmonics.md) and an approximation argument for arbitrary quantum processors.

