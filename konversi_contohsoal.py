def konversi_panjang():
    ulang = "ya"
    while ulang == "ya":
        satuan1 = str(input("Satuan yang dikonversi (km/hm/dam/m/dm/cm/mm) : ")).lower()
        satuan2 = str(input("Hasil konversi (km/hm/dam/m/dm/cm/mm) : ")).lower()
        angka = float(input("Masukkan angka yang ingin dikonversi : "))
        list_satuan = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

        if satuan1 not in list_satuan or satuan2 not in list_satuan:
            print("\nMasukkan satuan sesuai pilihan yang tertera!")
        else:
            for i in range(7):
                if i == list_satuan.index(satuan1):
                    if list_satuan.index(satuan1) > list_satuan.index(satuan2):
                        pangkat = list_satuan.index(satuan1) - list_satuan.index(satuan2)
                        hasil = angka / (10**pangkat)
                        print(f"{angka}{satuan1} = {hasil}{satuan2}")
                    elif list_satuan.index(satuan1) < list_satuan.index(satuan2):
                        pangkat = -(list_satuan.index(satuan1) - list_satuan.index(satuan2))
                        hasil = angka * (10**pangkat)
                        print(f"{angka}{satuan1} = {hasil}{satuan2}")
                        

            ulang = str(input("\nIngin mencoba lagi?(ya/tidak) : ")).lower()


def konversi_massa():
    ulang = "ya"
    while ulang == "ya":
        satuan1 = str(input("Satuan yang dikonversi (kg/hg/dag/gr/dg/cg/mg) : ")).lower()
        satuan2 = str(input("Hasil konversi (kg/hg/dag/gr/dg/cg/mg) : ")).lower()
        angka = float(input("Masukkan angka yang ingin dikonversi : "))
        list_satuan = ["kg","hg","dag","gr","dg","cg","mg"]

        if satuan1 not in list_satuan or satuan2 not in list_satuan:
            print("\nMasukkan satuan sesuai pilihan yang tertera!")
        else:
            for i in range(7):
                if i == list_satuan.index(satuan1):
                    if list_satuan.index(satuan1) > list_satuan.index(satuan2):
                        pangkat = list_satuan.index(satuan1) - list_satuan.index(satuan2)
                        hasil = angka / (10**pangkat)
                        print(f"{angka}{satuan1} = {hasil}{satuan2}")
                    elif list_satuan.index(satuan1) < list_satuan.index(satuan2):
                        pangkat = -(list_satuan.index(satuan1) - list_satuan.index(satuan2))
                        hasil = angka * (10**pangkat)
                        print(f"{angka}{satuan1} = {hasil}{satuan2}")
            ulang = str(input("\nIngin mencoba lagi?(ya/tidak) : ")).lower()


def konversi_waktu():
    import random
    ulang = "ya"
    while ulang == "ya":
        pilih = random.randint(1,5)
        waktu1 = "jam"
        waktu2 = random.choice(["menit","detik"])
        jawab = float(input(f"{pilih} {waktu1} berapa {waktu2}? "))
        if waktu2 == "menit":
            hasil = pilih * 60
            print(f"{pilih} {waktu1} = {hasil} {waktu2}")
        else:
            hasil = pilih * 60 * 60
            print(f"{pilih} {waktu1} = {hasil} {waktu2}")
        ulang = str(input("\nIngin mencoba lagi?(ya/tidak) : ")).lower()


def konversi_suhu():
    ulang = "ya"
    while ulang == "ya":
        suhu1 = str(input("suhu yang di konversi: ")).lower()
        suhu2 = str(input("hasil suhu yang di konversi: ")).lower()
        angka = float(input("masukkan angka yang di konversi: "))
        if suhu1 == "celcius":
            if suhu2 == "fahrenheit":
                hasil = angka * 9/5 + 32
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "kelvin":
                hasil = angka + 273.15
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "reamur":
                hasil = angka * 4/5
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            else:
                print(f"Masukkan nama suhu (celcius/fahrenheit/kelvin/reamur)")
        elif suhu1 == "fahrenheit":
            if suhu2 == "celcius":
                hasil = 5/9 * (angka - 32)
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "kelvin":
                hasil = 5/9 * (angka - 32) + 273
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "reamur":
                hasil = 49 * (angka - 32)
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            else:
                print(f"Masukkan nama suhu (celcius/fahrenheit/kelvin/reamur)")
        elif suhu1 == "kelvin":
            if suhu2 == "celcius":
                hasil = angka - 273
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "fahrenheit":
                hasil = 9/5 * (angka - 273) + 32
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "reamur":
                hasil = 4/5 * (angka - 273) 
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            else:
                print(f"Masukkan nama suhu (celcius/fahrenheit/kelvin/reamur)")
        elif suhu1 == "reamur":
            if suhu2 == "celcius":
                hasil = 5/4 * angka
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "fahrenheit":
                hasil = 9/4 * angka + 32
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            elif suhu2 == "kelvin":
                hasil = 5/4 * angka + 273 
                print(f"{angka} {suhu1} = {hasil} {suhu2}")
            else:
                print(f"Masukkan nama suhu (celcius/fahrenheit/kelvin/reamur)")
        else:
            print(f"Masukkan nama suhu (celcius/fahrenheit/kelvin/reamur)")
        
        ulang = str(input("\nIngin mencoba lagi?(ya/tidak) : ")).lower()


#Contoh soal materi zat
def contoh_zat():
    ulang = "ya"
    while ulang == "ya":
        print("=======================================")
        m = float(input("Masukkan nilai m (gram) : "))
        v = float(input("Masukkan nilai v (cm3): "))
        jawaban = m/v
        print(f"""Jawab:
ρ = m/v
ρ = {m} gram / {v} cm3
ρ = {jawaban:.2f}""")
        ulang = str(input("\nUlangi?(ya/tidak) : ")).lower()


#Contoh soal materi kalor
def contoh_kalor():
    ulang = "ya"
    while ulang == "ya":
        print("=======================================")
        m = float(input("masukkan nilai m (gram): "))
        c = float(input("masukkan niali c (kal/gr°C): "))
        t1 = float(input("masukkan nilai T1 (°C): "))
        t2 = float(input("masukkan nilai T2 (°C): "))
        jawaban = m*c*(t2-t1)
        print(f"""Jawaban:
Q = m.c.∆t
Q = {m} x {c} x ({t2} - {t1})
Q = {jawaban:.2f} joule""")
        ulang = str(input("\nUlangi?(ya/tidak): ")).lower()

