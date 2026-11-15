# Finite verification

For actual GitHub mathematical rendering, the separate `Hosted mathematics` pull-request job compares every Markdown expression at wide and narrow viewports and retains its report and screenshots for inspection. It runs only on same-repository pull requests with `contents: read`, without persisted checkout credentials or secret inputs. It first probes the README, then captures the complete pinned Markdown inventory. This checks presentation; it does not establish the theorem or replace visual review. Artifact retention is fourteen days; it is not permanent preservation.

Run from the repository root with Python3.10 or later:

```bash
python3 verification/run_all.py
```

This regenerates `results.json` deterministically. To compare a fresh run with the saved output without changing it:

```bash
python3 verification/run_all.py --check
```

There are no third-party dependencies. Integer and rational calculations use the Python standard library. The reported modular ranks are explicitly over finite fields.

## What is checked

| Check | Failure it can expose | Finite scope |
|---|---|---|
| Known index projection | Confusing source-index dimensionN with range dimensionM; assuming every known index projection produces the desired target | All injections for(N,M)=(2,3),(3,5),(4,6); a nonuniform index-vector negative control |
| Repeated attempts and fallback | Confusing success-conditioned fidelity with unconditional output error | Exact failure probability and squared half-trace distance for the same injections |
| Zero-copy average target | Omitting the nonzero off-diagonal part of the average target, or using its diagonal entry as its largest eigenvalue | Direct target-matrix averages for(2,3),(3,5) |
| Matching-union path count | Confusing the image-overlap stratum with the number of agreement coordinates or alternating cycles | Explicit multigraph components for the426 enumerated injections |
| Occupancy Gram identity | Missing Stirling/falling-factorial coefficients or normalization | N=2..12,k=1..floor(N/2), every integer agreement countA=0..N |
| Deletion operators and central transpositions | Wrong signs, shifts, coordinate actions or deleted-coordinate fibers inQ | The seven ordered-tuple modules listed below, constructed explicitly |
| Pieri/content spectrum | Wrong horizontal-strip convention, multiplicities, content eigenvalues or kernel label | Full exact characteristic polynomials for tuple dimensions at most30; exact first three trace moments and two modular ranks for larger modules |
| Hypergeometric tail | Confusing image overlap with an independent-binomial model, or reversing a factorial-moment bound | Exhaustive toy parametersN=1..6,M=N..24; exact rational cases atN=64,128,256,M=N⁴ |
| Uniform cutoff arithmetic | Losing anN- orM-dependent factor when extending the harmonic cutoff | N=64,96,128,256,1024; M=N⁴,N⁴+1,2N⁴; every integer tail cutoffell≤N/32 |
| Hook ratios | Wrong first-row correction, transposed tail or first-row-to-tail move factor | Direct full-hook toy checks and independently cancelled hook ratios for representative tails up to255 boxes atN=64,128,256 |
| Constant-error contradiction | Confusing target-overlap fidelity with trace distance, or comparing squared and unsquared errors | Exact rational mass gaps atN=64,65,96,128,256,1024,4096 against the squared allowance5/9 |

The ordered-tuple cases are(N,r)=(4,1),(4,2),(5,2),(6,2),(6,3),(7,3),(8,3), with dimensions4,12,20,30,120,210,336. The scripts reconstruct the tuple operators rather than loading the predicted matrices. For dimensions above30, modular kernel dimensions agree with the predicted integer-spectrum kernel, but are not presented as a separate general rational-rank proof.

The large-range hook checks never construct a partition withN⁴ individual first-row boxes. They cancel that row analytically and multiply the remaining finite hook factors. Small diagrams independently compare this cancellation with the ordinary full hook product. Only representative large tails are tested; the script does not enumerate every partition of255.

## Conventions and limits

Fidelity in these checks is the target overlap `<s|rho|s>`. Trace distance is one half of the trace norm. The upper protocol has exact conditional output, whereas its unconditional error includes all failed attempts and the fallback state.

The tests do not construct a large injection Gram, optimize all CPTP processors, establish the spherical-function identities, or prove the asymptotic copy lower bound. The analytical science account supplies those arguments and their credited representation-theoretic dependencies. Passing finite checks is also not a priority or publication certificate.
