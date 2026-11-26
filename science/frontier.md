# Optimal synthesis at a fixed deadline

Take the [dual-rail model](model.md) with unequal rates, $`a\gt 0`$. The quantity to optimize is the minimum survival over all logical inputs at a fixed deadline, $`\lambda_{\min}(A^\dagger A)`$. It measures the largest survival probability of an exact erasure channel obtainable with the optional terminal filter described below.

## Pulse and guarantee

For $`g\gt a`$ define $`\omega=\sqrt{g^2-a^2}`$ and $`T_*=\pi/\omega`$. At $`T\ge T_*`$, choose a constant resonant coupling $`c=\sqrt{a^2+\pi^2/T^2}\le g`$. Its normalized propagator is $`-I`$ at the deadline. The output channel is exact erasure with survival $`b(T)`$ and unchanged logical state when it survives.

At other positive deadlines choose $`c=g`$. The function $`s(T)`$ is

- $`\sin(\omega T)/\omega`$ when $`g\gt a`$ and $`T\lt T_*`$
- $`T`$ when $`g=a`$
- $`\sinh(\nu T)/\nu`$ when $`g\lt a`$, with $`\nu=\sqrt{a^2-g^2}`$

The same constant pulse maximizes the least-input survival over every admissible waveform. Its value is

```math
p_*(T)=\frac{b(T)}{\big(\sqrt{1+a^2s(T)^2}+a|s(T)|\big)^2}.
```

The strict inequality $`p_*(T)\lt b(T)`$ in these regimes excludes exact erasure from coherent control alone. In particular, there is no positive exact deadline at or below $`g=a`$. When $`g=0`$, the formula reduces to $`e^{-\Gamma_0 T}`$. The earliest exact pulse gives survival $`b(T_*)`$, which tends to zero as the coupling decreases to threshold at fixed unequal rates.

## Proof by hyperbolic comparison

Strip the scalar loss and the phase from the trace of $`H`$. The normalized propagator $`X`$ has determinant one and satisfies $`\dot X=(-aZ-iH_0)X`$, where $`H_0`$ is the traceless Hamiltonian. Write $`M=X^\dagger X`$. Positive determinant-one Hermitian matrices form hyperbolic three-space with metric

```math
\langle D,E\rangle_M=\tfrac12\mathrm{Tr}(M^{-1}D M^{-1}E).
```

Indeed, in Pauli coordinates $`M=q_0 I+q\cdot\sigma`$ the determinant is $`q_0^2-|q|^2=1`$, with $`q_0\gt 0`$. The metric above is the induced hyperboloid metric of curvature $`-1`$. The distance $`r`$ from $`I`$ satisfies $`\cosh r=\tfrac12\mathrm{Tr}M`$. The eigenvalues of $`A^\dagger A`$ are $`b(T)e^{\pm r}`$.

The curve speed is $`2a`$ because $`\dot M=-2aX^\dagger ZX`$ and congruence by $`X`$ is an isometry. Along the curve the covariant acceleration is

```math
\ddot M-\dot M M^{-1}\dot M=-2ai\,X^\dagger[H_0,Z]X.
```

The left side is the tangential projection of $`\ddot M`$ onto the determinant-one hyperboloid. The norm of the right side is $`4a|H_{01}|`$. Thus the length at time $`T`$ is fixed and the geodesic curvature is at most $`g/a`$. In this form the control problem is to find the shortest endpoint chord for that fixed length.

For $`H_0=g\sigma_x`$, put $`K=-aZ-ig\sigma_x`$. Its square is $`(a^2-g^2)I`$. Exponentiating gives $`X=C I+sK`$, where $`C=\cos(\omega T)`$ above threshold, $`C=1`$ at threshold, and $`C=\cosh(\nu T)`$ below. In Pauli coordinates of $`M`$, one obtains

```math
q_0=1+2a^2s^2,\qquad q_x=0,\qquad
q_y=-2ag s^2,\qquad q_z=-2aCs.
```

The reference curve has curvature $`g/a`$ and lies in the totally geodesic plane $`q_x=0`$. For $`g\gt 0`$, its first segment before return is simple. Above threshold this follows because the pair $`(s^2,Cs)`$ determines the phase modulo $`\pi`$. At and below threshold $`s^2`$ grows strictly with positive time. In Klein coordinates $`(y,z)=(q_y,q_z)/q_0`$, geodesics are straight lines and the curve lies on the boundary

```math
y+k-k\sqrt{1-y^2-z^2}=0,\qquad k=g/a.
```

The sublevel set is convex by strict convexity of the left side on the disk. The simple arc and its chord bound a convex cap. Thus the hypotheses of [Ghomi's generalized Schur theorem](../references/RELATED_WORK.md#hyperbolic-comparison) hold. After arclength reparametrization, that theorem gives a chord at least as long for any other admissible curve. This proves optimality at every pre-return deadline and at all finite deadlines at or below threshold. For integrable controls, smooth a bounded transverse component by convolution with a positive kernel and smooth the integrable detuning. The controls converge in $`L^1`$ with the original transverse bound, so their propagators converge uniformly on the interval. The chord comparison extends by continuity. At and beyond the first return the explicitly tuned pulse gives a zero chord, the minimum possible.

Finally, $`\cosh r=1+2a^2s^2`$ implies $`r=2\mathrm{arsinh}(a|s|)`$, giving the displayed survival. The theorem allows complex transverse drives and arbitrary integrable detunings. The finite-deadline objective is for deterministic waveforms. For the exact coherent-only statement, an input-independent mixture with branch-known unitary correction cannot circumvent the threshold: its surviving Choi block has rank one only if the nonzero surviving operator of every branch is proportional to the same unitary after correction.

## Optional terminal filter

If the terminal hardware can implement a calibrated contraction on the surviving rails, apply

```math
F=\sigma_{\min}(A) A^{-1}.
```

The filtered operation has $`FA=\sigma_{\min}(A)I`$. Use the singular-vector bases of $`A`$ and attenuate the more transmissive singular mode. Feed both vacuum and rejected filter outcomes into the same erasure flag. The final survival is state-independent and equal to the prefilter least-input survival. The attenuation is an idealized endpoint operation outside the coherent pulse interval.

For optimality, the successful block of any exact unitary-survivor channel has a rank-one Choi matrix. Each successful Kraus operator $`F_j`$ acting on the prefilter code block must satisfy $`F_j A=c_j V`$ for that unitary $`V`$. A success operation acting on vacuum can only contribute an entanglement-breaking block and cannot add to this nonzero rank-one qubit Choi block. The inequality $`\sum_jF_j^\dagger F_j\le I`$ then gives $`p(A^{-1})^\dagger A^{-1}\le I`$, where $`p=\sum_j|c_j|^2`$. Thus $`p\le\lambda_{\min}(A^\dagger A)`$. Combined with the optimal pulse, this gives the exact deadline–survival tradeoff for protocols with an ideal filter after deterministic open-loop control.

## An elementary check of the exact speed limit

There is also a direct proof of the first-return deadline. Write $`XX^\dagger=q_0I+q\cdot\sigma`$. If $`g\le a`$, then $`\dot q_z\le -2a q_0+2g|q_\perp|\lt 0`$, so the initial point never recurs at positive time.

For $`g\gt a`$, before the first return of $`q_z`$ to zero put $`x=|q_\perp|`$ and $`w=-q_z\gt 0`$. The radial equations are $`\dot x=2u w`$, $`\dot q_0=2a w`$, and $`\dot w=2a q_0-2u x`$ for an effective quadrature $`|u|\le g`$. They hold almost everywhere, including the zero set of $`x`$ with $`u=0`$. Integration gives $`x\le(g/a)(q_0-1)`$. Set $`p=(a q_0-g x)/\omega`$. The angular velocity of $`p+iw`$ is bounded above by $`2\omega`$, as

```math
\frac{d}{dt}\arg(p+iw)=2\omega+
\frac{2(g-u)}{\omega(p^2+w^2)}\big[a x q_0-g(q_0^2-1)\big]
\le 2\omega.
```

At the first positive zero of $`w`$, one has $`q_0\gt 1`$ and $`g x\ge a(q_0+1)`$, using $`x^2=q_0^2-1`$ and the integrated bound. Hence $`p\lt 0`$ there and the phase has gained $`\pi`$. The first lobe lasts at least $`\pi/(2\omega)`$.

If $`X(T)`$ is unitary, then $`Y(s)=\sigma_x X(T-s)X(T)^{-1}\sigma_x`$ is another admissible normalized propagator from the identity. Its initial lobe corresponds to the final lobe of the original curve with the sign of $`q_z`$ reversed, so the two lobes have disjoint interiors. Their lengths give $`T\ge\pi/\omega`$. The resonant constant pulse attains it.
