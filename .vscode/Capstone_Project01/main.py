#-------------MAIN----------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random


from utils import create as cr, read as re, update as up, delete as de, restore as rs, dashboard as db, validasi as va

# List untuk menyimpan data
data_keuangan = [
    {"ID": "AB123", "nama": "Andi Budi", "umur": 25, "asal": "Jakarta", "pendapatan": 5000000, "pengeluaran": 3000000, "tabungan": 2000000, "status keuangan": "aman"},
    {"ID": "RS456", "nama": "Rina Sari", "umur": 30, "asal": "Bandung", "pendapatan": 7000000, "pengeluaran": 4000000, "tabungan": 3000000, "status keuangan": "aman"},
    {"ID": "TP789", "nama": "Tono Purnomo", "umur": 35, "asal": "Surabaya", "pendapatan": 6000000, "pengeluaran": 5000000, "tabungan": 1000000, "status keuangan": "tidak aman"},
    {"ID": "MW321", "nama": "Maya Wijaya", "umur": 28, "asal": "Semarang", "pendapatan": 8000000, "pengeluaran": 6000000, "tabungan": 2000000, "status keuangan": "aman"},
    {"ID": "AD654", "nama": "Adi Darma", "umur": 40, "asal": "Yogyakarta", "pendapatan": 5500000, "pengeluaran": 4500000, "tabungan": 1000000, "status keuangan": "tidak aman"},
    {"ID": "SR987", "nama": "Sari Rahma", "umur": 23, "asal": "Malang", "pendapatan": 4800000, "pengeluaran": 3500000, "tabungan": 1300000, "status keuangan": "aman"},
    {"ID": "BT654", "nama": "Budi Tarmizi", "umur": 29, "asal": "Denpasar", "pendapatan": 7200000, "pengeluaran": 5200000, "tabungan": 2000000, "status keuangan": "aman"},
    {"ID": "RM852", "nama": "Rahmat Mulyadi", "umur": 33, "asal": "Medan", "pendapatan": 6500000, "pengeluaran": 4700000, "tabungan": 1800000, "status keuangan": "aman"},
    {"ID": "YS963", "nama": "Yuni Sari", "umur": 27, "asal": "Padang", "pendapatan": 5900000, "pengeluaran": 5100000, "tabungan": 800000, "status keuangan": "tidak aman"},
    {"ID": "AT741", "nama": "Adit Taufik", "umur": 31, "asal": "Makassar", "pendapatan": 7500000, "pengeluaran": 5500000, "tabungan": 2000000, "status keuangan": "aman"}]

# Menu utama
def main():
    while True:
        print("\n=== Aplikasi Financial Check-Up ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data") 
        print("4. Delete Data")
        print("5. Restore Data")
        print("6. Tampilkan Dashboard")
        print("7. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ").strip()

        if pilihan == "1":
            cr.tambah_data()
        elif pilihan == "2":
            re.tampilkan_data()
            if va.konfirmasi("Apakah Anda ingin memfilter data? (ya/tidak): "):
                re.filter_data_menu()
        elif pilihan == "3":
            up.update_data()
        elif pilihan == "4":
            de.delete_data()
        elif pilihan == "5":
            rs.restore_data()
        elif pilihan == "6":
            db.report_dashboard()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-7.")

# Jalankan program
if __name__ == "__main__":
    main()