# Project understanding map

The 30 milestones follow two phases. The first 12 build the model from an
excitation and its loss flag up to the complete operational task. The next
18 develop the resonant pulse, its optimality against shaped controls, the
terminal filtering benchmark, and the calibration and literature context.
The second phase has more room because the construction and the universal
comparison use different ideas before they yield one channel guarantee.

The [Watrous bridge](WATROUS_BRIDGE.md) identifies the relevant sections of
the single educational anchor. The linked scientific pages give the precise
claims and proofs.

| Milestones | Connection |
| --- | --- |
| [M01](#m01-the-excitation-and-the-two-rails)–[M08](#m08-channel-distance-and-exact-success) | The input, its reference, and the complete flagged channel |
| [M09](#m09-the-bounded-exchange-control)–[M12](#m12-the-operational-comparison) | Loss, coherent control, and the charged resources |
| [M13](#m13-the-determinant-budget)–[M17](#m17-the-survival-spectrum-before-the-return) | The invariant survival budget and the resonant pulse |
| [M18](#m18-a-distance-for-log-anisotropy)–[M24](#m24-a-direct-speed-limit-check) | Geometry and the comparison with all allowed waveforms |
| [M25](#m25-constructing-the-terminal-filter)–[M26](#m26-why-the-terminal-filter-is-optimal) | The optimal terminal correction with explicit rejection |
| [M27](#m27-calibration-error-and-the-loss-flag)–[M30](#m30-the-complete-control-problem) | Calibration, attribution, and the full operational result |

## Phase I — Background and preliminaries

### M01 The excitation and the two rails

**Central question.** Where is the qubit stored?

**Understanding target.** Use the two occupations with total excitation one as the logical basis. Identify vacuum as a third, orthogonal physical state.

**Prerequisites.** None within this map.

**Conceptual connection.** Relate a single rail-label qubit to the two modes and explain why a vacuum check can preserve the relative phase of a surviving code state.

**Canonical sources.** [Physical model](../science/model.md#physical-model) · [Watrous bridge](WATROUS_BRIDGE.md)

### M02 An unknown input and its reference

**Central question.** What must the memory preserve for an arbitrary user?

**Understanding target.** Represent a mixed or pure logical state jointly with an inaccessible reference. Take the code partial trace to obtain the reference marginal.

**Prerequisites.** [M01](#m01-the-excitation-and-the-two-rails).

**Conceptual connection.** A memory preserves coherence with systems outside the device, so survival on the two basis inputs alone does not define the output channel.

**Canonical sources.** [Physical model](../science/model.md#physical-model) · [Watrous bridge](WATROUS_BRIDGE.md)

### M03 Loss to a vacuum bath

**Central question.** How do the two rail lifetimes enter the dynamics?

**Understanding target.** Relate each occupation decay rate Γj to amplitude decay Γj/2. Track the jump from either code basis state to the same vacuum.

**Prerequisites.** [M01](#m01-the-excitation-and-the-two-rails).

**Conceptual connection.** The loss flag can be read at the end because excitation number is conserved by the drive and vacuum is absorbing under the model.

**Canonical sources.** [Physical model](../science/model.md#physical-model)

### M04 The survivor propagator

**Central question.** How does continuous loss act when the excitation is still present?

**Understanding target.** Follow the two-dimensional differential equation for the code propagator A, with Hermitian coherent control and negative diagonal amplitude drift.

**Prerequisites.** [M02](#m02-an-unknown-input-and-its-reference), [M03](#m03-loss-to-a-vacuum-bath).

**Conceptual connection.** A time-varying drive acts simultaneously with attenuation. The contraction AρA† represents the unnormalized surviving state.

**Canonical sources.** [Physical model](../science/model.md#physical-model)

### M05 The retained vacuum flag

**Central question.** Which map describes a run before its outcome is known?

**Understanding target.** Construct the completely positive flagged channel from the survivor map and the complementary loss effect. Interpret the loss branch as a weighted reference marginal.

**Prerequisites.** [M02](#m02-an-unknown-input-and-its-reference), [M04](#m04-the-survivor-propagator).

**Conceptual connection.** Adding two orthogonal outputs restores trace preservation without throwing away loss events or an arbitrary reference.

**Canonical sources.** [Physical model](../science/model.md#the-full-channel) · [Watrous bridge](WATROUS_BRIDGE.md)

### M06 The weakest surviving input

**Central question.** How can the most attenuated input be found?

**Understanding target.** Use the eigenvalues of A†A to identify the extrema of survival over normalized inputs. Distinguish singular values as amplitudes from their squares as probabilities.

**Prerequisites.** [M04](#m04-the-survivor-propagator), [M05](#m05-the-retained-vacuum-flag).

**Conceptual connection.** The right singular vector with the smaller singular value gives an operational witness for the memory's survival guarantee.

**Canonical sources.** [Physical model](../science/model.md#the-full-channel) · [Watrous bridge](WATROUS_BRIDGE.md)

### M07 State-independent erasure

**Central question.** When is a surviving logical transformation correct up to a known unitary?

**Understanding target.** Show that survival is input independent exactly when A†A is a scalar identity. Use polar decomposition to identify the surviving unitary at positive survival.

**Prerequisites.** [M05](#m05-the-retained-vacuum-flag), [M06](#m06-the-weakest-surviving-input).

**Conceptual connection.** The same scalar gives the vacuum probability for all inputs and makes the reference marginal independent of the loss event after normalization.

**Canonical sources.** [Physical model](../science/model.md#the-full-channel) · [Watrous bridge](WATROUS_BRIDGE.md)

### M08 Channel distance and exact success

**Central question.** How can one compare complete channels or recognize exact coherently preserved success?

**Understanding target.** Use the diamond distance to compare channels jointly with a reference. Interpret a rank-one Choi operator for a success branch proportional to a unitary channel.

**Prerequisites.** [M02](#m02-an-unknown-input-and-its-reference), [M05](#m05-the-retained-vacuum-flag), [M07](#m07-state-independent-erasure).

**Conceptual connection.** The channel metric can register both flag errors and changes to surviving coherence. Rank one restricts all accepted Kraus operators to the desired transformation.

**Canonical sources.** [Watrous bridge](WATROUS_BRIDGE.md)

### M09 The bounded exchange control

**Central question.** Which part of a general two-rail drive is charged?

**Understanding target.** Separate a scalar energy, diagonal detuning and complex off-diagonal exchange. Apply the pointwise magnitude bound to the off-diagonal element throughout the interval.

**Prerequisites.** [M03](#m03-loss-to-a-vacuum-bath), [M04](#m04-the-survivor-propagator).

**Conceptual connection.** A rapidly varying phase or detuning is an admissible competitor, and the model charges the time spent performing any exchange.

**Canonical sources.** [Physical model](../science/model.md)

### M10 Common and differential attenuation

**Central question.** Which combination of the rates affects rail imbalance?

**Understanding target.** Factor out common decay and define a as one quarter of the absolute rate difference. Read the remaining drift as a signed Pauli Z after rail relabeling.

**Prerequisites.** [M03](#m03-loss-to-a-vacuum-bath), [M04](#m04-the-survivor-propagator), [M09](#m09-the-bounded-exchange-control).

**Conceptual connection.** Common loss scales both singular values together. Differential loss changes their ratio and competes with the transverse drive.

**Canonical sources.** [Physical model](../science/model.md#the-determinant-budget) · [Finite-time analysis](../science/frontier.md)

### M11 The resonant generator

**Central question.** How does a constant resonant drive become analytically tractable?

**Understanding target.** Square the normalized generator −aZ−icX using Pauli anticommutation. Relate the sign of a²−c² to the real or imaginary pair of eigenvalues.

**Prerequisites.** [M09](#m09-the-bounded-exchange-control), [M10](#m10-common-and-differential-attenuation).

**Conceptual connection.** The same matrix formula covers hyperbolic growth, the degenerate linear case, and oscillatory exchange. The square avoids relying on normal eigenvectors.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M12 The operational comparison

**Central question.** What is optimized at each prescribed deadline?

**Understanding target.** Combine the fixed rates, unknown input, retained vacuum and exchange bound. Distinguish least-input survival, exact state-independent erasure, and the separately allowed terminal filtering benchmark.

**Prerequisites.** [M06](#m06-the-weakest-surviving-input), [M07](#m07-state-independent-erasure), [M08](#m08-channel-distance-and-exact-success), [M09](#m09-the-bounded-exchange-control), [M10](#m10-common-and-differential-attenuation), [M11](#m11-the-resonant-generator).

**Conceptual connection.** A fair comparison counts permanent loss during every admissible waveform. It asks for a channel on a qubit, rather than the evolution of one chosen state.

**Canonical sources.** [Physical model](../science/model.md) · [Finite-time analysis](../science/frontier.md)

## Phase II — Narrative and innovation

### M13 The determinant budget

**Central question.** What information about the loss is independent of the pulse?

**Understanding target.** Apply the determinant evolution law to the two-dimensional propagator. Identify the geometric mean b of the two survival eigenvalues and the condition for attaining b as worst-input survival.

**Prerequisites.** [M06](#m06-the-weakest-surviving-input), [M10](#m10-common-and-differential-attenuation), [M12](#m12-the-operational-comparison).

**Conceptual connection.** The control redistributes attenuation between input directions while the product of their survivals remains fixed.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M14 Below and at the critical coupling

**Central question.** What can a resonant pulse do at c≤a?

**Understanding target.** Use the positive hyperbolic sine, or its linear limit at c=a, to identify nonzero survival anisotropy at every positive time for this constant drive.

**Prerequisites.** [M11](#m11-the-resonant-generator), [M13](#m13-the-determinant-budget).

**Conceptual connection.** The resonant calculation identifies a candidate boundary. The arbitrary-waveform result will require a comparison covering shaped controls.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M15 The first oscillatory return

**Central question.** Why does strong enough coupling return all input states together?

**Understanding target.** For c>a, find the first positive zero of the sine multiplying the normalized generator. Recover the scalar operator −I at that time and the survival b of the physical channel.

**Prerequisites.** [M07](#m07-state-independent-erasure), [M11](#m11-the-resonant-generator), [M13](#m13-the-determinant-budget).

**Conceptual connection.** A full matrix return guarantees exact preservation up to a common phase for every input. Returning one vector's occupation would establish a weaker fact.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee) · [Related work](../references/RELATED_WORK.md)

### M16 Selecting a pulse by deadline

**Central question.** How does one synthesize an exact channel at a prescribed later time?

**Understanding target.** Solve for c from the desired first return at T. Compare c with the allowed maximum and recover the shortest deadline supplied by a constant pulse.

**Prerequisites.** [M09](#m09-the-bounded-exchange-control), [M13](#m13-the-determinant-budget), [M15](#m15-the-first-oscillatory-return).

**Conceptual connection.** At shorter deadlines the maximal admissible resonant pulse is the candidate for best survival. At longer exact deadlines a smaller calibrated coupling can use the complete storage interval.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M17 The survival spectrum before the return

**Central question.** How does the finite-time formula arise?

**Understanding target.** Compute the normalized trace of the positive matrix for the constant drive and use determinant one to determine both eigenvalues. Interpret the smaller physical eigenvalue as the guarantee.

**Prerequisites.** [M06](#m06-the-weakest-surviving-input), [M11](#m11-the-resonant-generator), [M13](#m13-the-determinant-budget), [M14](#m14-below-and-at-the-critical-coupling), [M15](#m15-the-first-oscillatory-return).

**Conceptual connection.** One calculation gives the survival formula in oscillatory, critical and hyperbolic regimes and connects continuously to scalar loss at the return.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M18 A distance for log anisotropy

**Central question.** How can a spectral ratio become a distance?

**Understanding target.** Regard the normalized Gram matrix M as positive Hermitian with determinant one. Express its eigenvalues as eʳ and e⁻ʳ and the smaller survival probability as b e⁻ʳ.

**Prerequisites.** [M13](#m13-the-determinant-budget), [M17](#m17-the-survival-spectrum-before-the-return).

**Conceptual connection.** The endpoint distance r from the identity measures the residual anisotropy. Minimizing r is exactly the deterministic worst-input survival problem.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#proof-by-hyperbolic-comparison)

### M19 The hyperbolic state space

**Central question.** What geometry does the positive matrix trace out?

**Understanding target.** Expand M in the Pauli basis and use the determinant-one constraint to identify the upper unit hyperboloid. Connect its invariant metric to the log spectrum at the identity.

**Prerequisites.** [M10](#m10-common-and-differential-attenuation), [M18](#m18-a-distance-for-log-anisotropy).

**Conceptual connection.** The hyperboloid represents positive Gram matrices rather than logical Bloch states. Its geodesic chord length measures the final survival imbalance.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#proof-by-hyperbolic-comparison)

### M20 The path speed and curvature

**Central question.** How does peak coupling constrain the geometry?

**Understanding target.** Differentiate M using the normalized propagator. Relate its constant speed to a and its covariant acceleration to the commutator of the Hamiltonian with Z.

**Prerequisites.** [M09](#m09-the-bounded-exchange-control), [M10](#m10-common-and-differential-attenuation), [M19](#m19-the-hyperbolic-state-space).

**Conceptual connection.** Diagonal detuning drops out of that commutator, so arbitrary detuning cannot increase the maximal rate at which the path turns.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#proof-by-hyperbolic-comparison)

### M21 The comparison arc

**Central question.** What identifies the resonant path as the comparison curve?

**Understanding target.** Follow the constant-drive Gram matrix in a hyperbolic plane. Explain why its arc together with its geodesic chord bounds a convex region before a full return.

**Prerequisites.** [M15](#m15-the-first-oscillatory-return), [M17](#m17-the-survival-spectrum-before-the-return), [M19](#m19-the-hyperbolic-state-space), [M20](#m20-the-path-speed-and-curvature).

**Conceptual connection.** The chord-convexity condition enables comparison with general three-dimensional paths. A complete return is provided directly by the matrix exponential.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#proof-by-hyperbolic-comparison)

### M22 The all-waveform converse

**Central question.** How does a curvature bound rule out a better shaped pulse?

**Understanding target.** Apply the hyperbolic Schur comparison to paths of equal length, with the constant drive as chord-convex reference of maximal curvature. Interpret the inequality as an endpoint-distance lower bound.

**Prerequisites.** [M18](#m18-a-distance-for-log-anisotropy), [M20](#m20-the-path-speed-and-curvature), [M21](#m21-the-comparison-arc).

**Conceptual connection.** The comparison covers changing amplitude, phase and detuning. Smooth approximation extends the result to integrable controls preserving the pointwise exchange bound.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#proof-by-hyperbolic-comparison) · [Related work](../references/RELATED_WORK.md)

### M23 The finite-time optimum

**Central question.** What does the complete pulse rule guarantee?

**Understanding target.** Combine the universal comparison before a return with the determinant ceiling at and after the first feasible return. Explain why no exact unfiltered erasure occurs below the threshold at positive time.

**Prerequisites.** [M13](#m13-the-determinant-budget), [M14](#m14-below-and-at-the-critical-coupling), [M16](#m16-selecting-a-pulse-by-deadline), [M17](#m17-the-survival-spectrum-before-the-return), [M22](#m22-the-all-waveform-converse).

**Conceptual connection.** The same rule settles every finite deadline. The availability of a perfect logical survivor and its survival probability are distinct predictions.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#pulse-and-guarantee)

### M24 A direct speed-limit check

**Central question.** Can one check the threshold without the geometric comparison?

**Understanding target.** Track a Pauli-coordinate phase until the first population-imbalance sign change. Use the reversed, rail-conjugated path to bound the final segment by the same half-return time.

**Prerequisites.** [M10](#m10-common-and-differential-attenuation), [M15](#m15-the-first-oscillatory-return), [M20](#m20-the-path-speed-and-curvature), [M23](#m23-the-finite-time-optimum).

**Conceptual connection.** The two-lobe argument supplies a separate check of earliest exact return. The chord comparison supplies the full survival guarantee at earlier deadlines.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#an-elementary-check-of-the-exact-speed-limit)

### M25 Constructing the terminal filter

**Central question.** Can a lossy survivor be corrected with a declared extra failure?

**Understanding target.** Apply the contraction F=σmin(A)A⁻¹ to equalize the surviving amplitudes. Include failure in the same retained erasure flag and compute the reference-safe success map.

**Prerequisites.** [M06](#m06-the-weakest-surviving-input), [M07](#m07-state-independent-erasure), [M08](#m08-channel-distance-and-exact-success), [M17](#m17-the-survival-spectrum-before-the-return).

**Conceptual connection.** The operation attenuates the stronger singular mode and realizes exact success at any deadline at the cost of additional erasures.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#optional-terminal-filter) · [Watrous bridge](WATROUS_BRIDGE.md)

### M26 Why the terminal filter is optimal

**Central question.** Can several accepted measurement outcomes improve exact success?

**Understanding target.** Use the rank-one success Choi operator to make every accepted product F_jA proportional to the same unitary. Apply trace nonincrease to bound total success by the smaller survival eigenvalue.

**Prerequisites.** [M08](#m08-channel-distance-and-exact-success), [M23](#m23-the-finite-time-optimum), [M25](#m25-constructing-the-terminal-filter).

**Conceptual connection.** The optimum from bounded coherent evolution also optimizes the final exact-erasure success probability under the separate ideal filtering resource.

**Canonical sources.** [Finite-time analysis](../science/frontier.md#optional-terminal-filter) · [Watrous bridge](WATROUS_BRIDGE.md)

### M27 Calibration error and the loss flag

**Central question.** Which imperfections change the state-independent output guarantee?

**Understanding target.** Distinguish common loss error from mismatch in differential loss, coupling, timing or detuning. Relate perturbed propagators to changed flag probabilities and channel error.

**Prerequisites.** [M08](#m08-channel-distance-and-exact-success), [M10](#m10-common-and-differential-attenuation), [M16](#m16-selecting-a-pulse-by-deadline), [M23](#m23-the-finite-time-optimum).

**Conceptual connection.** A nominal revival calibrated for one pair of rates can miss scalar survival after a perturbation. The calibration analysis specifies guarantees for the physical parameters it models.

**Canonical sources.** [Robustness analysis](../science/robustness.md#near-the-exact-return)

### M28 Reading the experimental scale

**Central question.** How should an experimental lifetime and drive be compared with the theorem?

**Understanding target.** Put population decay and angular exchange in consistent inverse-time units. Compute a return time, survival and calibration margin for a specified pair of rates and peak drive.

**Prerequisites.** [M10](#m10-common-and-differential-attenuation), [M16](#m16-selecting-a-pulse-by-deadline), [M23](#m23-the-finite-time-optimum), [M27](#m27-calibration-error-and-the-loss-flag).

**Conceptual connection.** The dimensionless g/a locates the regime, while common attenuation sets absolute survival. A finite-time channel prediction and an experimentally measured spin-locking lifetime answer different questions.

**Canonical sources.** [Robustness analysis](../science/robustness.md#hardware-scale) · [Related work](../references/RELATED_WORK.md)

### M29 Attribution and evidence

**Central question.** Which results follow from prior constant-drive work and which require new optimization?

**Understanding target.** Credit the published unequal-loss generator, spectral threshold and compensation mechanisms. Identify the arbitrary-waveform comparison and exact deadline synthesis as the additional scientific steps.

**Prerequisites.** [M15](#m15-the-first-oscillatory-return), [M22](#m22-the-all-waveform-converse), [M23](#m23-the-finite-time-optimum), [M26](#m26-why-the-terminal-filter-is-optimal), [M28](#m28-reading-the-experimental-scale).

**Conceptual connection.** A constant-drive spectrum gives one achievable trajectory. The curvature argument and completed success benchmark answer what no competing admissible control can improve.

**Canonical sources.** [Finite-time analysis](../science/frontier.md) · [Related work](../references/RELATED_WORK.md)

### M30 The complete control problem

**Central question.** How do the physical, geometric and operational accounts fit together?

**Understanding target.** Follow a run from the input and rate calibration through waveform choice, end flag and optional filter. State the exact guarantees, bounded resources and perturbation scope for an arbitrary entangled input.

**Prerequisites.** [M12](#m12-the-operational-comparison), [M23](#m23-the-finite-time-optimum), [M26](#m26-why-the-terminal-filter-is-optimal), [M27](#m27-calibration-error-and-the-loss-flag), [M28](#m28-reading-the-experimental-scale), [M29](#m29-attribution-and-evidence).

**Conceptual connection.** Connect the invariant determinant and curvature bound to the optimal achievable erasure channel. Use the final scope to evaluate proposed changes such as a new noise source or a different control resource.

**Canonical sources.** [Physical model](../science/model.md) · [Finite-time analysis](../science/frontier.md) · [Robustness analysis](../science/robustness.md) · [Related work](../references/RELATED_WORK.md)
