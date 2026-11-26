# Calibration and pulse errors

## Calibration model

Relabel the rails so that $`a=(\Gamma_0-\Gamma_1)/4\gt 0`$ at the nominal operating point. Write the surviving code-space operator as $`A=\sqrt b\,X`$ up to a scalar phase, where $`b=\exp[-(\Gamma_0+\Gamma_1)T/2]`$ and $`\det X=1`$. Let $`r\ge0`$ satisfy
```math
\lambda_\pm(A^\dagger A)=b\,e^{\pm r}.
```
Then $`r`$ measures state dependence of survival. If the propagator is calibrated, an ideal terminal filter produces an exact erasure channel with survival $`b e^{-r}`$. Alternatively a known polar unitary correction preserves all surviving trials and leaves the normalized filter $`\sqrt{X^\dagger X}`$. Pulse calibration can also change the logical rotation. The channel bound below includes that change.

For a constant resonant-drive amplitude $`c`$, a static detuning $`\delta`$ and a differential rate $`a`$, the trace-free code generator and its exponential are
```math
K=-a Z-i(c X_{\mathrm P}+\delta Z),\qquad
\Omega^2=c^2-a^2+\delta^2-2ia\delta,\qquad
X(T)=C I+S K,
\quad C=\cos(\Omega T),\quad S=\frac{\sin(\Omega T)}{\Omega}.
```
Here $`X_{\mathrm P}`$ is the Pauli matrix, distinct from the propagator $`X(T)`$. Both functions of $`\Omega`$ are even and $`S=T`$ at $`\Omega=0`$. These formulas therefore cover the exceptional point as well as complex $`\Omega`$. Putting $`z=C^*S`$ and writing $`X^\dagger X=q_0I+\boldsymbol q\cdot\boldsymbol\sigma`$ gives
```math
\boldsymbol q=(2c\,\mathrm{Im}z,\ -2ac|S|^2,\ -2a\,\mathrm{Re}z+2\delta\,\mathrm{Im}z),
\qquad r=\mathrm{arsinh}|\boldsymbol q|.
```
The vector follows from the Hermitian part of $`zK`$ and the Pauli product in $`K^\dagger K`$. The determinant relation $`q_0^2-|\boldsymbol q|^2=1`$ gives the formula for $`r`$. A drift in the common loss rate changes $`b`$ without changing $`r`$.

## Near the exact return

Let the nominal setting be $`c\gt a`$, $`\omega=\sqrt{c^2-a^2}`$ and $`T_0=\pi/\omega`$. The actual parameters are $`c+\Delta c`$, $`a+\Delta a`$, $`\delta`$ and $`T_0+\Delta T`$. To first order define
```math
\epsilon=\Delta T+\frac{T_0}{\omega^2}(c\,\Delta c-a\,\Delta a-i a\delta).
```
Then the two leading contributions to loss imbalance are
```math
r=2\sqrt{a^2(\mathrm{Re}\epsilon)^2+c^2(\mathrm{Im}\epsilon)^2}+O(\eta^2),
\qquad
\eta=\max\left\{\frac{|\Delta a|}{\omega},\frac{|\Delta c|}{\omega},
\frac{|\delta|}{\omega},\omega|\Delta T|\right\}.
```
The error term is local at fixed nominal parameters. In fact $`C=-1+O(\eta^2)`$ and $`S=-\epsilon`$ to first order, since the sine is expanded at $`\pi`$. Thus $`X\simeq-I-\epsilon K_0`$, and the Hermitian first-order part of $`X^\dagger X`$ has Pauli components $`(2c\mathrm{Im}\epsilon,0,-2a\mathrm{Re}\epsilon)`$. The anti-Hermitian part also contributes to coherent gate error. In particular, a small fractional drive error at $`c\gg a`$ changes the logical Pauli rotation angle by approximately $`2\pi\Delta c/c`$.

With timing error alone, the exact imbalance is
```math
r=2\,\mathrm{arsinh}\!\left(\frac{a|\sin(\omega\Delta T)|}{\omega}\right)
\le 2a|\Delta T|.
```
At fixed $`a\gt 0`$, the nominal return time grows as $`\pi/\sqrt{2a(c-a)}`$ as $`c`$ approaches $`a`$ from above. The logarithm of ideal survival is $`-(\Gamma_0+\Gamma_1)T_0/2`$. The coefficient $`T_0/\omega^2=\pi/\omega^3`$ in $`\epsilon`$ shows that weaker headroom also increases susceptibility to drive, differential-loss and detuning errors. The exact constant-pulse expression remains valid when the linear expansion ceases to be accurate.

## Arbitrary pulse errors

For the same terminal time $`T`$, let $`X_0(t)`$ be a calibrated nominal trajectory with anisotropy $`r_0(t)=2\log\|X_0(t)\|`$. Let the actual normalized generator differ by $`-\Delta a(t) Z-i\Delta H(t)`$, with $`\Delta H(t)`$ Hermitian. For integrable perturbations the actual terminal imbalance obeys
```math
r(T)\le r_0(T)
 +2\int_0^T\left[\cosh r_0(t)\,|\Delta a(t)|
 +\sinh r_0(t)\,\|\Delta H(t)\|\right]dt.
```
A scalar part of $`\Delta H`$ can be removed. This bound covers deterministic envelope, phase and detuning deviations, including finite ramps relative to a square reference pulse. It includes extra elapsed time by extending the reference trajectory to the same stop time.

For the proof, put $`Y=X_0^{-1}X`$. Its generator is $`B=X_0^{-1}(-\Delta a Z-i\Delta H)X_0`$. The inequality $`(\|Yv\|^2)'\le 2\|\mathrm{Herm}B\|\,\|Yv\|^2`$ holds almost everywhere. Thus $`\log\|Y(T)\|\le\int_0^T\|\mathrm{Herm}B\|dt`$ and $`\|X\|\le\|X_0\|\|Y\|`$. In the eigenbasis of the positive polar factor of $`X_0`$, its eigenvalues are $`e^{\pm r_0/2}`$. Hermitian symmetrization of the similarity scales the off-diagonal entries of a Hermitian perturbation by $`\cosh r_0`$ and leaves the diagonal unchanged. For an anti-Hermitian perturbation, it removes the diagonal and scales the magnitude of the off-diagonal entries by $`\sinh r_0`$. These give the stated operator-norm bounds. For a nominal exact return $`r_0(T)=0`$, the integral controls the entire survival mismatch. The coherent contribution vanishes for an equal-loss nominal trajectory because $`X_0`$ is then unitary.

The channel distance can also include uncompensated rotation and changes to the common loss rate. Let $`\mathcal E_A`$ and $`\mathcal E_{A_0}`$ be the two vacuum-flag channels for the actual and nominal physical propagators. Their half diamond distance satisfies
```math
\frac12\|\mathcal E_A-\mathcal E_{A_0}\|_\diamond
\le (\|A\|+\|A_0\|)\|A-A_0\|.
```
For each joint input with a reference, the vacuum-block difference is the negative partial trace of the surviving-block difference. The triangle inequality bounds the latter by the right-hand side, and partial trace is contractive on Hermitian differences. If $`G(t)=-\mathrm{diag}(\Gamma_0(t),\Gamma_1(t))/2-iH(t)`$ and $`G_0`$ denotes the nominal generator, Duhamel's identity gives $`\|A-A_0\|\le\int_0^T\|G(t)-G_0(t)\|dt`$ because both physical propagators are contractions on every subinterval. A known global phase can be removed before comparison. This second bound covers reference-preserving channel error even when a corrective polar rotation is unavailable.

## Hardware scale

Hajr et al. report single-photon decay times of $`27.0\,\mu\mathrm s`$ and $`31.0\,\mu\mathrm s`$ in the two Kerr oscillator rails (Table S1). In the same experiment they discuss a beam-splitter strength of approximately $`c/2\pi=2`$ MHz, using the convention $`H=c X_{\mathrm P}`$ on resonance. These inputs give $`a/2\pi\simeq190.15`$ Hz, $`c/a\simeq 1.05\times10^4`$, $`T_0\simeq250`$ ns, and $`b(T_0)\simeq0.991376`$. With the drive turned off for the same duration, the worse rail survives with probability about $`0.990783`$. These are loss-only model projections based on the reported parameters. The experiment also reports dephasing, heating and readout effects. [Hajr et al., Fig. 4 and Table S1](https://arxiv.org/html/2610.10432v1)

At those parameters the exact constant-pulse formula gives the following illustrative deviations, applied individually. The survival penalty column is the additional rejection $`b(1-e^{-r})`$ if a calibrated terminal filter is used. The overrun changes $`b`$ through the additional elapsed time, independently of the penalty shown.

| Deviation | Imbalance $`r`$ | Additional rejection |
| --- | ---: | ---: |
| 1 ns longer pulse | $`2.39\times10^{-6}`$ | $`2.37\times10^{-6}`$ |
| 1% weaker drive | $`6.03\times10^{-6}`$ | $`5.98\times10^{-6}`$ |
| Static detuning $`\delta/2\pi=10`$ kHz | $`2.99\times10^{-6}`$ | $`2.96\times10^{-6}`$ |
