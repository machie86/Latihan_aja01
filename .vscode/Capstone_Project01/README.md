# Aplikasi Financial Check-Up

Aplikasi ini adalah sebuah program Python sederhana untuk mengelola data keuangan pribadi dan mengetahui kondisi keuangan. Program ini memungkinkan pengguna untuk menambah, menampilkan, mengupdate, menghapus, dan merestore data keuangan. Selain itu, aplikasi ini juga menyediakan dashboard untuk memvisualisasikan data keuangan.

## Fitur Utama
1. **Tambah Data**: Menambahkan data keuangan baru.
2. **Tampilkan Data**: Menampilkan data keuangan dalam bentuk tabel.
3. **Update Data**: Memperbarui data keuangan yang sudah ada.
4. **Delete Data**: Menghapus data keuangan dan memindahkannya ke Recycle Bin.
5. **Restore Data**: Mengembalikan data yang telah dihapus dari Recycle Bin.
6. **Dashboard**: Menampilkan ringkasan dan visualisasi data keuangan.

## Cara Menggunakan
1. **Menjalankan Program**:
   - Pastikan Python sudah terinstall di sistem Anda.
   - Jalankan program dengan perintah:
     ```bash
     python nama_file.py
     ```
   - Ganti `nama_file.py` dengan nama file Python Anda.

2. **Menu Utama**:
   - Setelah program dijalankan, Anda akan melihat menu utama dengan pilihan:
     ```
     === Aplikasi Financial Check-Up ===
     1. Tambah Data
     2. Tampilkan Data
     3. Update Data
     4. Delete Data
     5. Restore Data
     6. Tampilkan Dashboard
     7. Keluar
     ```
   - Pilih menu dengan memasukkan angka yang sesuai.

3. **Tambah Data**:
   - Pilih menu `1` untuk menambahkan data baru.
   - Masukkan informasi seperti nama, tahun lahir, asal kota, pendapatan, dan pengeluaran.

4. **Tampilkan Data**:
   - Pilih menu `2` untuk menampilkan semua data keuangan.
   - Anda juga dapat memfilter data berdasarkan kriteria tertentu.

5. **Update Data**:
   - Pilih menu `3` untuk memperbarui data yang sudah ada.
   - Masukkan ID data yang ingin diupdate dan pilih informasi yang akan diubah.

6. **Delete Data**:
   - Pilih menu `4` untuk menghapus data.
   - Data yang dihapus akan dipindahkan ke Recycle Bin.

7. **Restore Data**:
   - Pilih menu `5` untuk mengembalikan data yang telah dihapus dari Recycle Bin.

8. **Dashboard**:
   - Pilih menu `6` untuk melihat ringkasan dan visualisasi data keuangan.

## Persyaratan
- Python 3.x
- Library yang diperlukan:
  - `tabulate`: Untuk menampilkan data dalam bentuk tabel.
  - `rich`: Untuk visualisasi dashboard.
  - Install library dengan perintah:
    ```bash
    pip install tabulate rich
    ```

## Struktur Data
Data keuangan disimpan dalam bentuk list of dictionaries dengan struktur berikut:
```python
data_keuangan = [
    {
        "ID": "AB123",
        "nama": "Andi Budi",
        "umur": 25,
        "asal": "Jakarta",
        "pendapatan": 5000000,
        "pengeluaran": 3000000,
        "tabungan": 2000000,
        "status keuangan": "aman"
    },
    ...
]

Kontribusi
Jika Anda ingin berkontribusi pada proyek ini, silakan buka issue atau pull request di repository GitHub.

Lisensi
Proyek ini dilisensikan di bawah 'Asiyatul Mahfudloh'