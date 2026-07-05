# 06-output

Hasil olahan data & visualisasi — **Tahap 4** (lihat [../09-docs/tahap-4-analisis-data.md](../09-docs/tahap-4-analisis-data.md)).

Dihasilkan oleh `05-kode/experiment/main.py` dan divisualisasikan oleh `05-kode/experiment/plot_results.py` dari data eksperimen `04-data/` (dataset riil 140 baris & dataset sintetis 10k baris, masing-masing 5 replikasi).

## logs/

| File | Isi |
|---|---|
| `benchmark_log.csv` | Log mentah metrik (`spearman_rho`, `kendall_tau`, `runtime`) per (dataset_size, delta_w, seed) |
| `run_log.jsonl` | Log terstruktur format JSON Lines untuk pembacaan mesin/basis data |
| `summary.json` | Ringkasan statistik (mean/min/max) agregat keseluruhan eksperimen (60 runs) |
| `anomaly_log.txt` | Catatan anomali saat eksperimen berjalan (contoh: overhead runtime OS/CPU interrupt) |

## plots/

| File | Isi |
|---|---|
| `fig_spearman_rho.png` | Line chart tren degradasi `spearman_rho` seiring kenaikan Δw: Real vs Synthetic dataset |
| `fig_kendall_tau.png` | Line chart tren stabilitas `kendall_tau` (rank inversion) seiring kenaikan Δw |
| `fig_runtime.png` | Line chart dengan *error bars* runtime komputasi (ms) seiring kenaikan Δw |

## Acuan

[../09-docs/tahap-4-analisis-data.md](../09-docs/tahap-4-analisis-data.md)
