import numpy as np
from scipy import stats

# ══════════════════════════════════════════════════════════
# Perturbasi Bobot
# ══════════════════════════════════════════════════════════


def perturb_weights(
    base_weights: np.ndarray,
    delta_pct: float,
    mode: str = "uniform",
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    w = base_weights.copy().astype(float)
    delta = delta_pct / 100.0

    if mode == "uniform":
        # Geser semua bobot ke arah seragam (lebih adil/rata)
        uniform = np.ones_like(w) / len(w)
        perturbed = (1 - delta) * w + delta * uniform
    elif mode == "random":
        if rng is None:
            rng = np.random.default_rng(42)
        noise = rng.uniform(-delta, delta, size=len(w))
        perturbed = w + noise * w  # gangguan proporsional
        perturbed = np.clip(perturbed, 1e-6, None)
    else:
        raise ValueError(
            f"Mode tidak dikenal: {mode!r}. Gunakan 'uniform' atau 'random'."
        )

    # Normalisasi ulang
    perturbed /= perturbed.sum()
    return perturbed


# ══════════════════════════════════════════════════════════
# Metrik Statistik
# ══════════════════════════════════════════════════════════


def compute_spearman(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
) -> float:
    rho, _ = stats.spearmanr(ranks_base, ranks_perturbed)
    return float(rho)


def detect_reversal(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
    top_k: int = 10,
) -> bool:
    top_base = set(np.where(ranks_base <= top_k)[0])
    top_perturbed = set(np.where(ranks_perturbed <= top_k)[0])
    return top_base != top_perturbed


def compute_kendall_tau(
    ranks_base: np.ndarray,
    ranks_perturbed: np.ndarray,
) -> float:
    """Hitung Kendall's Tau-b sebagai metrik korelasi tambahan."""
    tau, _ = stats.kendalltau(ranks_base, ranks_perturbed)
    return float(tau)


# ══════════════════════════════════════════════════════════
# Skenario Uji Sensitivitas
# ══════════════════════════════════════════════════════════


def run_sensitivity_test(
    delta_w_pct: float,
    base_weights: np.ndarray,
    base_ranks: np.ndarray,
    decision_matrix: np.ndarray,
    pairwise_matrix: np.ndarray,
    run_ahp_topsis_fn,
    top_k: int = 10,
) -> dict:

    # 1. Perturbasi bobot
    perturbed_w = perturb_weights(base_weights, delta_w_pct, mode="uniform")

    # 2. Jalankan ulang dengan sub_weights yang sudah diperturbasi
    result = run_ahp_topsis_fn(
        decision_matrix=decision_matrix,
        pairwise_matrix=pairwise_matrix,
        sub_weights=perturbed_w,
    )
    perturbed_ranks = result["ranks"]

    # 3. Hitung metrik
    rho = compute_spearman(base_ranks, perturbed_ranks)
    tau = compute_kendall_tau(base_ranks, perturbed_ranks)
    reversal = detect_reversal(base_ranks, perturbed_ranks, top_k=top_k)

    return {
        "delta_w_pct": delta_w_pct,
        "perturbed_weights": perturbed_w,
        "perturbed_ranks": perturbed_ranks,
        "spearman_rho": rho,
        "kendall_tau": tau,
        "reversal_detected": reversal,
    }
