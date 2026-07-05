# -*- coding: utf-8 -*-
"""
main.py
=======
Entry-point utama eksperimen AHP-TOPSIS.

Menjalankan pengujian sensitivitas bobot pada dataset sintetis (n=10.000).
Data riil akan dimasukkan secara terpisah oleh peneliti.

Setiap run menggunakan seed berbeda (multiple runs) untuk mendapatkan
distribusi hasil yang valid secara statistik.

Penggunaan:
  python main.py                          # jalankan dengan default
  python main.py --n 10000               # tentukan jumlah data sintetis
  python main.py --delta-range 0 50 --step 10
  python main.py --help                   # lihat semua opsi
"""

import argparse
import io
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

# ── Paksa UTF-8 di Windows ─────────────────────────────
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ── Impor modul eksperimen ──────────────────────────────
from src.ahp_topsis import run_ahp_topsis
from src.data_loader import CRITERIA, generate_synthetic_data, get_pairwise_matrix, load_real_data, set_seed
from src.logger import ExperimentLogger
from src.sensitivity_test import run_sensitivity_test

# ══════════════════════════════════════════════════════════
# CLI Argument Parser
# ══════════════════════════════════════════════════════════


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Eksperimen Sensitivitas Bobot AHP-TOPSIS — DSS Evaluasi Soft Skill",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python main.py                              # jalankan semua skenario
  python main.py --dataset real               # hanya dataset riil (n=140)
  python main.py --dataset synthetic --n 5000 # sintetis dengan 5000 data
  python main.py --delta-range 10 50 --step 10 --output hasil/log.csv
        """,
    )

    parser.add_argument(
        "--n",
        type=int,
        default=10000,
        help="Jumlah data sintetis yang di-generate (default: 10000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Seed awal untuk reprodusibilitas (default: 42)",
    )
    parser.add_argument(
        "--delta-range",
        nargs=2,
        type=float,
        metavar=("MIN", "MAX"),
        default=[0, 50],
        help="Rentang gangguan bobot dalam persen, default: 0 50",
    )
    parser.add_argument(
        "--step",
        type=float,
        default=10,
        help="Interval langkah gangguan bobot (default: 10)",
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=5,
        help="Jumlah run per skenario (default: 5)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output",
        help="Direktori output hasil (default: output/)",
    )
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Suppress output terminal (hanya tampilkan error)",
    )

    parser.add_argument(
        "--dataset",
        choices=["all", "real", "synthetic"],
        default="all",
        help="Skenario dataset yang dijalankan: all | real | synthetic (default: all)",
    )
    parser.add_argument(
        "--real-csv",
        type=str,
        default=None,
        help="Path ke CSV dataset riil (default: auto-detect 04-data/datasetsimulasi_riil_140.csv)",
    )

    return parser


# ══════════════════════════════════════════════════════════
# Fungsi Utilitas
# ══════════════════════════════════════════════════════════


def print_header(text: str, quiet: bool = False) -> None:
    if not quiet:
        sep = "=" * 60
        print(f"\n{sep}")
        print(f"  {text}")
        print(sep)


def print_progress(msg: str, quiet: bool = False) -> None:
    if not quiet:
        print(f"  >> {msg}")


def print_result(label: str, value, quiet: bool = False) -> None:
    if not quiet:
        print(f"    {label:<25} {value}")


# ══════════════════════════════════════════════════════════
# Skenario Eksperimen
# ══════════════════════════════════════════════════════════


def run_scenario(
    scenario_name: str,
    df,
    pairwise_matrix: np.ndarray,
    delta_values: list[float],
    seeds: list[int],
    logger: ExperimentLogger,
    quiet: bool = False,
) -> None:
    """
    Jalankan satu skenario eksperimen (mis. 'Real Dataset') dengan multiple runs.

    Alur per run:
      1. Set seed
      2. Buat decision matrix dari DataFrame
      3. Jalankan AHP-TOPSIS baseline (delta=0%)
      4. Untuk setiap delta, jalankan uji sensitivitas
      5. Log semua hasil
    """
    n_students = len(df)
    print_header(f"Skenario: {scenario_name} (n={n_students})", quiet)

    for run_idx, seed in enumerate(seeds, start=1):
        print_progress(f"Run {run_idx}/{len(seeds)} — seed={seed}", quiet)
        set_seed(seed)

        # ── Persiapan decision matrix ────────────────────
        dm = df[CRITERIA].values.astype(float)

        # ── Baseline (delta = 0%) ──────────────────────
        t_start = time.perf_counter()
        baseline = run_ahp_topsis(dm, pairwise_matrix)
        t_end = time.perf_counter()
        baseline_runtime = (t_end - t_start) * 1000

        base_ranks = baseline["ranks"]
        base_weights = baseline["weights"]
        cr = baseline["cr"]

        print_result(
            "CR (AHP):",
            f"{cr:.4f} {'OK' if baseline['is_consistent'] else 'FAIL CR>0.1!'}",
            quiet,
        )
        print_result("Baseline runtime:", f"{baseline_runtime:.2f} ms", quiet)

        # Log baseline
        logger.log(
            scenario=scenario_name,
            dataset_size=n_students,
            seed=seed,
            delta_w_pct=0.0,
            spearman_rho=1.0,
            kendall_tau=1.0,
            runtime_ms=baseline_runtime,
            reversal_detected=False,
            notes=f"baseline, CR={cr:.4f}",
        )

        # ── Loop delta values ─────────────────────────
        for delta in delta_values:
            if delta == 0:
                continue  # sudah di-log sebagai baseline

            t_start = time.perf_counter()
            try:
                result = run_sensitivity_test(
                    delta_w_pct=delta,
                    base_weights=base_weights,
                    base_ranks=base_ranks,
                    decision_matrix=dm,
                    pairwise_matrix=pairwise_matrix,
                    run_ahp_topsis_fn=run_ahp_topsis,
                    top_k=min(10, n_students // 5),
                )
                t_end = time.perf_counter()
                runtime_ms = (t_end - t_start) * 1000

                anomaly = runtime_ms > baseline_runtime * 5
                notes = "runtime anomaly suspected" if anomaly else ""

                run_id = logger.log(
                    scenario=scenario_name,
                    dataset_size=n_students,
                    seed=seed,
                    delta_w_pct=delta,
                    spearman_rho=result["spearman_rho"],
                    kendall_tau=result["kendall_tau"],
                    runtime_ms=runtime_ms,
                    reversal_detected=result["reversal_detected"],
                    anomaly_flag=anomaly,
                    notes=notes,
                )

                reversal_mark = " [REVERSAL]" if result["reversal_detected"] else ""
                anomaly_mark = " [ANOMALY]" if anomaly else ""
                print_result(
                    f"  δ={delta:4.0f}%:",
                    f"ρ={result['spearman_rho']:.4f}  "
                    f"τ={result['kendall_tau']:.4f}  "
                    f"t={runtime_ms:.2f}ms"
                    f"{reversal_mark}{anomaly_mark}",
                    quiet,
                )

                if anomaly:
                    logger.log_anomaly(
                        run_id,
                        f"Runtime anomaly: {runtime_ms:.2f}ms vs baseline {baseline_runtime:.2f}ms",
                    )

            except MemoryError:
                t_end = time.perf_counter()
                run_id = logger.log(
                    scenario=scenario_name,
                    dataset_size=n_students,
                    seed=seed,
                    delta_w_pct=delta,
                    spearman_rho=float("nan"),
                    kendall_tau=float("nan"),
                    runtime_ms=-1.0,
                    reversal_detected=False,
                    anomaly_flag=True,
                    notes="OOM error — skipped",
                )
                logger.log_anomaly(
                    run_id, f"MemoryError pada delta={delta}%, n={n_students}"
                )
                print_progress(
                    f"  [OOM] Pada delta={delta}% -- dicatat & dilanjutkan", quiet
                )

            finally:
                logger.cleanup_memory()

        print()


# ══════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    quiet = args.quiet

    # ── Setup ─────────────────────────────────────────
    delta_min, delta_max = args.delta_range
    delta_values = [
        float(round(d, 1)) for d in np.arange(delta_min, delta_max + args.step, args.step)
    ]
    seeds = [42, 123, 456, 789, 1001][: args.runs]

    output_dir = Path(args.output)
    logger = ExperimentLogger(output_dir=str(output_dir))
    pairwise_matrix = get_pairwise_matrix()

    if not quiet:
        print("=" * 62)
        print("  Eksperimen Sensitivitas AHP-TOPSIS")
        print("  DSS Evaluasi Soft Skill -- MA Mu'allimin Sruweng")
        print("-" * 62)
        print(f"  Dataset   : {args.dataset.capitalize()}")
        print(f"  Delta (%) : {delta_values}")
        print(f"  Seeds     : {seeds}")
        print(f"  Output    : {output_dir}")
        print("=" * 62)

    run_real    = args.dataset in ("all", "real")
    run_synth   = args.dataset in ("all", "synthetic")

    # ── Dataset Riil ──────────────────────────────────
    if run_real:
        try:
            df_real = load_real_data(args.real_csv)
            run_scenario(
                scenario_name="Real Dataset",
                df=df_real,
                pairwise_matrix=pairwise_matrix,
                delta_values=delta_values,
                seeds=seeds,
                logger=logger,
                quiet=quiet,
            )
        except FileNotFoundError as e:
            print(f"\n  [SKIP] Dataset riil tidak ditemukan: {e}", file=sys.stderr)
        except ValueError as e:
            print(f"\n  [SKIP] Dataset riil gagal dimuat: {e}", file=sys.stderr)

    # ── Generate & Jalankan Dataset Sintetis ──────────
    if run_synth:
        if not quiet:
            print(f"\n  [Synthetic] Generating {args.n} data (seed={args.seed})...")
        df_syn = generate_synthetic_data(n=args.n, seed=args.seed)
        run_scenario(
            scenario_name="Synthetic Dataset",
            df=df_syn,
            pairwise_matrix=pairwise_matrix,
            delta_values=delta_values,
            seeds=seeds,
            logger=logger,
            quiet=quiet,
        )

    # ── Ringkasan Akhir ───────────────────────────────
    summary = logger.summary()
    print_header("Ringkasan Eksperimen", quiet=quiet)
    for k, v in summary.items():
        print_result(k + ":", v, quiet)

    if not quiet:
        print(f"\n  CSV log   : {logger.get_csv_path()}")
        print(f"  JSONL log : {logger.get_jsonl_path()}")
        print("\n  [OK] Eksperimen selesai.\n")

    # Simpan summary ke JSON
    summary_path = output_dir / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
