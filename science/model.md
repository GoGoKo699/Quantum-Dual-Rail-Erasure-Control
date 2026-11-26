# Dual-rail loss and the erasure channel

A dual-rail qubit stores one excitation in two modes. Vacuum identifies a loss event. If one mode decays faster, the chance that the excitation survives depends on the logical input. Even a surviving qubit can then be distorted. The control task is to minimize this effect while loss continues and to retain an exact erasure channel whenever the control budget permits it.

## Physical model

Use units with $`\hbar=1`$. The code space is spanned by $`|0_L\rangle=|10\rangle`$ and $`|1_L\rangle=|01\rangle`$. The vacuum $`|e\rangle=|00\rangle`$ is orthogonal to the code. The jump operators are

```math
L_j=\sqrt{\Gamma_j}\,|e\rangle\langle j_L|,\qquad j=0,1.
```

The calibrated nonnegative rates $`\Gamma_j`$ are constant. The baths are inaccessible and begin in vacuum. The input is an arbitrary logical qubit, possibly entangled with an inert reference. A deterministic number-preserving Hamiltonian may act on the rails for the full interval $`[0,T]`$. Its entries are integrable, and its off-diagonal magnitude obeys $`|H_{01}(t)|\le g`$ almost everywhere. The detuning can vary independently. The vacuum is absorbing. The hardware provides two rails, the bounded coupling, and a terminal vacuum flag. The coherent protocol uses neither an extra mode nor an intermediate readout.

## The full channel

The surviving block is described by a single contraction $`A(T)`$:

```math
\dot A=\left(-\tfrac12\mathrm{diag}(\Gamma_0,\Gamma_1)-iH(t)\right)A,
\qquad A(0)=I.
```

Here $`H`$ is restricted to the one-excitation sector. With $`\rho`$ an input density operator, the channel is

```math
\mathcal E_A(\rho)=A\rho A^\dagger\;\oplus\;
\mathrm{Tr}[(I-A^\dagger A)\rho]\,|e\rangle\langle e|.
```

The formula follows by integrating the flux into vacuum and using trace preservation. With a reference, replace the scalar trace by the partial trace over the logical input, or equivalently extend this linear map by the identity on the reference. Thus the flag can be correlated with the reference whenever $`A^\dagger A`$ has unequal eigenvalues.

An exact erasure channel with survival $`p`$ and known surviving unitary $`V`$ has $`A=\sqrt p\,V`$. Its surviving block transports the whole logical state and its reference correlations up to $`V`$. The vacuum block is $`(1-p)|e\rangle\langle e|\otimes\rho_R`$. For coherent control alone this is equivalent to $`A^\dagger A=pI`$.

## The determinant budget

Label the faster rail first, and set

```math
a=\frac{\Gamma_0-\Gamma_1}{4},\qquad
b(T)=\exp\!\left[-\frac{\Gamma_0+\Gamma_1}{2}T\right].
```

Liouville's determinant formula gives $`\det(A^\dagger A)=b(T)^2`$ for every waveform. The two survival eigenvalues therefore have the same geometric mean $`b(T)`$ at fixed duration. If they are equal, both are $`b(T)`$. Maximizing the smaller eigenvalue also minimizes their ratio. With equal rail rates, the drift is a scalar loss times a unitary for every waveform and the optimum is immediate.

The [frontier](frontier.md) gives the pulse and proves its optimality. The optional terminal filter in that result is a separate physical resource whose rejected events count as erasures.
