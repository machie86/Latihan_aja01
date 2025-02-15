#----------- READ --------------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi

def tampilkan_data(filter_func=None):
    from main import data_keuangan
    if not data_keuangan:
        print("Belum ada data yang tersedia.\n")
        return

    data_tampil = list(filter(filter_func, data_keuangan)) if filter_func else data_keuangan
    headers = ["ID", "Nama", "Umur", "Asal", "Pendapatan", "Pengeluaran", "Tabungan", "Status Keuangan"]
    rows = [[item["ID"], item["nama"], item["umur"], item["asal"], f"Rp {item['pendapatan']:,}", f"Rp {item['pengeluaran']:,}", f"Rp {item['tabungan']:,}", item["status keuangan"]] for item in data_tampil]
    print("\n=== Data Keuangan ===")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print()

def filter_data_menu():
    from main import data_keuangan
    data_tampil = data_keuangan.copy()

    while True:
        print("\nPilih kriteria filter:")
        print("1. Asal Kota")
        print("2. Rentang Usia")
        print("3. Rentang Pendapatan")
        print("4. Rentang Pengeluaran")
        print("5. Status Keuangan")
        print("6. Selesai Filter dan Tampilkan Data")
        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ").strip()

        if pilihan == "1":
            asal = input_string("Masukkan asal kota: ")
            data_tampil = [item for item in data_tampil if item["asal"].lower() == asal.lower()]
        elif pilihan == "2":
            usia_min = input_angka("Masukkan usia minimal: ")
            usia_max = input_angka("Masukkan usia maksimal: ")
            data_tampil = [item for item in data_tampil if usia_min <= item["umur"] <= usia_max]
        elif pilihan == "3":
            pendapatan_min = input_angka("Masukkan pendapatan minimal: ")
            pendapatan_max = input_angka("Masukkan pendapatan maksimal: ")
            data_tampil = [item for item in data_tampil if pendapatan_min <= item["pendapatan"] <= pendapatan_max]
        elif pilihan == "4":
            pengeluaran_min = input_angka("Masukkan pengeluaran minimal: ")
            pengeluaran_max = input_angka("Masukkan pengeluaran maksimal: ")
            data_tampil = [item for item in data_tampil if pengeluaran_min <= item["pengeluaran"] <= pengeluaran_max]
        elif pilihan == "5":
            status = input("Masukkan status keuangan (aman/tidak aman): ").strip().lower()
            data_tampil = [item for item in data_tampil if item["status keuangan"].lower() == status]
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        if not data_tampil:
            print("Tidak ada data yang sesuai dengan kriteria filter.")
            return

        if not konfirmasi("Apakah Anda ingin menambahkan filter lainnya? (ya/tidak): "):
            break

    tampilkan_data(lambda item: item in data_tampil)