"""Reproduce finite checks of the dual-rail erasure-control frontier."""

import numpy as np
from scipy.linalg import expm, svdvals


IDENTITY = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOLERANCE = 2e-12


def close(actual, expected):
    np.testing.assert_allclose(actual, expected, atol=TOLERANCE, rtol=TOLERANCE)


def pulse_for_deadline(rates, g, duration):
    """Return the prescribed coupling and closed-form minimum survival."""
    a = abs(rates[0] - rates[1]) / 4
    b = np.exp(-sum(rates) * duration / 2)
    if a == 0:
        return 0.0, b

    if g > a:
        omega = np.sqrt((g - a) * (g + a))
        if duration >= np.pi / omega:
            return np.hypot(a, np.pi / duration), b
        s = np.sin(omega * duration) / omega
    elif g < a:
        decay = np.sqrt((a - g) * (a + g))
        s = np.sinh(decay * duration) / decay
    else:
        s = duration

    anisotropy = a * abs(s)
    return g, b / (np.hypot(1, anisotropy) + anisotropy) ** 2


def transfer_for_schedule(rates, schedule):
    """Propagate the code-space transfer directly through constant segments."""
    drift = -np.diag(rates) / 2
    transfer = IDENTITY.copy()
    for duration, hamiltonian in schedule:
        segment = expm(duration * (drift - 1j * hamiltonian))
        transfer = segment @ transfer
    return transfer


def random_schedule(rng, g, duration):
    """Draw a seeded waveform of arbitrary rail phase, detuning and segment time."""
    lengths = duration * rng.dirichlet(np.ones(8))
    schedule = []
    for length in lengths:
        magnitude = g * np.sqrt(rng.uniform())
        phase = rng.uniform(0, 2 * np.pi)
        detuning = rng.normal(scale=1 + 3 * g)
        transverse = np.cos(phase) * X + np.sin(phase) * Y
        schedule.append((length, magnitude * transverse + detuning * Z))
    return schedule


def check_frontier():
    rng = np.random.default_rng(1126)
    cases = 0
    comparisons = 0
    formula_error = 0.0
    worst_margin = float("inf")

    rate_pairs = ((4.0, 0.0), (0.4, 4.4), (0.7, 0.7), (0.0, 0.0))
    for rates in rate_pairs:
        a = abs(rates[0] - rates[1]) / 4
        scale = max(a, 1)
        for ratio in (0, 0.6, 1 - 1e-7, 1, 1 + 1e-7, 1.6, 4):
            g = a * ratio if a else ratio
            durations = [0.08 / scale, 0.5 / scale, 1.3 / scale]
            if a and g > 1.01 * a:
                first_return = np.pi / np.sqrt((g - a) * (g + a))
                durations.extend(first_return * fraction for fraction in (0.5, 0.9, 1, 1.25))

            for duration in durations:
                coupling, optimum = pulse_for_deadline(rates, g, duration)
                if coupling > g + TOLERANCE:
                    raise AssertionError("The constructive pulse exceeds the coupling limit.")
                selected = transfer_for_schedule(rates, [(duration, coupling * X)])
                actual = float(svdvals(selected)[-1] ** 2)
                close(actual, optimum)
                formula_error = max(formula_error, abs(actual - optimum))

                expected_det = np.exp(-sum(rates) * duration / 2)
                close(abs(np.linalg.det(selected)), expected_det)
                for _ in range(24):
                    waveform = random_schedule(rng, g, duration)
                    transfer = transfer_for_schedule(rates, waveform)
                    close(abs(np.linalg.det(transfer)), expected_det)
                    survival = float(svdvals(transfer)[-1] ** 2)
                    margin = optimum - survival
                    if margin < -TOLERANCE:
                        raise AssertionError((rates, g, duration, survival, optimum))
                    worst_margin = min(worst_margin, margin)
                    comparisons += 1
                cases += 1

    print(f"Frontier: {cases} parameter points, {comparisons} seeded waveform comparisons")
    print(f"Largest pulse/formula difference: {formula_error:.3g}")
    print(f"Smallest optimum-minus-sample margin: {worst_margin:.3g}")


def joint_lindblad_output(rates, schedule, initial, reference_dimension):
    """Integrate the full Lindblad equation with the vacuum and reference present."""
    joint_dimension = 3 * reference_dimension
    joint_identity = np.eye(joint_dimension)
    ref_identity = np.eye(reference_dimension)
    dissipator = np.zeros((joint_dimension**2, joint_dimension**2), dtype=complex)
    for rail, rate in enumerate(rates):
        local_jump = np.zeros((3, 3), dtype=complex)
        local_jump[2, rail] = np.sqrt(rate)
        jump = np.kron(local_jump, ref_identity)
        jump_square = jump.conj().T @ jump
        dissipator += np.kron(jump.conj(), jump)
        dissipator -= (np.kron(joint_identity, jump_square)
                       + np.kron(jump_square.T, joint_identity)) / 2

    output = np.zeros((joint_dimension, joint_dimension), dtype=complex)
    code_dimension = 2 * reference_dimension
    output[:code_dimension, :code_dimension] = initial
    state = output.flatten(order="F")
    for duration, code_hamiltonian in schedule:
        local_hamiltonian = np.zeros((3, 3), dtype=complex)
        local_hamiltonian[:2, :2] = code_hamiltonian
        hamiltonian = np.kron(local_hamiltonian, ref_identity)
        commutator = np.kron(joint_identity, hamiltonian)
        commutator -= np.kron(hamiltonian.T, joint_identity)
        state = expm(duration * (dissipator - 1j * commutator)) @ state
    return state.reshape((joint_dimension, joint_dimension), order="F")


def reduced_reference(joint, reference_dimension):
    return np.trace(joint.reshape(2, reference_dimension, 2, reference_dimension),
                    axis1=0, axis2=2)


def joint_flagged_output(transfer, initial, reference_dimension):
    ref_identity = np.eye(reference_dimension)
    full_transfer = np.kron(transfer, ref_identity)
    success = full_transfer @ initial @ full_transfer.conj().T
    output = np.zeros((3 * reference_dimension, 3 * reference_dimension), dtype=complex)
    code_dimension = 2 * reference_dimension
    output[:code_dimension, :code_dimension] = success
    output[code_dimension:, code_dimension:] = reduced_reference(initial - success,
                                                                 reference_dimension)
    return output


def terminal_filter(transfer):
    """Use an SVD to pass the weaker singular mode and balance the stronger one."""
    left, values, right_adjoint = np.linalg.svd(transfer)
    attenuation = np.diag(values[-1] / values)
    filter_operator = right_adjoint.conj().T @ attenuation @ left.conj().T
    return filter_operator, values[-1] ** 2


def ideal_erasure(initial, probability, reference_dimension):
    result = np.zeros((3 * reference_dimension, 3 * reference_dimension), dtype=complex)
    code_dimension = 2 * reference_dimension
    result[:code_dimension, :code_dimension] = probability * initial
    result[code_dimension:, code_dimension:] = (1 - probability) * reduced_reference(
        initial, reference_dimension)
    return result


def check_channel_and_filter():
    rates = (2.6, 0.2)
    reference_dimension = 3
    state_vector = np.array([1, -0.4j, 0.2, -0.3 + 0.7j, 1.2, 0.8j])
    state_vector /= np.linalg.norm(state_vector)
    initial = np.outer(state_vector, state_vector.conj())
    a = abs(rates[0] - rates[1]) / 4
    duration = 2.8
    resonant_g = np.hypot(a, np.pi / duration)
    exact_schedule = [(duration, resonant_g * X)]
    detuned_schedule = [(0.31, 0.6 * X + 0.3 * Z), (0.29, -0.4 * Y + 1.2 * Z)]

    for schedule in (exact_schedule, detuned_schedule):
        transfer = transfer_for_schedule(rates, schedule)
        predicted = joint_flagged_output(transfer, initial, reference_dimension)
        integrated = joint_lindblad_output(rates, schedule, initial, reference_dimension)
        close(predicted, integrated)
        close(np.trace(integrated), 1)
        if np.linalg.eigvalsh(integrated)[0] < -TOLERANCE:
            raise AssertionError("The integrated state is not positive.")

    exact_probability = np.exp(-sum(rates) * duration / 2)
    exact_transfer = transfer_for_schedule(rates, exact_schedule)
    close(exact_transfer.conj().T @ exact_transfer, exact_probability * IDENTITY)
    close(joint_flagged_output(exact_transfer, initial, reference_dimension),
          ideal_erasure(initial, exact_probability, reference_dimension))

    unbalanced = transfer_for_schedule(rates, detuned_schedule)
    filter_operator, filter_probability = terminal_filter(unbalanced)
    close(svdvals(filter_operator)[0], 1)
    compensated = filter_operator @ unbalanced
    close(compensated, np.sqrt(filter_probability) * IDENTITY)
    close(joint_flagged_output(compensated, initial, reference_dimension),
          ideal_erasure(initial, filter_probability, reference_dimension))

    higher_probability = min(1.01 * filter_probability, 1)
    impossible_filter = np.sqrt(higher_probability) * np.linalg.inv(unbalanced)
    if svdvals(impossible_filter)[0] <= 1:
        raise AssertionError("A larger exact-success weight appeared contractive.")

    print("Channel: full Lindblad evolution with an inert reference agrees in both cases")
    print("Filter: contractivity, exact reference preservation and the finite upper bound agree")


def main():
    check_frontier()
    check_channel_and_filter()


if __name__ == "__main__":
    main()
