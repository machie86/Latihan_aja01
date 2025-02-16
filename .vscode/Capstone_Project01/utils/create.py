#------------CREATE------------

from tabulate import tabulate 
from datetime import datetime 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi, hitung_umur, hitung_status_keuangan
    # .validasi, untuk mengimpor fungsi-fungsi validasi dari modul validasi yang berada di direktori yang sama

# fungsi menambah data (add)
def tambah_data():
    while True: # loop while True, program akan terus meminta input hingga pengguna memilih untuk berhenti.
        print("\n=== Tambah Data Baru ===")
        nama = input_string("Masukkan nama: ")

        # Validasi tahun lahir
        tahun_berjalan = datetime.now().year
        while True:
            tahun_lahir = input_angka("Masukkan tahun lahir (format YYYY): ", min_value=1900, max_value=tahun_berjalan)
            umur = hitung_umur(tahun_lahir)
            if 18 <= umur <= 65:
                break # break, jika umur antara 18 hingga 65 tahun, loop berhenti. 
                            #Jika tidak, program akan meminta input tahun lahir lagi.
            print("Umur harus antara 18 hingga 65 tahun. Silakan coba lagi.")

        asal = input_string("Masukkan asal kota: ")

        # Validasi pendapatan minimal Rp 1.000.000
        pendapatan = input_angka("Masukkan pendapatan: ", min_value=1000000)

        # Validasi pengeluaran minimal Rp 1.000.000
        pengeluaran = input_angka("Masukkan pengeluaran: ", min_value=1000000)

        status, tabungan = hitung_status_keuangan(pendapatan, pengeluaran)

        from main import data_keuangan # untuk mengimport variabel data_keuangan dari modul main.py (global)
        data_keuangan.append({
            "ID": generate_id(nama),
            "nama": nama,
            "umur": umur,
            "asal": asal,
            "pendapatan": pendapatan,
            "pengeluaran": pengeluaran,
            "tabungan": tabungan,
            "status keuangan": status
        }) # append, menambah data baru ke dalam list data_keuangan
        print("Data berhasil ditambahkan!\n")

        # Konfirmasi apakah ingin menambah data lagi
        if not konfirmasi("Apakah Anda ingin menambah data lagi? (ya/tidak): "):
            break # break di akhir loop while True, untuk menghentikan loop ketika pengguna memilih untuk tidak menambah data lagi. 