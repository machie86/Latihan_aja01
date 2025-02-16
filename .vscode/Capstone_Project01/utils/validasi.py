#------------VALIDASI---------------

from tabulate import tabulate # untuk menampilkan data dalam bentuk tabel
from datetime import datetime # untuk bekerja dengan tanggal dan waktu
import random # untuk menghasilkan nilai acak (random)
import re # untuk operasi regex (regular expression)

# fungsi input_angka
def input_angka(prompt, min_value=None, max_value=None): 
    while True:
        try: # try-except untuk handling error, program dapat memberikan pesan kesalahan yang spesifik kepada pengguna sehingga mudah untuk memperbaiki error
            value = int(input(prompt)) #min_value max_valur, untuk memastikan input berupa digit dan memiliki nilai tertentu (min, max)
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Input harus antara {min_value} dan {max_value}." if min_value and max_value else f"Input minimal {min_value}." if min_value else f"Input maksimal {max_value}.")
            else:
                return value
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

# fungsi input_string
def input_string(prompt):
    while True:
        value = input(prompt).strip() # strip, untuk menghilangkan spasi di awal dan akhir input
        # Regex untuk memeriksa apakah input hanya mengandung huruf dan spasi
        if re.match(r'^[A-Za-z\s]+$', value): # regex, untuk efisiensi penulisan syntax (lebih sederhana)
            return value.title() # title, untuk mengubah input menjadi judul (huruf pertama kapital)
        print("Input hanya boleh berupa huruf dan spasi. Silakan coba lagi.")

#fungsi konfirmasi
def konfirmasi(prompt):
    while True:
        value = input(prompt).strip().lower() # lower, untuk mengubah input menjadi lowercase untuk memudahkan validasi.
        if value in ["ya", "y", "tidak", "t"]:
            return value in ["ya", "y"] # return, menghentikan eksekusi loop dan mengembalikan nilai ke pemanggil fungsi.
                                        # Jika menggunakan break, kita perlu menyimpan hasil validasi dalam sebuah variabel sementara, lalu mengembalikan nilai tersebut setelah loop selesai.
        print("Input tidak valid. Masukkan 'ya' atau 'tidak'.")

# fungsi generate_id, untuk mendapatkan nilai acak atau random dari inisial nama dan no unique
def generate_id(nama, existing_ids=set()): # existing_ids, untuk membuat koleksi unik yang tidak mengizinkan duplikat.
                                            #set yang berisi ID yang sudah ada (opsional, default adalah set kosong).
    while True:
        inisial = ''.join([word[0] for word in nama.split()[:2]]).upper() # join, Menggabungkan karakter pertama dari dua kata pertama dalam nama pengguna untuk membuat inisial.
        angka = random.randint(100, 999) # random.rantind (100,999), fungsi untuk menghasilkan angka acak antara 100 dan 999 (angka 3 digit).
        new_id = f"{inisial}{angka}" # new_id, untuk menghasilkan ID unik berdasarkan inisial nama pengguna dan angka 3 digit setelahnya
        
        if new_id not in existing_ids: # jika ID unik sudah tersedia (terjadi duplikasi), dengan fungsi loop 'return' ini adalah untuk membuat ID baru 
            existing_ids.add(new_id)
            return new_id
        
# menggabungkan cara menghitung tabungan dan membuat fungsi status keuangan
def hitung_status_keuangan(pendapatan, pengeluaran): 
    tabungan = pendapatan - pengeluaran
    return "aman" if tabungan >= 0.2 * pendapatan else "tidak aman", tabungan

# fungsi menghitung umur dari tahun lahir
def hitung_umur(tahun_lahir):
    tahun_berjalan = datetime.now().year # datetime, untuk menjalankan tahun berjalan
    return tahun_berjalan - tahun_lahir