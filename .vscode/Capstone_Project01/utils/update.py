#---------- UPDATE -------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi, hitung_umur, hitung_status_keuangan
from .read import tampilkan_data

def update_data():
    from main import data_keuangan
    if not data_keuangan:
        print("Belum ada data yang tersedia.")
        return

    while True:
        tampilkan_data()
        id_update = input("Masukkan ID data yang ingin diupdate: ").strip().upper()
        item = next((item for item in data_keuangan if item["ID"] == id_update), None)

        if not item:
            print("ID data tidak ditemukan.")
            return
        
        print(f"Data dengan ID {id_update} ditemukan.")
        while True:
            print("\nPilih data yang ingin diupdate:")
            print("1. Nama")
            print("2. Umur")
            print("3. Asal")
            print("4. Pendapatan")
            print("5. Pengeluaran")
            print("6. Kembali ke Menu Utama")
            pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ").strip()

            if pilihan == "1":
                item["nama"] = input_string("Masukkan nama baru: ")
            elif pilihan == "2":
                tahun_berjalan = datetime.now().year
                while True:
                    tahun_lahir = input_angka("Masukkan tahun lahir baru (format YYYY): ", min_value=1900, max_value=tahun_berjalan)
                    umur = hitung_umur(tahun_lahir)
                    if 18 <= umur <= 65:
                        item["umur"] = umur
                        break
                    print("Umur harus antara 18 hingga 65 tahun. Silakan coba lagi.")
            elif pilihan == "3":
                item["asal"] = input_string("Masukkan asal baru: ")
            elif pilihan == "4":
                item["pendapatan"] = input_angka("Masukkan pendapatan baru: ", min_value=1000000)
            elif pilihan == "5":
                item["pengeluaran"] = input_angka("Masukkan pengeluaran baru: ", min_value=1000000)
            elif pilihan == "6":
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

            item["status keuangan"], item["tabungan"] = hitung_status_keuangan(item["pendapatan"], item["pengeluaran"])
            print("Data berhasil diupdate!\n")

        tampilkan_data(lambda x: x["ID"] == id_update)  # Tampilkan data yang baru diupdate

        # Konfirmasi apakah ingin mengupdate data lagi
        if not konfirmasi("Apakah Anda ingin mengupdate data lainnya? (ya/tidak): "):
            break
