#------------VALIDASI---------------

from tabulate import tabulate # untuk menampilkan dalam bentuk tabel
from datetime import datetime # 
import random


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