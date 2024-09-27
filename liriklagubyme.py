import time
import sys

def print_lirik():
    delays = [1.5, 1.5, 2, 2,2]  # Waktu delay untuk tiap baris lirik
    # Made with love by Raka!
     #Instagram: @rakafpp_
     #Email: pramuditaraka448@gmail.com
     
 # Thanks to all <3 
    

    lirik = [
        ("Siapa yang jadi bahu saat kau perlu", 5),
        ("Menangis terluka di payung rindu", 5),
        ("Apa ada yang bisa diambil peranku", 5),
        ("Menjaga dirimu,yang kini tak ditanganku",5)
        # Tambahkan baris lirik lainnya di sini
    ]

    for i, (line, char) in enumerate(lirik):  # Perbaikan loop for
        for ch in line:
            print(ch, end='')  # Cetak karakter tanpa newline
            sys.stdout.flush()  # Memastikan output langsung ditampilkan
            time.sleep(delays[i] * 0.1)  # Sesuaikan kecepatan dengan delay
        print('')  # Cetak newline setelah tiap baris lirik

print_lirik()
