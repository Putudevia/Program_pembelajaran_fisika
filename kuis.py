from kumpulan_soal import *

#Kuis Besaran
def kuis_besaran():
    ulang = "ya"
    while ulang == "ya":
        soal_kuis = [f"{besaran_soal1()}\n{besaran_jawab1()}",
                     f"{besaran_soal2()}\n{besaran_jawab2()}",
                     f"{besaran_soal3()}\n{besaran_jawab3()}",
                     f"{besaran_soal4()}\n{besaran_jawab4()}",
                     f"{besaran_soal5()}\n{besaran_jawab5()}",
                     f"{besaran_soal6()}\n{besaran_jawab6()}",
                     f"{besaran_soal7()}\n{besaran_jawab7()}",
                     f"{besaran_soal8()}\n{besaran_jawab8()}",
                     f"{besaran_soal9()}\n{besaran_jawab9()}",
                     f"{besaran_soal10()}\n{besaran_jawab10()}"
                     ]
        penjelasan = [f"{besaran_penjelasan1()}",
                      f"{besaran_penjelasan2()}",
                      f"{besaran_penjelasan3()}",
                      f"{besaran_penjelasan4()}",
                      f"{besaran_penjelasan5()}",
                      f"{besaran_penjelasan6()}",
                      f"{besaran_penjelasan7()}",
                      f"{besaran_penjelasan8()}",
                      f"{besaran_penjelasan9()}",
                      f"{besaran_penjelasan10()}"
                      ]
    
        kunci_jawaban = ["C","B","A","A","D","D","A","B","C","A"]
        nilai = 0

        for i in range(len(soal_kuis)):
            print(f"\nsoal {i+1}\n{soal_kuis[i]}")
            jawab = str(input("jawab(a/b/c/d) : ")).upper()
            if jawab == kunci_jawaban[i]:
                nilai += 10
                print(f"Jawaban anda benar 😊\n{penjelasan[i]}")
            else:
                nilai += 0
                print(f"Jawaban anda salah 😢\n{penjelasan[i]}")
        print("\nAnda mendapatkan nilai :",nilai)
        ulang = str(input("Ingin mengerjakan ulang? (ya/tidak) : ")).lower()

#KUIS ZAT
def kuis_zat():
    ulang = "ya"
    while ulang == "ya":
        soal_kuis = [f"{zat_soal1()}\n{zat_jawab1()}",
                     f"{zat_soal2()}\n{zat_jawab2()}",
                     f"{zat_soal3()}\n{zat_jawab3()}",
                     f"{zat_soal4()}\n{zat_jawab4()}",
                     f"{zat_soal5()}\n{zat_jawab5()}",
                     f"{zat_soal6()}\n{zat_jawab6()}",
                     f"{zat_soal7()}\n{zat_jawab7()}",
                     f"{zat_soal8()}\n{zat_jawab8()}",
                     f"{zat_soal9()}\n{zat_jawab9()}",
                     f"{zat_soal10()}\n{zat_jawab10()}"
                    ]
        penjelasan = [f"{zat_penjelasan1()}",
                      f"{zat_penjelasan2()}",
                      f"{zat_penjelasan3()}",
                      f"{zat_penjelasan4()}",
                      f"{zat_penjelasan5()}",
                      f"{zat_penjelasan6()}",
                      f"{zat_penjelasan7()}",
                      f"{zat_penjelasan8()}",
                      f"{zat_penjelasan9()}",
                      f"{zat_penjelasan10()}"
                      ]
        kunci_jawaban = ["B","C","A","A","A","C","D","D","B","C"]
        nilai = 0

        for i in range(len(soal_kuis)):
            print(f"\nsoal {i+1}\n{soal_kuis[i]}")
            jawab = str(input("jawab(a/b/c/d) : ")).upper()
            if jawab == kunci_jawaban[i]:
                nilai += 10
                print(f"Jawaban anda benar 😊\n{penjelasan[i]}")
            else:
                nilai += 0
                print(f"Jawaban anda salah 😢\n{penjelasan[i]}")
        print("\nAnda mendapatkan nilai :",nilai)
        ulang = str(input("Ingin mengerjakan ulang? (ya/tidak) : ")).lower()


#Kuis Kalor
def kuis_kalor():
    ulang = "ya"
    while ulang == "ya":
        soal_kuis = [f"{kalor_soal1()}\n{kalor_jawab1()}",
                     f"{kalor_soal2()}\n{kalor_jawab2()}",
                     f"{kalor_soal3()}\n{kalor_jawab3()}",
                     f"{kalor_soal4()}\n{kalor_jawab4()}",
                     f"{kalor_soal5()}\n{kalor_jawab5()}",
                     f"{kalor_soal6()}\n{kalor_jawab6()}",
                     f"{kalor_soal7()}\n{kalor_jawab7()}",
                     f"{kalor_soal8()}\n{kalor_jawab8()}",
                     f"{kalor_soal9()}\n{kalor_jawab9()}",
                     f"{kalor_soal10()}\n{kalor_jawab10()}"
                     ]
        penjelasan = [f"{kalor_penjelasan1()}",
                      f"{kalor_penjelasan2()}",
                      f"{kalor_penjelasan3()}",
                      f"{kalor_penjelasan4()}",
                      f"{kalor_penjelasan5()}",
                      f"{kalor_penjelasan6()}",
                      f"{kalor_penjelasan7()}",
                      f"{kalor_penjelasan8()}",
                      f"{kalor_penjelasan9()}",
                      f"{kalor_penjelasan10()}"
                      ]
        kunci_jawaban = ["A","D","D","C","A","C","A","C","C","C"]
        nilai = 0

        for i in range(len(soal_kuis)):
            print(f"\nsoal {i+1}\n{soal_kuis[i]}")
            jawab = str(input("jawab(a/b/c/d) : ")).upper()
            if jawab == kunci_jawaban[i]:
                nilai += 10
                print(f"Jawaban anda benar 😊\n{penjelasan[i]}")
            else:
                nilai += 0
                print(f"Jawaban anda salah 😢\n{penjelasan[i]}")
        print("\nAnda mendapatkan nilai :",nilai)
        ulang = str(input("Ingin mengerjakan ulang? (ya/tidak) : ")).lower()

