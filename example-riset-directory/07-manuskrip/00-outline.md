# Outline Naskah Jurnal

**Judul Jurnal:** ANALISIS PERFORMA ALGORITMA HIBRIDA AHP-TOPSIS DALAM REDUKSI SUBJEKTIVITAS DATA PADA SISTEM PENGAMBIL KEPUTUSAN

## Struktur Draf

**1. Abstrak**
- Latar belakang kerentanan SPK terhadap perubahan bobot (bias preferensi).
- Metode eksperimen: Simulasi komputasi *noise injection* (deviasi bobot) untuk menguji *rank reversal*.
- Parameter uji: Korelasi Spearman ($\rho$), Kendall Tau ($\tau$), dan Waktu Eksekusi (*Runtime*).
- Dataset: 140 riil & hingga 10.000 sintetis.
- Hasil singkat: Peta toleransi ketangguhan algoritma AHP-TOPSIS.

**2. Pendahuluan**
- Pentingnya SPK untuk mengubah data kualitatif menjadi kuantitatif objektif.
- Permasalahan: SPK sangat bergantung pada bobot awal. Deviasi kecil bisa memicu *rank reversal*.
- Pengenalan integrasi AHP-TOPSIS, namun mempertanyakan ketahanan (*robustness*) secara struktural di lingkungan *backend*.
- Tujuan riset: Mencari ambang toleransi stabilitas peringkat (korelasi) vs intervensi *noise injection* dinamis.

**3. Tinjauan Pustaka**
- Kelebihan dan kekurangan TOPSIS (efisien tapi bobot arbitrer).
- Solusi AHP-TOPSIS (mengukur *Consistency Ratio*).
- Identifikasi *gap*: Literatur selama ini bersifat "statis", jarang mengekspos model pada uji batas ketahanan dinamis (*sensitivity analysis* & *rank reversal*).

**4. Metodologi**
- Desain eksperimen komputasi (*benchmarking*) menggunakan instrumen CLI.
- Variabel independen: Injeksi deviasi bobot $\Delta W$ ($\pm 10\%$ s.d. $\pm 50\%$).
- Variabel dependen: Stabilitas peringkat (Korelasi Spearman $\rho$, Kendall Tau $\tau$) dan *Runtime* komputasi (ms).
- Prosedur skenario dari validasi AHP, injeksi *noise*, hingga perbandingan *baseline* vs intervensi.

**5. Hasil dan Pembahasan**
- Pemeringkatan *baseline* dan hasil CR AHP.
- Stabilitas peringkat: AHP-TOPSIS tahan uji pada deviasi $\le \pm 20\%$ (Spearman $\rho \ge 0.95$, Kendall Tau $\tau \ge 0.95$).
- Kejadian *Rank Reversal*: Penurunan akurasi drastis pada deviasi $\ge \pm 30\%$.
- Efisiensi komputasi: *Noise* tidak memengaruhi *runtime*, melainkan volume baris data yang menciptakan *bottleneck* eksponensial.

**6. Kesimpulan**
- Ambang batas toleransi stabilitas AHP-TOPSIS berada di titik $\pm 20\%$. Melewati itu, akan terjadi anomali *rank reversal* berlebihan.
- Keterbatasan eksekusi (*runtime*) murni disebabkan komputasi skala *Big Data*.
- Penelitian lanjutan: Menerapkan skrip *benchmarking* CLI untuk membandingkan model-model MCDM lain (misal VIKOR, PROMETHEE).
