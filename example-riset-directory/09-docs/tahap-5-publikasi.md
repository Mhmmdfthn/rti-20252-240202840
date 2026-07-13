# Tahap 5: Penyusunan Naskah Jurnal Publikasi

**Tujuan:** Mengompilasi seluruh rancangan teori, metodologi eksekusi *script*, dan data korelasi hasil eksperimen ke dalam format naskah akademis terstandar.

## Rincian Penulisan per Bab

Dokumen ini disinkronisasikan ke folder `07-manuskrip/`.
- **Abstrak**: Ringkasan *noise injection*, *Spearman Rank*, *Kendall Tau*, dan temuan batas deviasi $20\%$.
- **Pendahuluan**: Latar belakang subjektivitas SPK, celah literatur (minimnya studi ketahanan algoritma dinamis), dan signifikansi uji *Rank Reversal*.
- **Metodologi**: Spesifikasi data (140 vs 10.000), rumus AHP-TOPSIS, rumusan Spearman & Kendall Tau, dan alur perulangan penyuntikan deviasi pada skrip CLI.
- **Hasil**: Narasi tabel *Baseline*, grafik penurunan $\rho$ seiring perbesaran $\Delta W$, serta fenomena eksponensial *runtime* matriks 10.000.
- **Kesimpulan**: Konfirmasi hipotesis kerentanan arsitektur MCDM saat mencapai titik patahan (*breaking point*) dan usulan riset lanjutan.
