# From Watrous to loss-balanced dual-rail control

A pair of rails stores one excitation. An ideal loss detector can distinguish
vacuum from the one-excitation code without distinguishing the two rails.
That is enough to say whether the qubit survived. To say whether the qubit
survived *unchanged*, one must also know how unequal attenuation acts on
the state inside the code.

The educational anchor is **John Watrous, *The Theory of Quantum
Information***, Cambridge University Press, 2018. The readings below use
the author's 2018 manuscript from the
[author's book page](https://jhwatrous.github.io/books-and-courses.html).
The [30-milestone map](MILESTONES.md) develops the project in order.

## Targeted reading

| Reading from the single anchor | Use in this project |
| --- | --- |
| [§1.1, Linear algebra](https://jhwatrous.github.io/TQI.1.pdf) | Use a direct sum for the mutually exclusive survivor and vacuum outputs. Read singular values from the positive matrix `A†A`. |
| [§2.1, Registers and states](https://jhwatrous.github.io/TQI.2.pdf) | Describe an arbitrary logical input jointly with a reference and take a partial trace when the logical register is erased. |
| [§2.2.1–2.2.2, Quantum channels and their representations](https://jhwatrous.github.io/TQI.2.pdf) | Use the Kraus sum and the Choi representation to treat all outcomes as one linear channel. A rank-one success Choi matrix forces all successful Kraus operators to be proportional. |
| [§2.3.1–2.3.2, Measurements](https://jhwatrous.github.io/TQI.2.pdf) | Recover the probability of a flag from its effect and retain the conditional quantum output on success. |
| [§3.3, Channel distances and discrimination](https://jhwatrous.github.io/TQI.3.pdf) | Compare perturbed and ideal channels on inputs that can share entanglement with a reference. Flag probabilities already give a lower bound on their distinguishability. |

## Notation and the full output

Watrous writes `A*` for the adjoint `A†`. Let `C` be
the two-dimensional code, `R` an external reference, and `vac` the vacuum.
The survivor output and the vacuum occupy orthogonal parts of the same
output register. The system-reference output is therefore a direct sum
between the two flagged sectors. Tensor products describe the system and
reference in either sector.

The code-space propagator `A` has one Kraus operator on the
survival branch. For an input state `ρ` on the code, its unnormalized output
is `AρA†` and the survival probability is its trace. The vacuum branch has
effect `I − A†A`. For an input `ρ_CR` with a reference, the probability
and unnormalized reference state on vacuum are supplied by

```math
\mathrm{Tr}_{C}\bigl[((I-A^\dagger A)\otimes I_R)\rho_{CR}\bigr].
```

The branch formula has an equivalent completely positive expression with
the square root of the effect on both sides of the input. The partial trace
over the code makes the two expressions identical. Normalizing the survivor
state is appropriate after a particular flag is observed. Keeping both
unnormalized branches gives a linear channel before any flag is observed.

If $`A^\dagger A=pI`$, then $`A=\sqrt p\,U`$ for a unitary
$`U`$ at positive $`p`$. The input survives with probability
$`p`$ and the known $`U`$ preserves its correlations. The vacuum
branch leaves the unnormalized reference marginal
$`(1-p)\mathrm{Tr}_{C}\rho_{CR}`$. Conversely, input-independent
survival implies $`\langle\psi|A^\dagger A|\psi\rangle=p`$ for
every unit vector and therefore $`A^\dagger A=pI`$.

## A two-rail example

Suppose one idle rail has amplitude survival $`1/2`$ and the other is
lossless. With no mixing, $`A=\mathrm{diag}(1/2,1)`$.
The two basis inputs survive with probabilities $`1/4`$ and $`1`$.
An equal superposition survives with probability $`5/8`$ and
its conditional state has rail occupation probabilities $`1/5`$ and
$`4/5`$. Thus no detected loss still changes the state.

A terminal filter $`F=\mathrm{diag}(1,1/2)`$ restores equal
survival. The product $`FA=I/2`$ gives success probability $`1/4`$
on every input, and failure joins the vacuum flag. The filter cannot reach
the geometric-mean survival $`1/2`$ in this example; that would require
increasing the weaker amplitude. Coherent evolution throughout the same
loss interval can reach the geometric mean if the coupling bound permits
an exact return within the deadline.

## From channel description to pulse design

The [physical model](../science/model.md) derives `A` from
Markovian loss and bounds the instantaneous off-diagonal Hamiltonian
element. The determinant fixes the product of survival eigenvalues at each
deadline. The transverse drive changes their ratio, which controls both
worst-input survival and the amount of extra rejection required by a
terminal filter.

The [frontier proof](../science/frontier.md) uses normalized positive
matrices of determinant one to express the ratio as a hyperbolic
distance. The peak coupling bounds how sharply the path can turn. A
constant resonant pulse minimizes its endpoint distance up to the first
return. For a later exact deadline the same pulse family can be retuned to
return at that deadline. This is a statement about all allowed waveforms,
including control with time-dependent phase and detuning.

The [robustness analysis](../science/robustness.md) tracks how timing and
calibration affect that return. The [related-work
account](../references/RELATED_WORK.md) gives the sources for the physical
generator and the geometric comparison. The anchor supplies the channel
language used to express and test the result.
