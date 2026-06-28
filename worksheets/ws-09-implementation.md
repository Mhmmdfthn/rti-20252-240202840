# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel Core i5-1235U, 10 Core (2P + 8E), 4.4 GHz Max
  RAM     : 16 GB DDR4 3200 MHz
  GPU     : Intel Iris Xe Graphics (CPU-only, tidak digunakan)
  Storage : SSD NVMe 512 GB

Software:
  OS        : Windows 11 Home 64-bit (Build 22631)
  Runtime   : Python 3.11.9
  Framework : NumPy + SciPy + Pandas (scientific stack)

Dependencies:
| Library  | Version | Sumber          | Hash/Checksum               |
|----------|---------|-----------------|-----------------------------|
| numpy    | 1.26.4  | PyPI (pip)      | SHA256: terdokumentasi di requirements.txt |
| pandas   | 2.2.2   | PyPI (pip)      | SHA256: terdokumentasi di requirements.txt |
| scipy    | 1.13.0  | PyPI (pip)      | SHA256: terdokumentasi di requirements.txt |

Konfigurasi:
  Config file     : experiment/experiment_config.json (di-commit ke Git)
  Random seed     : 42 (random.seed + np.random.seed + PYTHONHASHSEED)
  Hyperparameters : delta_w_range = [-50%..+50%], step=10%, runs=30

Reproducibility Check:
  [✔] Dependency terdokumentasi (requirements.txt + pip freeze > requirements_lock.txt)
  [✔] Seed ditetapkan di semua level (Python random, NumPy, os.environ PYTHONHASHSEED)
  [✔] Config di version control (experiment_config.json di-track Git)
  [✔] README instruksi reproduksi lengkap (lihat Latihan 3)
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda.

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5-1235U, 10 Core (2P + 8E), Clock Max 4.4 GHz |
| RAM | 16 GB DDR4 3200 MHz |
| GPU | Intel Iris Xe Graphics (tidak digunakan — CPU-only computation) |
| OS | Windows 11 Home 64-bit, Build 22631 |
| Runtime | Python 3.11.9 (via virtual environment `venv`) |
| Framework | NumPy 1.26.4 (komputasi matriks) + SciPy 1.13.0 (statistik) + Pandas 2.2.2 (data manipulation) |
| Random Seed | 42 — dikunci di tiga level: `random.seed(42)`, `np.random.seed(42)`, `os.environ["PYTHONHASHSEED"] = "42"` |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| numpy | 1.26.4 | Operasi matriks presisi tinggi: normalisasi vektor, perkalian matriks, jarak Euclidean untuk TOPSIS |
| pandas | 2.2.2 | Load/manipulasi dataset 140 siswa × 13 indikator dari CSV, ekspor hasil ke format tabular |
| scipy | 1.13.0 | Uji statistik inferensial: `stats.spearmanr()`, `stats.kendalltau()`, `stats.wilcoxon()` |
| json (stdlib) | built-in | Baca `experiment_config.json` dan tulis log hasil eksperimen secara terstruktur |
| time (stdlib) | built-in | `time.perf_counter()` untuk mengukur execution time sub-milidetik dengan presisi tinggi |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Rank Spearman (ρ) pada kondisi Δw = +30% | — (baseline) |
| 2 | 42 | Rank Spearman (ρ) pada kondisi Δw = +30% | [✔] Ya / [ ] Tidak |
| 3 | 42 | Rank Spearman (ρ) pada kondisi Δw = +30% | [✔] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**
> Seed belum di-set di semua level Python (hanya `random.seed` tapi lupa `np.random.seed` dan `PYTHONHASHSEED`), atau terdapat state tersembunyi dalam cache NumPy/OS yang tidak di-reset antar-run. Proses background Windows (seperti Windows Defender, indexing) juga dapat menyebabkan fluktuasi pada metrik execution time meskipun nilai ρ tetap identik.

**Checklist kontrol yang sudah diterapkan:**
- [✔] Random seed di-set di semua level (`random.seed(42)`, `np.random.seed(42)`, `os.environ["PYTHONHASHSEED"]="42"` dipanggil di fungsi `set_global_seed()` sebelum setiap run)
- [✔] Tidak ada background process yang mengganggu (eksperimen dijalankan via terminal tanpa browser/aplikasi lain aktif)
- [✔] Cache dibersihkan antar-run (array objek direinisialisasi di awal setiap iterasi loop, Python garbage collector tidak menyimpan state antar-run)
- [✔] Config file yang sama untuk semua run (`experiment_config.json` di-load sekali dan bersifat read-only selama eksperimen)

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Uji Sensitivitas & Stabilitas Peringkat Algoritma Hibrida AHP-TOPSIS
# pada DSS Evaluasi Soft Skill Siswa MA Mu'allimin Sruweng

## 1. Environment

Hardware:
  - CPU     : Intel Core i5-1235U (10 Core, 4.4 GHz Max)
  - RAM     : 16 GB DDR4
  - Storage : SSD NVMe 512 GB

Software:
  - OS      : Windows 11 Home 64-bit (Build 22631)
  - Python  : 3.11.9 (gunakan virtual environment)
  - Runtime : NumPy 1.26.4 + SciPy 1.13.0 + Pandas 2.2.2

## 2. Installation

# 1. Clone repository
git clone https://github.com/[username]/dss-ahp-topsis.git
cd dss-ahp-topsis

# 2. Buat virtual environment Python
python -m venv venv

# 3. Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies (versi terkunci)
pip install -r experiment/requirements.txt

# 5. Verifikasi instalasi
python -c "import numpy, pandas, scipy; print('OK')"

## 3. Data

- Sumber      : Data penilaian siswa kelas X & XI MA Mu'allimin Sruweng
- Format      : CSV (students_assessment.csv + expert_pairwise_matrix.csv)
- Ukuran      : 140 baris (siswa) × 13 kolom (indikator soft skill)
- Struktur    :
    students_assessment.csv    → student_id, K1..K4, KO1..KO3, KP1..KP3, TJ1..TJ3
    expert_pairwise_matrix.csv → matriks 4×4 perbandingan berpasangan pakar

## 4. Execution

# Pindah ke direktori benchmark
cd experiment/ahp_topsis_benchmark

# Jalankan benchmark dengan dataset riil saja (Fase 1 & 2)
python main.py --dataset real --delta-range 10 50 --step 10

# Jalankan uji beban dengan 10.000 data sintetis (Fase 3)
python main.py --dataset synthetic --n 10000 --delta-range 10 50 --step 10

# Jalankan semua pengujian sekaligus dan simpan ke file log CSV
python main.py --dataset all --n 10000 --delta-range 10 50 --step 10 --output results/benchmark_log.csv

## 5. Configuration

Kontrol eksperimen sekarang dipusatkan melalui argumen CLI `argparse` di `main.py`:
  --dataset      : "real", "synthetic", atau "all"
  --n            : Jumlah data sintetis (default: 10000)
  --delta-range  : Rentang gangguan bobot (min max, default: 10 50)
  --step         : Interval penambahan gangguan bobot (default: 10)
  --output       : Lokasi penyimpanan file CSV (default: results/benchmark_log.csv)

PENTING: Validitas dijamin dengan random seed 42 di `data_loader.py` dan pembersihan memori `gc.collect()` per iterasi untuk menghindari latensi.

## 6. Expected Output

File: experiment/ahp_topsis_benchmark/results/benchmark_log.csv

dataset_size,delta_w_pct,spearman_rho,runtime_ms,reversal_detected
140,0,1.0,1.52,False
140,10,0.9857,0.91,False
140,20,0.9571,1.06,False
140,30,0.9286,0.97,False
140,40,0.9000,1.02,False
140,50,0.8571,0.93,True
10000,0,1.0,17.47,False
10000,10,1.0,22.18,False
...
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [✔] Repeatability / [ ] Reproducibility / [ ] Belum keduanya

**Komponen yang belum terdokumentasi:**
> Aspek **reproducibility** masih belum sepenuhnya tercapai karena dua komponen berikut belum terdokumentasi secara publik: (1) Data sampel asli 140 siswa tidak dapat dipublikasikan karena alasan privasi — diperlukan dataset sintetis pengganti yang representatif sebagai data publik untuk riset lanjutan (sudah diatasi sebagian dengan `generate_sample_data.py`); (2) Prosedur kalibrasi panel 3 pakar (pengisian nilai perbandingan berpasangan AHP) belum didokumentasikan dalam bentuk protokol terstruktur, sehingga peneliti lain belum bisa mereplikasi tahap pembobotan awal secara independen tanpa panduan dari peneliti asli.
