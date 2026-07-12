# 6. Kesimpulan

Penelitian ini telah berhasil menjalankan eksperimen simulasi *noise injection* untuk mengevaluasi ketangguhan arsitektur algoritma hibrida AHP-TOPSIS terhadap fenomena *rank reversal*. Hasil eksperimen mengungkap bahwa pemeringkatan AHP-TOPSIS mampu bertahan dan sangat stabil secara struktural ketika diintervensi oleh deviasi bobot sebesar $\pm 10\%$ hingga $\pm 20\%$, dibuktikan dengan nilai Koefisien Korelasi Spearman ($\rho$) dan Kendall Tau ($\tau$) di atas $0.95$. Namun, ambang batas toleransi terpetakan saat gangguan bobot mencapai atau melampaui $\pm 30\%$, di mana sistem mengalami *rank reversal* yang signifikan dan nilai korelasi menurun tajam, sehingga mencederai objektivitas rekomendasi keputusan. 

Uji komputasi juga membuktikan bahwa penyuntikan *noise* pembobotan kriteria tidak mengubah efisiensi waktu eksekusi secara langsung; *bottleneck* utama *runtime* AHP-TOPSIS murni dipengaruhi oleh pertumbuhan eksponensial baris alternatif matriks saat diuji pada 10.000 data sintetis.

**Penelitian Lanjutan (*Future Work*)**  
Hasil temuan memetakan ambang kritis toleransi model AHP-TOPSIS yang berguna bagi pengembang SPK ke depan. Penelitian selanjutnya sangat disarankan untuk menerapkan uji ketangguhan serupa (*benchmarking* dengan skrip otomatis) terhadap algoritma-algoritma lain seperti VIKOR atau PROMETHEE, serta mempertimbangkan optimasi kalkulasi matriks *backend* guna mengakomodasi volume *Big Data* tanpa mengorbankan stabilitas urutan keputusan.
