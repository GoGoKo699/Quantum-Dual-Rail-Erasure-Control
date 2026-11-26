# Quantum Dual-Rail Erasure Control

**How quickly can a bounded coupling turn unequal rail loss into a state-independent erasure?** A single constant resonant pulse is optimal at every deadline. With sufficient coupling and time, the qubit either survives intact or reaches an orthogonal vacuum flag. Before that deadline, the same control law gives the best worst-case survival and, with a terminal filter, the best survival of an exact erasure channel.

Let $`\Gamma_0,\Gamma_1`$ be the two fixed excitation decay rates, $`a=|\Gamma_0-\Gamma_1|/4>0`$ their scaled difference, and $`g`$ the peak rail coupling. The earliest exact coherent pulse has length

```math
T_*=\frac{\pi}{\sqrt{g^2-a^2}},\qquad g>a.
```

| Deadline or coupling | Pulse and outcome |
| --- | --- |
| At or after $`T_*`$ | Set the pulse amplitude to $`\sqrt{a^2+\pi^2/T^2}`$. The exact survival probability is $`\exp[-(\Gamma_0+\Gamma_1)T/2]`$. |
| Before $`T_*`$, or $`g\le a`$ | Drive at the coupling cap. This maximizes the minimum survival over input states. An optional terminal filter realizes exact erasure at that survival probability. |

The optimality proof allows time-dependent amplitudes, phases, and detunings. Its comparison class uses two rails, loss active throughout, and deterministic number-preserving coherent control. Near the coupling threshold the earliest exact pulse can sacrifice most excitations. The [finite-time survival formula](science/frontier.md#pulse-and-guarantee) quantifies the option to finish earlier.

## Read and verify

- [Channel model](science/model.md) explains the vacuum flag, the surviving state, and why unequal rates cause backaction.
- [Optimal pulse and proof](science/frontier.md) derives the complete deadline–survival tradeoff and the terminal filter. The proof connects bounded drive to bounded curvature in hyperbolic space.
- [Calibration and hardware scale](science/robustness.md) quantifies timing, coupling and detuning errors, and distinguishes survival imbalance from a logical rotation of the survivor.
- [Related work](references/RELATED_WORK.md) traces the continuous-drive spectrum, experimental echoes, and mathematical tools.
- [Learning route](learning/README.md) connects Watrous's channel formalism to the project through [30 milestones](learning/MILESTONES.md).
- [Verification guide](verification/README.md) gives commands for analytic-limit, randomized waveform, and full-channel reference checks. Run `python verification/run_all.py` from the repository root after installing NumPy and SciPy.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
