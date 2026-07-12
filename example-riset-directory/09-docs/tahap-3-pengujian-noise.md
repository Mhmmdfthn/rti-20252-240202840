# Tahap 3: Pengujian Noise Injection

**Tujuan:** Mengeksekusi penyuntikan *noise* (deviasi) dan mendeteksi anomali *Rank Reversal*.

## Skenario Eksperimen
1. Mesin *Python CLI* dijalankan di terminal.
2. Bobot asli (*baseline*) dicatat (misal: Kriteria 1 = 0.40).
3. Pengujian masuk ke iterasi 1: Skrip menyuntikkan deviasi $10\%$. Bobot diturunkan (0.36) atau dinaikkan (0.44), sementara 3 bobot lainnya dinormalisasi ulang agar total tetap 1.0. 
4. *Engine* TOPSIS dijalankan ulang menggunakan kombinasi bobot baru.
5. Urutan rekomendasi terbaru direkam.
6. Langkah 3 hingga 5 diulang untuk deviasi $20\%, 30\%, 40\%$, dan $50\%$.

## Identifikasi Masalah
Fokus deteksi pada kuartil teratas (*Top 10*): apakah terjadi loncatan alternatif (misalnya Siswa X yang asalnya peringkat 12 mendadak menjadi peringkat 3)? Jika iya, fenomena *Rank Reversal* dikonfirmasi positif.
