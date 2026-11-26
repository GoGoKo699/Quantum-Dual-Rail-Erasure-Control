# Numerical verification

From the repository root, run the checks with Python 3 and the NumPy and SciPy packages installed.

```bash
python verification/run_all.py
```

The script runs offline. It uses seeded input waveforms and exits with an error when a comparison exceeds the numerical tolerance. The printed residuals can vary within floating-point rounding across platforms.

| Check | Calculation | Scientific statement |
| --- | --- | --- |
| Finite-time frontier | Direct matrix exponentials and singular values at 100 parameter points, against the formula and 2,400 seeded eight-segment waveforms with varying amplitudes, phases and detunings | [Optimal survival](../science/frontier.md) |
| Loss and the reference | Full Lindblad evolution of the two rails, vacuum and an inert three-dimensional reference for a detuned sequence and a balanced pulse | [The flagged channel](../science/model.md) |
| Ideal terminal filter | Construct the filter by singular-value decomposition, verify contractivity and both output blocks, then test a larger success weight | [The loss–survival frontier](../science/frontier.md) |

The parameter points include equal and unequal rail losses, both rail orderings, zero coupling, couplings on either side of the threshold and deadlines before, at and after first return. With NumPy 2.3.5 and SciPy 1.17.0, the largest difference between the pulse and the formula was $`3.61\times10^{-16}`$, and the smallest advantage over sampled controls was $`-8.88\times10^{-16}`$, within the $`2\times10^{-12}`$ tolerance.

The [analytic proof](../science/frontier.md) handles the full set of admissible waveforms. These finite comparisons check the channel normalization, control formula, filter construction and boundary cases.
