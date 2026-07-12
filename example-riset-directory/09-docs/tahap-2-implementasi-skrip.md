# Tahap 2: Implementasi Skrip CLI Eksperimen

**Tujuan:** Membangun *Calculation Engine* AHP-TOPSIS beserta modul intervensi deviasi bobot.

## Rincian Modul Python

1. **`ahp_topsis.py`**:
   Berisi logika matematis kalkulasi *Eigen Value* (AHP), pengujian batas inkonsistensi (*Consistency Ratio* / CR), pembentukan *decision matrix*, penentuan Solusi Ideal Positif & Negatif, dan ekstraksi *Closeness Coefficient* (Cci). Output dari modul ini akan menjadi *Ground Truth* (Peringkat *Baseline* tanpa gangguan).

2. **`sensitivity_test.py`**:
   Modul pengganggu utama (*Noise Injector*). Akan secara terprogram mencari kriteria dengan bobot terbesar, lalu menambahkan deviasi ($\Delta W$) sebesar $10\%, 20\%, \dots, 50\%$. Modul ini juga menghitung korelasi peringkat dengan metrik Spearman ($\rho$) dan Kendall Tau ($\tau$).

3. **`logger.py`**:
   Modul pasif yang memonitor *timestamp* awal dan akhir setiap fungsi komputasi untuk mendapatkan *runtime execution* dalam milidetik, lalu menyimpannya di file `experiment_log.csv`.
