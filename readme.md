# Prediksi Kelulusan Mahasiswa Menggunakan Machine Learning

## Studi Kasus

Proyek ini merupakan implementasi Machine Learning untuk memprediksi status kelulusan mahasiswa berdasarkan Indeks Prestasi Kumulatif (IPK) dan persentase kehadiran. Algoritma yang digunakan adalah **Decision Tree Classifier**, yaitu algoritma klasifikasi yang mempelajari pola dari data untuk menghasilkan prediksi berdasarkan kondisi tertentu.

Program dikembangkan menggunakan Python dengan library Pandas untuk pengolahan data dan Scikit-learn untuk membangun, melatih, serta mengevaluasi model Machine Learning.

Pengguna dapat memasukkan nilai IPK dan persentase kehadiran mahasiswa untuk memperoleh prediksi status kelulusan berupa **Lulus** atau **Belum**. Dataset yang digunakan merupakan data simulasi untuk keperluan pembelajaran, bukan data kelulusan mahasiswa yang sebenarnya.

## Teknologi yang Digunakan

- Python
- Pandas
- Scikit-learn
- Visual Studio Code
- GitHub

## Algoritma

### Decision Tree Classifier

Decision Tree merupakan algoritma Machine Learning yang menggunakan struktur menyerupai pohon keputusan untuk melakukan klasifikasi.

Dalam proyek ini, algoritma Decision Tree mempelajari hubungan antara IPK, persentase kehadiran, dan status kelulusan mahasiswa berdasarkan data pelatihan.

Parameter yang digunakan:

- `random_state=42`: menjaga konsistensi hasil model.
- `test_size=0.25`: menggunakan 25% data untuk pengujian dan 75% untuk pelatihan.
- `stratify=y`: menjaga proporsi kelas pada pembagian data latih dan data uji.

## Dataset

Dataset disimpan dalam file `dataset.csv` dan berisi 12 data simulasi mahasiswa.

| Atribut | Keterangan |
|---|---|
| `ipk` | Indeks Prestasi Kumulatif mahasiswa |
| `kehadiran` | Persentase kehadiran mahasiswa |
| `status` | Status kelulusan mahasiswa |

### Contoh Dataset

```csv
ipk,kehadiran,status
3.8,95,Lulus
3.5,90,Lulus
3.2,85,Lulus
2.9,80,Lulus
2.7,75,Belum
2.5,70,Belum
2.3,60,Belum
2.0,55,Belum
3.6,92,Lulus
2.4,65,Belum
3.4,88,Lulus
2.6,72,Belum
```

**Catatan:** Dataset bersifat simulasi dan berukuran kecil. Hasil prediksi bergantung pada pola yang dipelajari model dari data tersebut.

## Alur Kerja Program

1. Membaca dataset dari file `dataset.csv`.
2. Menentukan IPK dan kehadiran sebagai atribut input.
3. Menentukan status sebagai target klasifikasi.
4. Membagi dataset menjadi data latih dan data uji.
5. Melatih model menggunakan algoritma Decision Tree.
6. Menguji model dan menghitung akurasi prediksi.
7. Meminta pengguna memasukkan IPK dan persentase kehadiran.
8. Menampilkan hasil prediksi kelulusan mahasiswa.

## Struktur Folder

```text
prediksi-kelulusan/
├── dataset.csv
├── main.py
└── README.md
```

Keterangan:
- `dataset.csv`: menyimpan data simulasi mahasiswa.
- `main.py`: berisi kode program Machine Learning.
- `README.md`: dokumentasi proyek.


## Evaluasi Model

Evaluasi model menggunakan metrik **Accuracy Score**, yaitu persentase prediksi yang benar dibandingkan dengan seluruh data pengujian.

Rumus akurasi:

Akurasi = (Jumlah Prediksi Benar / Jumlah Seluruh Data Uji) × 100%

Akurasi digunakan untuk mengetahui seberapa baik model memprediksi data uji. Namun, karena dataset hanya terdiri dari 12 data, hasil evaluasi belum cukup untuk menunjukkan kemampuan model pada data mahasiswa yang lebih beragam.

## Kelebihan Proyek

- Menggunakan algoritma klasifikasi yang mudah dipahami.
- Memiliki alur Machine Learning yang sederhana.
- Mendukung input data mahasiswa secara interaktif.
- Menampilkan hasil evaluasi model dalam bentuk persentase.
- Dapat dikembangkan menggunakan dataset yang lebih besar.

## Kesimpulan

Proyek ini menerapkan algoritma Decision Tree Classifier untuk memprediksi status kelulusan mahasiswa berdasarkan IPK dan persentase kehadiran. Model dilatih menggunakan data simulasi, dievaluasi menggunakan akurasi, dan digunakan untuk menghasilkan prediksi berdasarkan input baru.

Proyek ini menjadi sarana pembelajaran mengenai tahapan dasar Machine Learning, mulai dari pengolahan dataset, pelatihan model, evaluasi, hingga penerapan prediksi.
