"""
logger.py
=========
Modul logging terstruktur untuk eksperimen AHP-TOPSIS.

Fungsi:
  ExperimentLogger — kelas utama untuk mencatat dan mengekspor hasil eksperimen
"""

import csv
import gc
import json
import os
from datetime import datetime, timezone
from pathlib import Path


class ExperimentLogger:
    """
    Logger terstruktur untuk mencatat setiap run eksperimen.

    Data yang dicatat per entry:
      - Identitas   : run_id, timestamp, scenario
      - Konfigurasi : seed, dataset_size, delta_w_pct, code_version
      - Hasil       : spearman_rho, kendall_tau, runtime_ms, reversal_detected
      - Metadata    : anomaly_flag, notes
    """

    VERSION = "1.0.0"

    def __init__(self, output_dir: str = "results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self._csv_path  = self.output_dir / "benchmark_log.csv"
        self._jsonl_path = self.output_dir / "run_log.jsonl"

        self._entries: list[dict] = []
        self._run_counter = 0

        # Tulis header CSV
        self._init_csv()

    # ── Init ───────────────────────────────────────────
    def _init_csv(self) -> None:
        if not self._csv_path.exists():
            with open(self._csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self._csv_fields())
                writer.writeheader()

    @staticmethod
    def _csv_fields() -> list[str]:
        return [
            "run_id", "timestamp", "scenario", "dataset_size",
            "seed", "delta_w_pct", "code_version",
            "spearman_rho", "kendall_tau", "runtime_ms",
            "reversal_detected", "anomaly_flag", "notes",
        ]

    # ── Logging ────────────────────────────────────────
    def log(
        self,
        *,
        scenario: str,
        dataset_size: int,
        seed: int,
        delta_w_pct: float,
        spearman_rho: float,
        kendall_tau: float,
        runtime_ms: float,
        reversal_detected: bool,
        anomaly_flag: bool = False,
        notes: str = "",
    ) -> str:
        """
        Catat satu hasil run ke memori, CSV, dan JSONL.

        Returns
        -------
        str — run_id yang baru dibuat
        """
        self._run_counter += 1
        run_id = f"run-{scenario.lower().replace(' ', '-')}-{self._run_counter:04d}"
        timestamp = datetime.now(tz=timezone.utc).isoformat()

        entry = {
            "run_id":            run_id,
            "timestamp":         timestamp,
            "scenario":          scenario,
            "dataset_size":      dataset_size,
            "seed":              seed,
            "delta_w_pct":       delta_w_pct,
            "code_version":      self.VERSION,
            "spearman_rho":      round(spearman_rho, 6),
            "kendall_tau":       round(kendall_tau, 6),
            "runtime_ms":        round(runtime_ms, 3),
            "reversal_detected": reversal_detected,
            "anomaly_flag":      anomaly_flag,
            "notes":             notes,
        }

        self._entries.append(entry)
        self._append_csv(entry)
        self._append_jsonl(entry)

        return run_id

    def _append_csv(self, entry: dict) -> None:
        with open(self._csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self._csv_fields())
            writer.writerow(entry)

    def _append_jsonl(self, entry: dict) -> None:
        with open(self._jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # ── Utilitas ───────────────────────────────────────
    def log_anomaly(self, run_id: str, description: str) -> None:
        """Tambahkan catatan anomali ke file terpisah."""
        anomaly_path = self.output_dir / "anomaly_log.txt"
        with open(anomaly_path, "a", encoding="utf-8") as f:
            ts = datetime.now(tz=timezone.utc).isoformat()
            f.write(f"[{ts}] {run_id}: {description}\n")

    def summary(self) -> dict:
        """Kembalikan ringkasan statistik semua entry yang sudah dicatat."""
        if not self._entries:
            return {}

        rhos      = [e["spearman_rho"] for e in self._entries]
        runtimes  = [e["runtime_ms"]   for e in self._entries]
        reversals = [e["reversal_detected"] for e in self._entries]

        return {
            "total_runs":         len(self._entries),
            "spearman_rho_mean":  round(sum(rhos)     / len(rhos),    4),
            "spearman_rho_min":   round(min(rhos),    4),
            "spearman_rho_max":   round(max(rhos),    4),
            "runtime_ms_mean":    round(sum(runtimes) / len(runtimes), 3),
            "runtime_ms_min":     round(min(runtimes), 3),
            "runtime_ms_max":     round(max(runtimes), 3),
            "total_reversals":    sum(reversals),
            "reversal_rate_pct":  round(100 * sum(reversals) / len(reversals), 2),
        }

    def get_csv_path(self) -> str:
        return str(self._csv_path)

    def get_jsonl_path(self) -> str:
        return str(self._jsonl_path)

    @staticmethod
    def cleanup_memory() -> None:
        """Panggil garbage collector antar-run untuk mencegah OOM."""
        gc.collect()
