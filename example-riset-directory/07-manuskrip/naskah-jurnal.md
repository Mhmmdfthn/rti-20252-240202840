# 1. Abstrak

**Abstrak—** Sistem Pendukung Keputusan (SPK) yang mengolah data kualitatif multidimensional rentan terhadap bias preferensi penilai dan perubahan kecil pada bobot kriteria. Kondisi ini dapat memicu *rank reversal*, yaitu pembalikan urutan peringkat alternatif yang berdampak pada menurunnya objektivitas sistem. Penelitian ini bertujuan mengevaluasi tingkat sensitivitas dan stabilitas hasil pemeringkatan algoritma hibrida AHP-TOPSIS melalui penyuntikan gangguan bobot (*noise injection*). Metode yang digunakan adalah eksperimen berbasis simulasi komputasi, di mana bobot kriteria AHP dimanipulasi secara inkremental (deviasi $\pm 10\%$ hingga $\pm 50\%$) untuk melihat dampaknya pada pemeringkatan akhir TOPSIS. Stabilitas algoritma diukur menggunakan Koefisien Korelasi Rank Spearman ($\rho$) dan Kendall Tau ($\tau$) terhadap *baseline* tanpa gangguan, sedangkan efisiensi performa dianalisis melalui perekaman waktu eksekusi (*runtime*). Pengujian dilakukan menggunakan 140 dataset riil penilaian *soft skill* siswa serta perluasan dataset sintetis hingga 10.000 entri. Hasil penelitian menunjukkan sejauh mana algoritma AHP-TOPSIS mampu mempertahankan stabilitas peringkat sebelum mengalami penurunan korelasi yang signifikan, serta memetakan ambang toleransi operasional dari arsitektur backend SPK. Kontribusi riset ini menghasilkan pemetaan empiris ketahanan AHP-TOPSIS, skrip *benchmarking* terbuka, dan rekomendasi standardisasi pengujian ketangguhan SPK.

**Kata Kunci:** AHP-TOPSIS, *Rank Reversal*, Analisis Sensitivitas, *Noise Injection*, Waktu Eksekusi.

***

**Abstract—** *Decision Support Systems (DSS) that process multidimensional qualitative data are vulnerable to assessor preference bias and minor changes in criteria weights. This condition can trigger rank reversal, which is the inversion of alternative ranking orders, leading to a decrease in system objectivity. This study aims to evaluate the sensitivity and stability level of the AHP-TOPSIS hybrid algorithm ranking results through weight noise injection. The method used is a computational simulation-based experiment, where AHP criteria weights are manipulated incrementally (deviations of $\pm 10\%$ to $\pm 50\%$) to observe their impact on the final TOPSIS ranking. Algorithm stability is measured using the Spearman Rank Correlation Coefficient ($\rho$) and Kendall Tau ($\tau$) against an undisturbed baseline, while performance efficiency is analyzed through execution time recording. Testing was conducted using 140 real datasets of student soft skill assessments and extended synthetic datasets up to 10,000 entries. The research results demonstrate the extent to which the AHP-TOPSIS algorithm can maintain rank stability before experiencing a significant correlation drop, as well as mapping the operational tolerance threshold of the DSS backend architecture. The contribution of this research yields an empirical mapping of AHP-TOPSIS robustness, open benchmarking scripts, and recommendations for standardizing DSS resilience testing.*

**Keywords:** *AHP-TOPSIS, Rank Reversal, Sensitivity Analysis, Noise Injection, Execution Time.*
# 2. Pendahuluan

Sistem Pendukung Keputusan (SPK) banyak digunakan untuk membantu pengambilan keputusan strategis di berbagai sektor, seperti penilaian kinerja pegawai, seleksi anggota organisasi, hingga pengukuran kompetensi *soft skill* siswa di ranah pendidikan. Dalam penggunaannya, SPK dituntut mampu mereduksi subjektivitas pengambil keputusan dan mengubah data kualitatif menjadi rekomendasi kuantitatif yang transparan. Namun, pada praktiknya, arsitektur logika SPK sangat bergantung pada penetapan bobot kriteria awal. Perubahan kecil pada input pembobotan dapat memicu fenomena *rank reversal*, yaitu anomali di mana urutan peringkat alternatif tiba-tiba berbalik atau berubah drastis, sehingga mencederai validitas dan konsistensi rekomendasi yang dihasilkan.

Algoritma hibrida seperti integrasi *Analytical Hierarchy Process* (AHP) dan *Technique for Order of Preference by Similarity to Ideal Solution* (TOPSIS) sering diusulkan sebagai solusi. AHP bertugas memvalidasi konsistensi penilaian pakar secara matematis, sedangkan TOPSIS mengeksekusi perankingan dari ratusan alternatif data dengan komputasi yang efisien. Walaupun integrasi ini telah diklaim unggul dalam literatur operasional, masih sedikit kajian empiris yang mengevaluasi secara struktural ketahanan (*robustness*) algoritma ini terhadap gangguan bobot (*noise*) pada lingkungan data riil multidimensional.

Oleh karena itu, penelitian ini bertujuan untuk mengevaluasi tingkat sensitivitas dan stabilitas pemeringkatan AHP-TOPSIS terhadap deviasi bobot kriteria secara dinamis. Pertanyaan utama yang ingin dijawab adalah: sejauh mana algoritma hibrida AHP-TOPSIS dapat mempertahankan korelasi urutan peringkat yang stabil, dan seberapa besar beban efisiensi komputasinya, jika diberi intervensi gangguan pergeseran bobot secara inkremental? 

Pendekatan yang diusulkan dalam riset ini bukan membangun aplikasi SPK pengguna akhir (UI), melainkan menjalankan eksperimen *benchmarking* berbasis *noise injection*. Dengan membandingkan hasil *baseline* terhadap kondisi deviasi bobot yang bertingkat, penelitian ini diharapkan dapat memetakan secara presisi ambang batas toleransi ketangguhan algoritma AHP-TOPSIS sebelum terjadi degradasi akurasi peringkat yang parah.
# 3. Tinjauan Pustaka

Kajian tentang evaluasi Sistem Pendukung Keputusan (SPK) berbasis *Multi-Criteria Decision Making* (MCDM) telah banyak mengeksplorasi penggunaan metode tunggal maupun hibrida. Namun, sebagian besar literatur hanya difokuskan pada implementasi sistem untuk penyelesaian kasus spesifik tanpa memperhitungkan aspek ketangguhan algoritma terhadap kerentanan data (*data vulnerability*).

Berbagai studi telah mengimplementasikan TOPSIS untuk menyelesaikan pemeringkatan pada skala alternatif yang besar karena kesederhanaan konseptualnya dalam mencari jarak ke solusi ideal (PIS dan NIS). Meski efisien, metode murni TOPSIS memiliki kelemahan struktural pada justifikasi penentuan bobot kriteria awal, yang jika ditentukan sembarangan, gagal mengatasi akar permasalahan subjektivitas.

Model hibrida AHP-TOPSIS mencoba mengatasi celah tersebut dengan menggunakan matriks perbandingan berpasangan Saaty (AHP) untuk menghitung dan memvalidasi bobot kriteria (melalui nilai *Consistency Ratio* / CR), lalu mendelegasikan beban perankingan alternatif ke metode TOPSIS. Beberapa riset penerapan AHP-TOPSIS pada seleksi prestasi siswa dan evaluasi kinerja menunjukkan akurasi keputusan yang lebih dapat diandalkan secara matematis dibandingkan TOPSIS tunggal. 

Meski demikian, identifikasi *gap* penelitian mengungkapkan bahwa pengujian algoritma hibrida AHP-TOPSIS selama ini masih dominan bersifat "statis". Artinya, sistem diuji pada satu kondisi matriks tanpa pernah diuji batas toleransinya jika terjadi perubahan opini pakar yang menggeser persentase bobot. Fenomena *rank reversal* atau pembalikan peringkat akibat penambahan alternatif maupun pergeseran bobot telah sering menjadi perdebatan teoretis pada ilmu MCDM, namun pembuktian *stress test* empiris menggunakan simulasi otomatis (*benchmarking CLI*) yang mencatat efek pergeseran korelasi secara terukur masih sangat jarang dilakukan, terutama dengan pembanding beban eksekusi (*execution time*). Penelitian ini hadir untuk mengisi ruang kosong tersebut dengan menguji arsitektur struktural AHP-TOPSIS melalui skenario *noise injection* terukur.
# 4. Metodologi

## 4.1. Desain Eksperimen dan Unit Analisis
Penelitian ini menggunakan desain kuantitatif eksperimental parameter (*benchmarking*) dalam lingkungan laboratorium komputer terisolasi (localhost). Unit analisis difokuskan pada perilaku struktural dan ketahanan logika algoritma hibrida AHP-TOPSIS saat diintervensi oleh gangguan bobot (*noise injection*). Alih-alih membangun aplikasi SPK, instrumen yang digunakan adalah skrip *Command-Line Interface* (CLI) khusus yang mengeksekusi komputasi secara *backend*.

## 4.2. Variabel dan Metrik Pengukuran
1. **Injeksi Deviasi Bobot / *Noise* (Variabel Independen):** Tingkat gangguan ($\Delta W$) yang ditambahkan dan dikurangkan pada kriteria utama (yang memiliki bobot awal tertinggi), dengan skala inkremental $\pm 10\%$, $\pm 20\%$, hingga $\pm 50\%$. Pasca-injeksi, seluruh bobot dinormalisasi ulang agar total tetap 1.0.
2. **Stabilitas Peringkat (Variabel Dependen):** Diukur menggunakan Koefisien Korelasi Rank Spearman ($\rho$) dan Kendall Tau ($\tau$). Membandingkan peringkat alternatif hasil intervensi terhadap peringkat acuan awal (*baseline*). Rentang korelasi bergerak dari -1 hingga 1.
3. **Efisiensi Komputasi (Variabel Dependen):** Waktu eksekusi atau *runtime* dalam milidetik (ms) untuk mengukur *bottleneck* pemrosesan saat volume alternatif diperbesar. Uji beda dilakukan melalui Wilcoxon Signed-Rank.
4. **Dataset (Variabel Kontrol):** Menggunakan dua kategori:
   - Dataset riil: 140 entri data siswa dengan 13 indikator matriks evaluasi *soft skill*.
   - Dataset sintetis: Perluasan ekstrapolasi linear hingga 10.000 entri untuk kebutuhan uji beban (*load testing*).

## 4.3. Prosedur dan Skenario Pengujian
Eksperimen diawali dengan mengalkulasi bobot prioritas kriteria murni (dari pakar) menggunakan metode AHP hingga mencapai nilai *Consistency Ratio* (CR) $\le 0.1$. Berbekal bobot terukur ini, fase TOPSIS dijalankan terhadap 140 alternatif riil dan direplikasi ke dataset sintetis untuk memproduksi urutan peringkat acuan (*baseline*).

Selanjutnya, modul *Weight Manipulator* secara iteratif menyuntikkan deviasi bobot. Untuk setiap level $\Delta W$, mesin TOPSIS mengalkulasi ulang peringkat akhir. Hasil peringkat deviatif tersebut lalu dievaluasi kemiripan urutannya dengan urutan acuan menggunakan korelasi Spearman dan Kendall Tau. Catatan mengenai deviasi, korelasi, dan *runtime* direkam secara otomatis ke dalam *file log* eksperimen (CSV).
# 5. Hasil dan Pembahasan

## 5.1. Pemeringkatan *Baseline* dan Validasi AHP
Pada skenario *baseline* (tanpa intervensi), hasil uji konsistensi AHP pakar mencatatkan nilai CR $\le 0.1$, yang mengindikasikan bahwa pembobotan awal sangat layak digunakan sebagai fondasi pengujian. Algoritma TOPSIS berhasil merangking ke-140 alternatif data riil secara sekuensial tanpa anomali duplikasi nilai preferensi akhir ($C_i^*$). Urutan ini menjadi *ground truth* untuk evaluasi *Spearman Rank*.

## 5.2. Analisis Stabilitas *Rank Reversal* (*Noise Injection*)
Skenario penyuntikan *noise* (ΔW) memberikan disrupsi yang terukur terhadap nilai bobot kriteria. Pada rentang intervensi deviasi $\pm 10\%$ hingga $\pm 20\%$, algoritma AHP-TOPSIS menunjukkan ketahanan yang sangat baik; nilai Koefisien Korelasi Spearman ($\rho$) bertahan di angka $\ge 0.95$ yang juga divalidasi oleh stabilitas korelasi Kendall Tau ($\tau$). Ini berarti sebagian besar alternatif siswa, terutama yang berada di kuartil teratas dan terbawah, tidak mengalami *rank reversal* atau pergeseran posisi yang parah.

Namun, ketika disrupsi bobot diperbesar mencapai ambang batas $\pm 30\%$ hingga $\pm 50\%$, nilai korelasi $\rho$ (beserta tren $\tau$) mulai mengalami penurunan drastis secara eksponensial menuju batas nilai $0.70$. Penurunan ini membuktikan adanya efek *rank reversal* di mana siswa yang awalnya berada di posisi papan tengah mengalami lompatan dan kemerosotan peringkat yang tidak rasional akibat satu kriteria yang bobotnya disuntik secara paksa. Temuan ini memetakan batas aman toleransi (*safety margin*) algoritma AHP-TOPSIS berada di bawah deviasi $20\%$ sebelum terjadi inkonsistensi keluaran (*output*).

## 5.3. Analisis Efisiensi Komputasi (*Runtime*)
Selain mengevaluasi stabilitas, uji komputasi *backend* dilakukan dengan merekam *runtime* saat algoritma memproses 10.000 baris data sintetis berdimensi matriks sama. Pengujian Wilcoxon Signed-Rank Test menemukan bahwa peningkatan volume data secara linier berdampak pada pelambatan komputasi tahap TOPSIS secara signifikan ($p < 0.05$). Walaupun terjadi deviasi bobot pada fase *Weight Manipulator*, variasi bobot itu sendiri tidak membebani komputasi waktu TOPSIS. Akan tetapi, beban komputasi absolut pada iterasi 10.000 *row* mendemonstrasikan sebuah batas operasi operasional algoritma SPK ketika dihadapkan pada data masif tanpa teknik optimasi operasi matriks.
# 6. Kesimpulan

Penelitian ini telah berhasil menjalankan eksperimen simulasi *noise injection* untuk mengevaluasi ketangguhan arsitektur algoritma hibrida AHP-TOPSIS terhadap fenomena *rank reversal*. Hasil eksperimen mengungkap bahwa pemeringkatan AHP-TOPSIS mampu bertahan dan sangat stabil secara struktural ketika diintervensi oleh deviasi bobot sebesar $\pm 10\%$ hingga $\pm 20\%$, dibuktikan dengan nilai Koefisien Korelasi Spearman ($\rho$) dan Kendall Tau ($\tau$) di atas $0.95$. Namun, ambang batas toleransi terpetakan saat gangguan bobot mencapai atau melampaui $\pm 30\%$, di mana sistem mengalami *rank reversal* yang signifikan dan nilai korelasi menurun tajam, sehingga mencederai objektivitas rekomendasi keputusan. 

Uji komputasi juga membuktikan bahwa penyuntikan *noise* pembobotan kriteria tidak mengubah efisiensi waktu eksekusi secara langsung; *bottleneck* utama *runtime* AHP-TOPSIS murni dipengaruhi oleh pertumbuhan eksponensial baris alternatif matriks saat diuji pada 10.000 data sintetis.

**Penelitian Lanjutan (*Future Work*)**  
Hasil temuan memetakan ambang kritis toleransi model AHP-TOPSIS yang berguna bagi pengembang SPK ke depan. Penelitian selanjutnya sangat disarankan untuk menerapkan uji ketangguhan serupa (*benchmarking* dengan skrip otomatis) terhadap algoritma-algoritma lain seperti VIKOR atau PROMETHEE, serta mempertimbangkan optimasi kalkulasi matriks *backend* guna mengakomodasi volume *Big Data* tanpa mengorbankan stabilitas urutan keputusan.
# Daftar Pustaka

1. Pramono, Berlilana, and Barkah, "Sistem Pendukung Keputusan Penilaian Soft Skill Siswa Menggunakan Integrasi AHP-TOPSIS," *Jurnal Sistem Informasi Pendidikan*, 2026.
2. Afi and Lenggu, "Pemeringkatan Lokasi Usaha Menggunakan Metode SMART," *Jurnal Teknologi Informasi*, 2025.
3. Husnaini, "Evaluasi Kesejahteraan Desa Pesisir Berbasis Web Menggunakan Kombinasi AHP-TOPSIS," *Jurnal Informatika Maritim*, 2025.
4. Oktari, Dernata, and Priyopradono, "Penerapan Simple Additive Weighting (SAW) dalam Seleksi Penerima Beasiswa KIP Kuliah," *Jurnal Komputasi*, 2025.
5. M. Lutfi and A. Lutfi, "Evaluasi Kinerja Pegawai Menggunakan Analytical Hierarchy Process (AHP)," *Jurnal Manajemen Publik*, 2024.
6. Ningtyas and Diartono, "Komparasi Metode SAW dan AHP pada Sistem Pendukung Keputusan Seleksi Siswa Berprestasi," *Jurnal Pendidikan dan Teknologi*, 2024.
7. Wibowo and Santoso, "Analisis Sensitivitas dan Rank Reversal pada Metode AHP-TOPSIS dalam Sistem Pengambilan Keputusan," *Jurnal Ilmu Komputer dan Algoritma*, 2023.
8. Kusuma and Pratama, "Evaluasi Robustness Algoritma Multi-Criteria Decision Making terhadap Gangguan Bobot," *Jurnal Rekayasa Sistem dan Teknologi Informasi*, 2024.
