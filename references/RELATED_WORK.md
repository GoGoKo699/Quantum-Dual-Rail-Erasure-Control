# Related work

## Dual-rail control and loss

**Hajr et al.** derive the driven, unequal-loss dual-rail generator and its spectrum in Supplementary Eqs. S85–S87. Their constant-drive criterion is precisely that the coupling exceed one quarter of the difference in excitation decay rates. Exponentiating their matrix also gives the isolated constant-pulse revival. Their experiments characterize dynamical protection and an erasure bias, with dephasing and heating relevant to actual device performance. The present question is the optimum across all admissible waveforms at a prescribed deadline, including the best worst-input survival before exact revival. [Hajr et al., 2026](https://arxiv.org/html/2610.10432v1)

**Mehta et al.** analyze unequal-loss backaction in a swap–wait–swap gate. In Appendix G, a midpoint logical $`X`$ cancels the two equal intervals of no-jump backaction in the discrete-pulse analysis. Their master-equation simulations study the particular gate implementation. Charging the finite duration of the mixing pulse while maintaining continuous rail loss leads to the waveform optimization solved here. [Mehta et al., 2026, Appendix G in the preprint](https://arxiv.org/html/2503.10935v2#A7)

**Teoh et al.** develop the superconducting-cavity dual-rail architecture and explain why the vacuum makes one-photon loss detectable. **Chou et al.** demonstrate dual-rail logical measurement with integrated erasure detection. The project uses this flag convention and studies the surviving qubit under calibrated unequal decay. [Teoh et al., 2023](https://doi.org/10.1073/pnas.2221736120) · [Chou et al., 2024](https://doi.org/10.1038/s41567-024-02539-4)

**Klauck et al.** implement a passive lossy directional coupler and study two-photon interference across an exceptional point. The same two-mode non-Hermitian dynamics underlie the constant control example here. The channel-synthesis task uses an arbitrary logical input with an optional reference and optimizes its survival across a larger class of controls. [Klauck et al., 2025](https://doi.org/10.1126/sciadv.adr8275)

**Brewster et al.** discuss polarization-dependent loss compensation with additional passive attenuation and heralded amplification or attenuation. Attenuating the better transmitted singular mode is an inherited way to rebalance the output. Here it is a separate terminal resource, and the optimum derives from jointly selecting the preceding coherent waveform and the filter at a fixed deadline. [Brewster et al., 2019](https://doi.org/10.1103/PhysRevA.100.033811)

## Hyperbolic comparison

**Ghomi**, Theorem 3.1, generalizes Schur's chord comparison to nonpositive curvature. A chord-convex model curve of the same length and with no smaller geodesic curvature supplies a lower bound on chord distance. The proof here identifies the normalized survival effect with a hyperbolic curve and translates the bound on the coherent coupling into the geodesic-curvature hypothesis. [Ghomi, Theorem 3.1](https://ghomi.math.gatech.edu/Papers/curvrigidII.pdf)

## Quantum-channel framework

**Watrous** provides the mathematical language for quantum channels, output flags, reference systems and channel distinguishability. The [learning bridge](../learning/WATROUS_BRIDGE.md) points to the specific sections used in this project. [Watrous, 2018](https://jhwatrous.github.io/books-and-courses.html)
