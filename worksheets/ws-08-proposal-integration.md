# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment)
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [✔] Problem → Gap: masalah terdokumentasi di literatur
  [✔] Gap → RQ: pertanyaan menjawab gap spesifik
  [✔] RQ → Hypothesis: hipotesis memprediksi jawaban
  [✔] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [✔] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [✔] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [✔] Istilah sama di semua bagian
  [✔] Variabel di RQ = variabel di hipotesis = metrik di desain
  [✔] Scope tidak berubah dari masalah ke eksperimen

Rubrik Self-Assessment:
| Kriteria    | 1 (Lemah) | 2 (Cukup) | 3 (Baik) | Skor |
|-------------|-----------|-----------|----------|------|
| Koherensi   |           |           | ✔        | 3    |
| Specificity |           |           | ✔        | 3    |
| Feasibility |           | ✔         |          | 2    |
| Rigor       |           |           | ✔        | 3    |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Proses evaluasi kompetensi soft skill siswa di MA Mu'allimin Sruweng masih bergantung pada pengamatan subjektif guru tanpa mekanisme pembobotan kriteria multidimensi yang terstruktur, sehingga hasil penilaian rentan bias dan inkonsistensi antar-penilai. |
| Gap | WS-03 | Belum adanya model DSS yang mengintegrasikan pembobotan kriteria hierarkis (AHP) dan pemeringkatan berbasis jarak solusi ideal (TOPSIS) secara komprehensif, yang dirancang khusus untuk domain evaluasi soft skill siswa di sekolah formal. |
| RQ | WS-04 | Apakah implementasi model DSS hibrida berbasis integrasi komprehensif AHP-TOPSIS dengan struktur 13 indikator operasional mampu menghasilkan nilai closeness coefficient yang stabil, konsisten secara logis (CR ≤ 0.1), dan bebas bias evaluator dibandingkan sistem penilaian konvensional sekolah? |
| Hipotesis | WS-04 | H₁: Model DSS berbasis integrasi AHP-TOPSIS menghasilkan nilai rasio konsistensi kriteria yang valid (CR ≤ 0.1) serta memberikan pemisahan peringkat preferensi (Vi) yang tajam untuk memetakan 4 klasifikasi tingkat kompetensi siswa. |
| Variabel & Metrik | WS-05 | IV = Pergeseran Bobot Kriteria (Δw, %); DV = Stabilitas Peringkat Akhir diukur dengan Koefisien Rank Spearman (ρ) dan Efisiensi Komputasi diukur dengan Execution Time (ms); CV = Dimensi Matriks Keputusan (140 × 13). |
| Sistem | WS-06 | Sistem terdiri dari 4 modul: (1) Perturbation Simulator (IV), (2) Spearman Rank Evaluator (DV-1), (3) Execution Time Benchmarker (DV-2), dan (4) Core Data Loader — dikontrol via file experiment_config.json agar config-driven dan reproducible. |
| Desain Eksperimen | WS-07 | Eksperimen bertipe Parameter Study: Kondisi kontrol (Δw = 0%) vs kondisi treatment (Δw = ±10% hingga ±50%) pada matriks 140 × 13 yang identik; analisis menggunakan Wilcoxon Signed-Rank Test (α = 0.05). |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap (ketiadaan model MCDM hibrida untuk soft skill) muncul langsung dari analisis 5 paper relevan yang menunjukkan pola limitasi berulang: subjektivitas pembobotan tunggal dan tidak adanya validasi instrumen penilaian (WS-03). |
| Gap → RQ | ✅ | RQ secara eksplisit bertanya apakah integrasi komprehensif AHP-TOPSIS mampu mengatasi gap tersebut, yakni menghasilkan pemeringkatan yang konsisten (CR ≤ 0.1) dan bebas bias evaluator (WS-04). |
| RQ → Hypothesis | ✅ | H₁ memprediksi jawaban terukur dari RQ: CR ≤ 0.1 dan pemisahan 4 klasifikasi kompetensi melalui rentang nilai preferensi Vi (0 ≤ Vi ≤ 1) (WS-04). |
| Hypothesis → Metric | ✅ | Variabel di H₁ (konsistensi pembobotan dan ketajaman peringkat) dioperasionalisasi ke metrik Consistency Ratio (CR), Closeness Coefficient (Vi), Rank Spearman (ρ), dan Execution Time — semua dengan skala dan satuan terdefinisi (WS-05). |
| Metric → System | ✅ | Setiap metrik dipetakan ke komponen sistem yang spesifik: Perturbation Simulator → Δw, Spearman Evaluator → ρ, Execution Benchmarker → ms, Core Data Loader → matriks 140×13 (WS-06). |
| System → Experiment | ✅ | Desain eksperimen Parameter Study menggunakan seluruh komponen sistem sebagai instrumen pengujian; kondisi kontrol dan treatment dikontrol via experiment_config.json dengan dataset identik (WS-07). |

**Koneksi mana yang paling lemah?** Metric → System (aspek pengukuran tied ranks pada Spearman)
**Bagaimana cara memperkuatnya?**
> Mengintegrasikan penanganan komponen *tied ranks* secara ketat pada modul Spearman Calculator, dan menyandingkan metrik Spearman dengan Kendall's Tau-b sebagai secondary metric penguat untuk memitigasi potensi distorsi nilai ρ.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [✔] Ya / [ ] Tidak
> Istilah "AHP-TOPSIS", "Consistency Ratio (CR)", "Closeness Coefficient (Vi)", dan "matriks 140×13" digunakan secara konsisten dari WS-04 hingga WS-07 tanpa perubahan scope.

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 — Baik | Keenam koneksi kritis (Problem→Gap→RQ→Hipotesis→Metrik→Sistem→Eksperimen) terjalin kuat dan tidak ada lompatan logis. Setiap komponen dapat ditelusuri balik ke masalah asal. |
| Specificity | 3 — Baik | Semua metrik sudah terdefinisi secara numerik: CR ≤ 0.1, ρ (Spearman), Vi (0–1), dan execution time (ms). Threshold pengambilan keputusan H₀/H₁ sudah dideklarasikan sebelum eksperimen. |
| Feasibility | 2 — Cukup | Dataset 140 siswa riil dari satu institusi sudah tersedia dan dapat diakses. Namun, skenario stress testing (skala 1.000–10.000 entri) dan validasi PLS-SEM membutuhkan waktu dan sumber daya tambahan yang perlu dipertimbangkan dalam timeline. |
| Rigor | 3 — Baik | Ancaman validitas (internal, eksternal, construct, conclusion) telah diidentifikasi dan dimitigasi sebelum eksperimen. Uji statistik inferensial (Wilcoxon Signed-Rank, α = 0.05) dipilih sesuai tipe data ordinal/interval berpasangan. |

**Skor total:** 11 / 12

**Apakah proposal siap untuk fase eksekusi?** [✔] Ya / [ ] Belum
> Proposal sudah siap untuk fase implementasi teknis. Catatan: skenario validasi eksternal (dataset multi-institusi) dapat dijadwalkan sebagai eksperimen lanjutan pada iterasi penelitian berikutnya.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Latihan di WS-04 (Formulasi RQ & Hipotesis), karena setelah gap dari WS-03 sudah teridentifikasi dengan jelas, struktur pertanyaan riset dan pasangan hipotesisnya mengalir secara alami mengikuti logika "apa yang ingin dibuktikan".

**Bagian tersulit:** Latihan di WS-05 (Operasionalisasi Variabel & Metrik), karena menerjemahkan konsep abstrak seperti "stabilitas peringkat" menjadi metrik konkret yang memiliki skala, satuan, dan justifikasi construct validity yang kuat membutuhkan pemikiran kritis yang mendalam.

**Yang akan dilakukan berbeda:**
> Memulai pembuatan *integration map* sejak WS-02, bukan menunggu hingga WS-08. Dengan memetakan koneksi antar-komponen lebih awal, inkonsistensi terminologi dan lompatan logis dapat dideteksi dan diperbaiki secara bertahap, bukan sekaligus di akhir.
> Selain itu, akan lebih proaktif mendokumentasikan setiap keputusan desain (mengapa metrik X dipilih bukan Y) sejak awal, sehingga rubrik rigor di WS-08 bisa terpenuhi dengan lebih mudah.
