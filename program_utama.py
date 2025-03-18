from materi import *
from kuis import *
from evaluasi import *


def fitur1():
    print("""
========================
PROGRAM FISIKA KELAS VII
========================
      Menu Program
------------------------
1. Besaran
2. Zat
3. Kalor
4. Evaluasi
------------------------""")

def fitur2():
    print("""
~~~~~~~~~~~~~~
1. Materi    
2. Kuis
~~~~~~~~~~~~~~""")


menu = "ya"
while menu == "ya":
    fitur1()
    pilih_menu = int(input("Masukkan pilihan anda (1/2/3/4) : "))
    if pilih_menu == 1:
        fitur2()
        pilih_menu_besaran = int(input("Masukkan pilihan anda (1/2) : "))
        if pilih_menu_besaran == 1:
            materi_besaran()
        elif pilih_menu_besaran == 2:
            kuis_besaran()
        else:
            print("Pilihan anda tidak valid")
    elif pilih_menu == 2:
        fitur2()
        pilih_menu_zat = int(input("Masukkan pilihan anda (1/2) : "))
        if pilih_menu_zat == 1:
            materi_zat()
        elif pilih_menu_zat == 2:
            kuis_zat()
        else:
            print("Pilihan anda tidak valid")
    elif pilih_menu == 3:
        fitur2()
        pilih_menu_kalor = int(input("Masukkan pilihan anda (1/2) : "))
        if pilih_menu_kalor == 1:
            materi_kalor()
        elif pilih_menu_kalor == 2:
            kuis_kalor()
        else:
            print("Pilihan anda tidak valid")
    elif pilih_menu == 4:
        print("\n~Selamat Mengerjakan 😊~")
        evaluasi()
    else:
        print("Pilihan anda tidak valid")
    menu = str(input("Kembali ke menu utama? (ya/tidak) : ")).lower()
    if menu != "ya":
        print("\nProgram Selesai\nTerima kasih telah memakai program kami😊")

    break
