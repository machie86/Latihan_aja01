#---------- RESTORE ----------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi
from .delete import recycle_bin

# Fungsi memulihkan data (restore)
def restore_data():
    while True:  # Loop untuk merestore data berulang kali
        if not recycle_bin:
            print("Recycle Bin kosong.")
            return

        print("\n=== Data di Recycle Bin ===")
        print(tabulate(recycle_bin, headers="keys", tablefmt="grid")) #headers='keys', menggunakan key dari dictionary sebagai header tabel.
        id_restore = input("Masukkan ID data yang ingin direstore: ").strip().upper()
        item = next((item for item in recycle_bin if item["ID"] == id_restore), None)

        if item:
            from main import data_keuangan
            data_keuangan.append(recycle_bin.pop(recycle_bin.index(item))) #recycle_bin.index(item), mencari indeks item dalam recycle_bin. #ecycle_bin.pop, Menghapus item dari recycle_bin berdasarkan indeks.
            print("Data berhasil direstore!")           #data_keuangan.append, menambahkan item yang dihapus dari recycle_bin ke data_keuangan.
        else:
            print("ID data tidak ditemukan di Recycle Bin.")

        # Konfirmasi apakah ingin merestore data lagi
        if not konfirmasi("Apakah Anda ingin merestore data lagi? (ya/tidak): "):
            break  # Kembali ke menu utama jika tidak ingin merestore lagi
