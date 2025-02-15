#---------- RESTORE ----------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi
from .delete import recycle_bin

def restore_data():
    while True:  # Loop untuk merestore data berulang kali
        if not recycle_bin:
            print("Recycle Bin kosong.")
            return

        print("\n=== Data di Recycle Bin ===")
        print(tabulate(recycle_bin, headers="keys", tablefmt="grid"))
        id_restore = input("Masukkan ID data yang ingin direstore: ").strip().upper()
        item = next((item for item in recycle_bin if item["ID"] == id_restore), None)

        if item:
            from main import data_keuangan
            data_keuangan.append(recycle_bin.pop(recycle_bin.index(item)))
            print("Data berhasil direstore!")
        else:
            print("ID data tidak ditemukan di Recycle Bin.")

        # Konfirmasi apakah ingin merestore data lagi
        if not konfirmasi("Apakah Anda ingin merestore data lagi? (ya/tidak): "):
            break  # Kembali ke menu utama jika tidak ingin merestore lagi
