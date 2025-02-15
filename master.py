from tabulate import tabulate
from datetime import datetime
import random
from utils import input_angka
# REPORT
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

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
    {"ID": "AT741", "nama": "Adit Taufik", "umur": 31, "asal": "Makassar", "pendapatan": 7500000, "pengeluaran": 5500000, "tabungan": 2000000, "status keuangan": "aman"}
]

# Recycle bin untuk data yang dihapus
recycle_bin = []

# Fungsi utilitas
def input_angka(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Input harus antara {min_value} dan {max_value}." if min_value and max_value else f"Input minimal {min_value}." if min_value else f"Input maksimal {max_value}.")
            else:
                return value
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def input_string(prompt):
    while True:
        value = input(prompt).strip()
        if value and all(char.isalpha() or char.isspace() for char in value):
            return value.title()
        print("Input hanya boleh berupa huruf dan spasi. Silakan coba lagi.")

def konfirmasi(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["ya", "y", "tidak", "t"]:
            return value in ["ya", "y"]
        print("Input tidak valid. Masukkan 'ya' atau 'tidak'.")

def generate_id(nama, existing_ids=set()):
    while True:
        inisial = ''.join([word[0] for word in nama.split()[:2]]).upper()
        angka = random.randint(100, 999)
        new_id = f"{inisial}{angka}"
        
        if new_id not in existing_ids:
            existing_ids.add(new_id)
            return new_id

def hitung_status_keuangan(pendapatan, pengeluaran):
    tabungan = pendapatan - pengeluaran
    return "aman" if tabungan >= 0.2 * pendapatan else "tidak aman", tabungan

def hitung_umur(tahun_lahir):
    tahun_berjalan = datetime.now().year
    return tahun_berjalan - tahun_lahir

# Fungsi utama
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

def tampilkan_data(filter_func=None):
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

def update_data():
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

def delete_data():
    while True:  # Loop untuk menghapus data berulang kali
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
            data_keuangan.append(recycle_bin.pop(recycle_bin.index(item)))
            print("Data berhasil direstore!")
        else:
            print("ID data tidak ditemukan di Recycle Bin.")

        # Konfirmasi apakah ingin merestore data lagi
        if not konfirmasi("Apakah Anda ingin merestore data lagi? (ya/tidak): "):
            break  # Kembali ke menu utama jika tidak ingin merestore lagi


def report_dashboard():
    if not data_keuangan:
        print("Belum ada data yang tersedia.\n")
        return

    console = Console()

    # Data untuk visualisasi
    nama = [item["nama"] for item in data_keuangan]
    pendapatan = [item["pendapatan"] for item in data_keuangan]
    pengeluaran = [item["pengeluaran"] for item in data_keuangan]
    tabungan = [item["tabungan"] for item in data_keuangan]
    status_keuangan = [item["status keuangan"] for item in data_keuangan]
    asal = [item["asal"] for item in data_keuangan]
    umur = [item["umur"] for item in data_keuangan]

    # Hitung jumlah status keuangan
    jumlah_aman = status_keuangan.count("aman")
    jumlah_tidak_aman = status_keuangan.count("tidak aman")

    # 1. Ringkasan Status Keuangan
    console.print(Panel.fit("[bold cyan]Ringkasan Status Keuangan[/bold cyan]", padding=(1, 2)))
    status_table = Table(show_header=True, header_style="bold magenta")
    status_table.add_column("Status", justify="center")
    status_table.add_column("Jumlah", justify="center")
    status_table.add_row("Aman", str(jumlah_aman))
    status_table.add_row("Tidak Aman", str(jumlah_tidak_aman))
    console.print(status_table)

    # 2. Ringkasan Minimal dan Maksimal
    pendapatan_min = min(pendapatan)
    pendapatan_max = max(pendapatan)
    pengeluaran_min = min(pengeluaran)
    pengeluaran_max = max(pengeluaran)
    tabungan_min = min(tabungan)
    tabungan_max = max(tabungan)

    console.print(Panel.fit("[bold cyan]Ringkasan Minimal dan Maksimal[/bold cyan]", padding=(1, 2)))
    min_max_table = Table(show_header=True, header_style="bold magenta")
    min_max_table.add_column("Variabel", justify="left")
    min_max_table.add_column("Minimal (Rp)", justify="right")
    min_max_table.add_column("Maksimal (Rp)", justify="right")
    min_max_table.add_row("Pendapatan", f"{pendapatan_min:,}", f"{pendapatan_max:,}")
    min_max_table.add_row("Pengeluaran", f"{pengeluaran_min:,}", f"{pengeluaran_max:,}")
    min_max_table.add_row("Tabungan", f"{tabungan_min:,}", f"{tabungan_max:,}")
    console.print(min_max_table)

    # 3. Distribusi Asal Kota
    console.print(Panel.fit("[bold cyan]Distribusi Asal Kota[/bold cyan]", padding=(1, 2)))
    asal_kota = {}
    for kota in asal:
        asal_kota[kota] = asal_kota.get(kota, 0) + 1

    kota_table = Table(show_header=True, header_style="bold magenta")
    kota_table.add_column("Asal Kota", justify="left")
    kota_table.add_column("Jumlah", justify="right")
    for kota, jumlah in asal_kota.items():
        kota_table.add_row(kota, str(jumlah))
    console.print(kota_table)

    # 4. Hubungan Usia dan Tabungan
    console.print(Panel.fit("[bold cyan]Hubungan Usia dan Tabungan[/bold cyan]", padding=(1, 2)))
    usia_tabungan_table = Table(show_header=True, header_style="bold magenta")
    usia_tabungan_table.add_column("Nama", justify="left")
    usia_tabungan_table.add_column("Usia", justify="right")
    usia_tabungan_table.add_column("Tabungan (Rp)", justify="right")
    for i in range(len(nama)):
        usia_tabungan_table.add_row(nama[i], str(umur[i]), f"{tabungan[i]:,}")
    console.print(usia_tabungan_table)

# Menu utama
def main():
    while True:
        print("\n=== Aplikasi Personal Finance ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Update Data") 
        print("4. Delete Data")
        print("5. Restore Data")
        print("6. Tampilkan Dashboard")
        print("7. Keluar")
        pilihan = input("Pilih menu (1/2/3/4/5/6/7): ").strip()

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
            if konfirmasi("Apakah Anda ingin memfilter data? (ya/tidak): "):
                filter_data_menu()
        elif pilihan == "3":
            update_data()
        elif pilihan == "4":
            delete_data()
        elif pilihan == "5":
            restore_data()
        elif pilihan == "6":
            report_dashboard()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-7.")

# Jalankan program
if __name__ == "__main__":
    main()