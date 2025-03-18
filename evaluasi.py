from kumpulan_soal import *

def evaluasi():
    soal_evaluasi = [f"{evaluasi_soal1()}\n{evaluasi_jawab1()}",
                    f"{evaluasi_soal2()}\n{evaluasi_jawab2()}",
                    f"{evaluasi_soal3()}\n{evaluasi_jawab3()}",
                    f"{evaluasi_soal4()}\n{evaluasi_jawab4()}",
                    f"{evaluasi_soal5()}\n{evaluasi_jawab5()}",
                    f"{evaluasi_soal6()}\n{evaluasi_jawab6()}",
                    f"{evaluasi_soal7()}\n{evaluasi_jawab7()}",
                    f"{evaluasi_soal8()}\n{evaluasi_jawab8()}",
                    f"{evaluasi_soal9()}\n{evaluasi_jawab9()}",
                    f"{evaluasi_soal10()}\n{evaluasi_jawab10()}",
                    f"{evaluasi_soal11()}\n{evaluasi_jawab11()}",
                    f"{evaluasi_soal12()}\n{evaluasi_jawab12()}",
                    f"{evaluasi_soal13()}\n{evaluasi_jawab13()}",
                    f"{evaluasi_soal14()}\n{evaluasi_jawab14()}",
                    f"{evaluasi_soal15()}\n{evaluasi_jawab15()}",
                    f"{evaluasi_soal16()}\n{evaluasi_jawab16()}",
                    f"{evaluasi_soal17()}\n{evaluasi_jawab17()}",
                    f"{evaluasi_soal18()}\n{evaluasi_jawab18()}",
                    f"{evaluasi_soal19()}\n{evaluasi_jawab19()}",
                    f"{evaluasi_soal20()}\n{evaluasi_jawab20()}",
                    ]

    kunci_jawaban = ["C","C","B","D","A","A","A","D","D","A","D","C","A","D","C","D","C","B","C","B","A"]
    nilai = 0

    for i in range(len(soal_evaluasi)):
        print(f"\nsoal {i+1}\n{soal_evaluasi[i]}")
        jawab = str(input("jawab(a/b/c/d) : ")).upper()
        if jawab == kunci_jawaban[i]:
            nilai += 5
        else:
            nilai += 0
    print("\nAnda mendapatkan nilai :",nilai)
