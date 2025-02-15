#----------- DASHBOARD ---------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random

from .validasi import input_string, input_angka, generate_id, konfirmasi, hitung_umur, hitung_status_keuangan

# 
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def report_dashboard():
    from main import data_keuangan
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