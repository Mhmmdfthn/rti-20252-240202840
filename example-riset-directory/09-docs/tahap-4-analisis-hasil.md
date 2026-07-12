# Tahap 4: Analisis Hasil Eksperimen

**Tujuan:** Mengekstraksi data log dan mengonversi fenomena matematis ke dalam konklusi riset.

## 1. Analisis Spearman Rank & Kendall Tau
Membaca file `experiment_log.csv`. Memetakan nilai koefisien korelasi Spearman ($\rho$) dan stabilitas Kendall Tau ($\tau$) terhadap level $\Delta W$:
- $\rho \ge 0.90$ : Sangat Stabil
- $0.75 \le \rho < 0.90$ : Mulai Terganggu
- $\rho < 0.75$ : Pembalikan Peringkat (*Rank Reversal*) Ekstrem

*Ekspektasi Temuan:* Akan ada titik (misal $30\%$) di mana nilai korelasi menukik tajam secara eksponensial. Titik ini disebut *Ambang Batas Toleransi (Safety Margin)*.

## 2. Analisis Beban Komputasi (*Execution Time*)
Membandingkan *runtime* kalkulasi matriks 140 baris dengan 10.000 baris. 
*Ekspektasi Temuan:* Modifikasi bobot (noise injection) tidak memberi beban memori, namun volume baris matriks memberi efek *bottleneck* eksponensial akibat struktur perulangan TOPSIS konvensional.
