#------------ DELETE ------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi
from .read import tampilkan_data

# Recycle bin untuk data yang dihapus
recycle_bin = []

def delete_data():
    while True:  # Loop untuk menghapus data berulang kali
        from main import data_keuangan
        if not data_keuangan:
            print("Belum ada data yang tersedia.")
            return

        tampilkan_data()
        id_hapus = input("Masukkan ID data yang ingin dihapus: ").strip().upper()
        item = next((item for item in data_keuangan if item["ID"] == id_hapus), None)

        if item:
            recycle_bin.append(data_keuangan.pop(data_keuangan.index(item)))
            print("Data dipindahkan ke Recycle Bin!")
        else:
            print("ID data tidak ditemukan.")

        # Konfirmasi apakah ingin menghapus data lagi
        if not konfirmasi("Apakah Anda ingin menghapus data lagi? (ya/tidak): "):
            break  # Kembali ke menu utama jika tidak ingin menghapus lagi