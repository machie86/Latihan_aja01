#------------CREATE------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi, hitung_umur, hitung_status_keuangan

def tambah_data():
    while True:
        print("\n=== Tambah Data Baru ===")
        nama = input_string("Masukkan nama: ")

        # Validasi tahun lahir
        tahun_berjalan = datetime.now().year
        while True:
            tahun_lahir = input_angka("Masukkan tahun lahir (format YYYY): ", min_value=1900, max_value=tahun_berjalan)
            umur = hitung_umur(tahun_lahir)
            if 18 <= umur <= 65:
                break
            print("Umur harus antara 18 hingga 65 tahun. Silakan coba lagi.")

        asal = input_string("Masukkan asal kota: ")

        # Validasi pendapatan minimal Rp 1.000.000
        pendapatan = input_angka("Masukkan pendapatan: ", min_value=1000000)

        # Validasi pengeluaran minimal Rp 1.000.000
        pengeluaran = input_angka("Masukkan pengeluaran: ", min_value=1000000)

        status, tabungan = hitung_status_keuangan(pendapatan, pengeluaran)

        from main import data_keuangan
        data_keuangan.append({
            "ID": generate_id(nama),
            "nama": nama,
            "umur": umur,
            "asal": asal,
            "pendapatan": pendapatan,
            "pengeluaran": pengeluaran,
            "tabungan": tabungan,
            "status keuangan": status
        })
        print("Data berhasil ditambahkan!\n")

        # Konfirmasi apakah ingin menambah data lagi
        if not konfirmasi("Apakah Anda ingin menambah data lagi? (ya/tidak): "):
            break