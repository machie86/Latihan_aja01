#------------ DELETE ------------

from tabulate import tabulate 

from .validasi import input_string, input_angka, generate_id, konfirmasi
from .read import tampilkan_data

# Recycle bin untuk menyimpan data yang dihapus sementara sebelum benar-benar dihapus permanen, berbentuk list
recycle_bin = []

# Fungsi menghapus data (delete)
def delete_data():
    while True:  # Loop, memungkinkan pengguna untuk menghapus data berulang kali hingga memilih untuk berhenti.
        from main import data_keuangan
        if not data_keuangan:
            print("Belum ada data yang tersedia.")
            return

        tampilkan_data()
        id_hapus = input("Masukkan ID data yang ingin dihapus: ").strip().upper() 
        item = next((item for item in data_keuangan if item["ID"] == id_hapus), None)

        if item:
            recycle_bin.append(data_keuangan.pop(data_keuangan.index(item))) #data_keuangan.index(item), untuk mencari indeks item dalam data_keuangan.
            print("Data dipindahkan ke Recycle Bin!")                       #data_keuangan.pop(...), untuk menghapus item dari data_keuangan berdasarkan indeks.
                                                                            #recycle_bin.append(...), untuk menambahkan item yang dihapus ke recycle_bin.
        else:                                                               
            print("ID data tidak ditemukan.")

        # Konfirmasi apakah ingin menghapus data lagi
        if not konfirmasi("Apakah Anda ingin menghapus data lagi? (ya/tidak): "):
            break  # Kembali ke menu utama jika tidak ingin menghapus lagi