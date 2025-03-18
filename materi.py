from konversi_contohsoal import *

#BESARAN
def materi_besaran():
    print(f"""
Besaran dan Satuan

➤Besaran adalah sesuatu yang dapat diukur (dinyatakan dengan nilai/angka) dan mempunya satuan.
➤Satuan adalah besaran pembanding yang digunakan dalam pengukuran.

Contoh:
300 meter ⇒ 300 merupakan besaran dan meter merupakan satuan besaran panjang.
10 liter  ⇒ 10 merupakan besaran dan liter merupakan satuan besaran volume.

Ada dua macam sistwm satuan, yaitu:
1. Sistem Inggris, dikenal dengan FPS(Foot, Pound, Second).
2. Sistem Metrik, terdiri dari dua yaitu: Sistem MKS(Meter, Kilogram, sekon) dan CGS(Centimeter, Gram, Second).

1. Besaran Pokok
    Besaran pokok adalah besaran yang satuannya telah ditetapkan terlebih dahulu dan tidak diturunkan dari besaran lain.
    Berikut tujuh besaran pokok dan satuannya berdasarkan Sistem (SI).

-------------------------------------------------------------------
| NO|  BESARAN POKOK     |   SATUAN SI(MKS)  |   SATUAN SI(CGS)   |
-------------------------------------------------------------------
| 1 |  Panjang           |   Meter(m)        |   Centimeter(cm)   |
| 2 |  Massa             |   Kilogram(kg)    |   Gram(g)          |
| 3 |  Waktu             |   Sekon(s)        |   Sekon(s)         |
| 4 |  Suhu              |   Kelvin(k)       |   Kelvin(k)        |
| 5 |  Kuat Arus         |   Ampere(A)       |   Stat ampere      |
| 6 |  Intensitas Cahaya |   Candela(Cd)     |   Candela(Cd)      |
| 7 |  Jumlah Zat        |   Kilo mol(Kmol)  |   Mol              |
-------------------------------------------------------------------
    
a. Panjang
Dalam fisika, panjang menyatakan jarak antara dua titik. Satuan besaran panjang berdasarkan SI dinyatakan dalam meter (m).
⟡ Alat ukur panjang
    1. Mistar/penggaris, memiliki ketelitian
    2. Stikmeter (meteran gulung), memiliki ketelitian 0,1 cm
    3. Jangka sorong memiliki ketelitian 0,01 cm atau 0,1 mm
    4. Mikrometer sekrup, memiliki ketelitian 0,01 mm

⟡ Konversi satuan panjang
  Tangga konversi:
    km
      hm
        dam
           m
            dm
              cm
                mm

    Catatan:
    - Setiap turunan satu tingkat satuan dikali 10.
    - Setiap naik satu tingkat satuan dibagi 10.

    Contoh:
    3m = 3 x 100cm = 300cm
    20cm = 20 : 100m = 0,2m

Selamat mencoba:) """)
    #def konversi panjang
    konversi_panjang()
    
    print("""
b. Massa
Massa adalah banyak zat yang terkandung dalam suatu benda. Satuan massa dalam Sistem Satuan Internasional adalah kilogram.
Seperti halnya satuan panjang, satuan massa juga dapat diubah atau dikonversikan ke satuan massa yang lebih besar atau lebih kecil.
⟡ Alat ukur massa
    1. Neraca pasar atau timbangan
    2. Neraca kimia, biasa digunakan untuk mengukur massa yang kecil (dalam gram)
    3. Neraca elektronik atau digital
    4. Neraca lengan, ada yang terdiri dari dua lengan yang sama dan ada pula yang tiga lengan

⟡ Konversi satuan massa
  Tangga konversi:
    kg
      hg
        dag
           gr
             dg
               cg
                 mg

    Catatan:
    - Setiap turunan satu tingkat satuan dikali 10.
    - Setiap naik satu tingkat satuan dibagi 10.

    Contoh:
    5gr = 5 x 1000mg = 5000mg
    8gr = 8 : 10dag = 0,8dag

Selamat mencoba:) """)
    #def konversi massa
    konversi_massa()

    print("""
c. Waktu
Satuan waktu secara internasional adalah sekon (detik). Waktu adalah selang antara dua kejadian atau dua peristiwa.
Misalnya, waktu siang adalah sejak matahari terbit hingga tenggelam, waktu hidup adalah sejak dilahirkan hingga meninggal.
Dalam kehidupan sehari-hari waktu dapat diukur dengan jam tangan atau stop watch.
Untuk peristiwa yang selang terjadinya cukup lama, waktu dinyatakan dalam satuan-satuan yang lebih besar, misalnya: menit, jam, bulan, abad dan lain-lain.
Sedangkan, untuk kejadian-kejadian yang cepat sekali bisa disatuan milisekon (ms) dan mikrosekon(ms).

1 hari = 24 jam
1 jam = 60 menit
1 menit = 60 sekon

Contoh:
""")
    #def konversi waktu
    konversi_waktu()
    
    
    print("""
d. Suhu
Suhu atau temperatur merupakan salah satu besaran pokok yang sering kita jumpai dalam kehidupan seharihari. Pada siang hari kita merasa panas,
sebaliknya pada malam hari terasa dingin. Suatu benda dikatakan panas berarti benda tersebut bersuhu tinggi, demikian juga sebaliknya,
benda dikatakan dingin berarti benda tersebut bersuhu rendah. Jadi suhu menyatakan ukuran tingkat atau derajat panas atau dinginnya suatu benda.
Alat ukur suhu yang sering digunakan adalah termometer. Termometer yang sering digunakan yaitu termometer raksa dan termometer alkohol.

⟡ Skala suhu
1. Celcius (C)
2. Farenheit (F)
2. Reamur (R)
4. Kelvin (K)

⟡ Konversi suhu
Rumus konversi celcius:
⦁ Celcius ke fahrenheit ⇒ F = 9/5 x C + 32
⦁ Celcius ke kelvin     ⇒ K = C + 273
⦁ Celcius ke reamur     ⇒ R = 4/5 x C
Rumus konversi fahrenheit:
⦁ Fahrenheit ke celcius ⇒ C = 5/9 (F - 32)
⦁ Fahrenheit ke kelvin  ⇒ K = 5/9 (F - 32) + 273
⦁ Fahrenheit ke reamur  ⇒ R = 4/9 x (F - 32)
Rumus konversi kelvin:
⦁ Kelvin ke celcius     ⇒ C = K - 273
⦁ Kelvin ke fahrenheit  ⇒ F = 9/5 x (K - 273) + 32
⦁ Kelvin ke reamur      ⇒ R = 4/5 x (K-273)
Rumus konversi reamur:
⦁ Reamur ke celcius     ⇒ C = 5/4 x R
⦁ Reamur ke fahrenheit  ⇒ F = 9/4 x R + 32
⦁ Reamur ke Kelvin      ⇒ K = 5/4 x R + 273

Selamat mencoba:)""")
    konversi_suhu()

#BESARAN TURUNAN
    print("""
2. Besaran Turunan
Besaran turunan adalah besaran yang satuannya diturunkan dari besaran pokok. Berikut beberapa besaran turunan.
--------------------------------------------------------------------------------
| NO|  BESARAN TURUNAN  |   PENJABARAN               |   SATUAN                |
--------------------------------------------------------------------------------
| 1 |  Luas             |   Panjang x Lebar          |   m**2                  |
| 2 |  Volume           |   Panjang x Lebar x Tinggi |   m**3                  |         
| 3 |  Gaya             |   Massa x Percepatan       |   Newton(N) = kg.m/s**2 |
| 4 |  Massa Jenis      |   Kelvin(k)                |   Kelvin(k)             |
--------------------------------------------------------------------------------
""")


#ZAT
def materi_zat():
    print("""
Zat dan Wujudnya

Zat adalah sesuatu yang menempati ruang dan memiliki massa. Pada prinsipnya terdapat tiga wujud zat yaitu : zat padat, zat cair, dan zat gas.

A. WUJUD ZAT
1. Jenis-Jenis Zat
a. Zat Padat
    Sifat-sifat zat padat sebagai berikut.
    1) Bentuk benda tetap
    2) Tidak dipengaruhi oleh tempat benda diletakkan.
    Contoh : Batu, kayu, besi, dan lain-lain.

b. Zat Cair
    Sifat-sifat zat cair sebagai berikut.
    1) Volume (banyaknya) benda-benda tersebut tetap, artinya jika benda-benda tersebut ditempatkan ke dalam berbagai wadah, volumenya tetap.
    2) Bentuk benda-benda tersebut tergantung dari bentuk wadahnya. Jika dimasukkan ke dalam botol, berbentuk botol. Jika dimasukkan ke dalam mangkuk,
       berbentuk mangkuk.
    Contoh : Air, minyak, susu, dan lain-lain.

c. Zat Gas
    Sifat-sifat zat gas sebagai berikut.
    1) Volumenya tidak tetap, tergantung tempatnya.
    2) Bentuknya tidak tetap, tergantung bentuk wadahnya.
    3) Selalu memenuhi ruang.
    Contoh : uap air dan asap hasil pembakaran

    Beberapa zat atau benda dapat mengalami perubahan wujud, misalnya dari cair menjadi padat atau dari padat menjadi uap. Perubahan wujud dapat terjadi melalui
    beberapa peristiwa berikut.
    1) Mencair atau melebur yaitu perubahan wujud zat dari padat menjadi cair.
    2) Membeku yaitu perubahan wujud zat dari cair menjadi padat.
    3) Menguap yaitu perubahan wujud zat dari cair menjadi gas.
    4) Mengembun yaitu perubahan wujud zat dari uap (gas) menjadi cair.
    5) Menyublim yaitu perubahan wujud zat dari gas menjadi padat.
    6) Melenyap yaitu wujud zat dari padat menjadi gas.

2. Partikel-Partikel Zat
    Zat tersusun atas partikel-partikel yang disebut atom. Beberapa atom bergabung membentuk molekul. Molekul adalah bagian terkecil dari suatu zat yang masih
mempunyai sifat zat itu. Molekul pembentuk zat padat, zat cair, dan gas memiliki sifat yang berbeda-beda.

a. Sifat-sifat molekul pembentuk zat padat yaitu:
1) letak molekul-molekulnya sangat berdekatan (rapat),
2) susunan molekulnya teratur, dan
3) gerak molekulnya tidak bebas.
Sifat-sifat molekuler tersebut mengakibatkan bentuk benda padat relatif tetap dan tidak mudah diubah.

b. Sifat-sifat molekul pembentuk zat cair yaitu:
1) letak molekulnya berdekatan,
2) susunan molekulnya tidak teratur, dan
3) gerak molekulnya lebih bebas.
Sifat-sifat ini menjadikan bentuk zat cair mudah berubah sesuai wadahnya. Zat ini dapat mengalir.

c. Sifat-sifat molekul pembentuk gas yaitu:
1) letak molekulnya berjauhan,
2) susunan molekulnya tidak teratur, dan
3) gerak molekulnya sangat bebas sehingga dapat memenuhi ruangan.
Sifat-sifat ini menjadikan bentuk gas bergerak sangat lebar dan dapat mengembang volumenya.

3. Adhesi dan Kohesi
    Antarmolekul suatu zat terdapat gaya tarik-menarik yang disebut kohesi dan adhesi. Kohesi adalah gaya tarik-menarik antarmolekul yang sejenis.
Contohnya gaya tarik-menarik antarmolekul air, gaya tarik-menarik antarmolekul raksa. Adhesi adalah gaya tarik-menarik antarmolekul yang tidak sejenis.
Contohnya gaya tarik-menarik antara molekul-molekul air dengan molekul-molekul kaca tabung reaksi. Contoh lain adhesi adalah tulisan kapur yang melekat
pada papan tulis.

4. Meniskus
    Bentuk permukaan zat cair dalam tabung disebut meniskus. Oleh karena bentuk permukaan air dalam tabung cekung, sehingga disebut meniskus cekung.
Sebaliknya, permukaan raksa di dalam tabung reaksi berbentuk cembung sehingga disebut meniskus cembung.

5. Kapilaritas
    Kapilaritas adalah peristiwa naik atau turunnya permukaan zat cair dalam pipa atau saluran kapiler (saluran sempit). Kapilaritas dalam kehidupan sehari-hari
misalnya naiknya air tanah melalui pembuluh kayu pada batang tanaman dan naiknya minyak tanah melalui sumbu pada kompor atau lampu minyak.
Selain itu, menetesnya air dari satu ujung saputangan yang ujung lainnya dicelupkan ke dalam air juga merupakan peristiwa kapilaritas.


B. MASSA JENIS
Massa jenis suatu zat adalah bilangan yang menyatakan massa zat itu tiap satuan volumenya. Massa jenis ditulis dengan persamaan:

|----------|
| ρ = m/V  |
|----------|

Keterangan:
ρ = massa jenis zat (dibaca ”rho”), satuannya kg/m³  atau g/cm³ 
m = massa benda, satuannya kg atau gram
V = volume benda, satuannya m³ atau cm³ 
Satuan massa jenis dalam sistem MKS adalah kg/m³  dan dalam CGS adalah g/cm³.

Contoh soal:
 Massa sebatang aluminium 270 gram. Jika volume aluminium itu 100 cm3, berapa massa jenisnya dalam g/cm3 ?
✦Penyelesaian:
Diketahui:
m = 270 gram
V = 100 cm3
Ditanyakan:
massa jenis aluminium (ρ)
Jawab:
ρ = m/v
  = 270 gram / 100 cm
  = 2,7 g/cm3
Jadi, massa jenis aluminium 2,7 g/cm3.

Selamat mencoba:)""")
    contoh_zat()

    

#KALOR
def materi_kalor():
    print("""
✽Kalor sebagai Bentuk Energi
1. kalor
kalor yaitu peristiwa menjerang air. sesuatu menyebabkan air dingin berubah menjadi panas(mendidih). sesuatu tersebut adalah kalor yang di bawa oleh api.
energi kalor disebut juga dengan energi panas. jadi, kalor adalah salah satu bentuk energi. satuan kalor adalah kalori.

✽Kalor dapat mengubah Suhu Benda
Benda-benda yang bersuhu lebih tinggi dari lingkungannya akan cenderung melepas kalor. demikian juga sebaliknya benda-benda yang bersuhu lebih rendah
dari lingkungannya akan cenderung menerima kalor untuk menstabilkan kondisi dengan lingkungan disekitarnya. suhu zat akan berubah ketika zat tersebut melepas
atau menerima kalor. kalor dapat mengubah suhu suatu benda.

1. kalor jenis
kalor jenis suatu zat adalah banyaknya kalor yang diperlukan oleh suatu zat bermassa 1 kg untuk menaikkan suhu 1 °C sebagai contoh:
kalor jenis air 4.200 J/kg °C, artinya kalor yang diperlukan untuk menaikan suhu 1 kg air sebesar 1 °C adalah 4.200 J.
kalor jenis suatu zat dapat diukur dengan alat kalorimeter.

banyaknya kalor yang diperlukan untuk menaikkan atau menurunkan suhu suatu benda bergantung pada:
 ● massa benda (m)
 ● jenis benda / kalor jenis benda (c)
 ● perubahan suhu (∆t)

oleh karena itu, hubungan banyaknya kalor, massa zat, kalor jenis zat, dan perubahan suhu zat dapat dinyatakan dalam persamaan.
    |---------------|
    |Q = m.c.(T2-T1)|
    |---------------|

keterangan:
Q = Banyaknya kalor yang diserap atau dilepaskan (joule)
m = massa zat(kg)
c = kalor jenis zat(joule/kg°C)
T1 = suhu awal(°C)
T2 = suhu akhir(°C)

   ------------------------------
   | 1 kalori = 4,2 joule       |
   | 1 kilokalori = 1.000 kalori|
   ------------------------------

secara alami kalor berpindah dari zat yang suhunya tinggi ke zat yang suhunya rendah.Ditinjau dari cara perpindahannya,
ada tiga cara dalam perpindahannya, ada tiga cara dalam perpindahan kalor yaitu:
 ❄ Konduksi
 ❄ Konveksi
 ❄ Radiasi

✶ Perpindahan Kalor secara Konduksi
cobalah membakar ujung besi dan ujung besi lainnya kamu pegang, setelah beberapa lama ternyata ujung besi yang kamu pegang lama-kelamaan teraa semakin panas.
hal ini disebabkan adanya perpindahan kalor yang melalui besi. peristiwa perpindahan dari ujung besi kalor yang dinpanaskan ke ujung besi yang kamu pegang mirip
dengan perpindahan buku yang kamu lakukan, dimana molekul-molekul besi yang menghantarkan kalor tidak ikut berpindah.perpindahan kalor seperti ini dinamakan
perpindahan kalor secara hantaran atau konduksi. bahan yang dapat menghantarkan kalor disebut konduktor kalor, misalnya besi, baja, tembaga, seng,
dan aluminium(jenis logam). adapun penghantar yang kurang baik/penghantar yang buruk disebut isolator kalor, misalnya kayu, kaca, wol, kertas,
dan plastik(jenis bukan logam).

✶ Perpindahan Kalor secara Konveksi
perpindahan kalor secara konveksi terjadi pada zat cair dan gas. perpindahan kalor secara konveksi terjadi karena adanya perbedaan massa jenis dalam zat tersebut.
perpindahan kalor yang diikuti oleh perpindahan partikel-partikel zatnya disebut konveksi/aliran. selain perpindah kalor secara konveksi terjadi pada zat cair,
ternyata konveksi juga dapat terjadi pada gas/udara. peristiwa konveksi kalor melalui pengantar air.

✶ Perpindahan Kalor secara Radiasi
Bagaimanakah energi kalor matahari dapat sampai ke bumi? Telah kita ketahui bahwa antara matahari dengan bumi berupa ruang hampa udara, sehingga kalor dari matahari
sampai ke bumi tanpa melalui zat perantara. Perpindahan kalor tanpa melalui zat perantara atau medium ini disebut radiasi/hantaran. Contoh perpindahan kalor secara
radiasi, misalnya pada waktu kita mengadakan kegiatan perkemahan, di malam hari yang dingin sering menyalakan api unggun. Saat kita berada di dekat api unggun badan
kita terasa hangat karena adanya perpindahan kalor dari api unggun ke tubuh kita secara radiasi. Walaupun di sekitar kita terdapat udara yang dapat memindahkan
kalor secara konveksi, tetapi udara merupakan penghantar kalor yang buruk (isolator). Jika antara api unggun dengan kita diletakkan sebuah penyekat atau tabir,
ternyata hangatnya api unggun tidak dapat kita rasakan lagi. Hal ini berarti tidak ada kalor yang sampai ke tubuh kita, karena terhalang oleh penyekat itu.
Dari peristiwa api unggun dapat disimpulkan bahwa:

    ● Dalam peristiwa radiasi, kalor berpindah dalam bentuk cahaya, karena cahaya dapat merambat dalam ruang hampa, maka kalor pun dapat merambat dalam ruang hampa
    ● Radiasi kalor dapat dihalangi dengan cara memberikan tabir/penutup yang dapat menghalangi cahaya yang dipancarkan dari sumber cahaya.

✽ Kalor dapat merubah wujud zat
Suatu zat apabila diberi kalor terus-menerus dan mencapai suhu maksimum, maka zat akan mengalami perubahan wujud. Peristiwa ini juga berlaku jika suatu zat
melepaskan kalor terus-menerus dan mencapai suhu minimumnya. Oleh karena itu, selain kalor dapat digunakan untuk mengubah suhu zat, juga dapat digunakan
untuk mengubah wujud zat.
    ● Menguap (terjadi perubahan suhu)
    Apakah pada waktu zat menguap memerlukan kalor? Dari manakah kalor itu diperoleh? pada waktu air dipanaskan akan tampak uap keluar dari permukaan air.
    Kenyataan ini menunjukkan bahwa pada waktu menguap zat memerlukan kalor. Jika air dipanaskan terus-menerus, lama-kelamaan air tersebut akan habis. Habisnya air
    akibat berubah wujud menjadi uap atau gas. Peristiwa ini disebut menguap, yaitu perubahan wujud dari cair ke gas,
    karena molekul-molekul zat cair bergerak meninggalkan permukaan zat cairnya. Pada peristiwa menguap terjadi perubahan suhu, oleh karena itu berlaku:
          |---------------| 
          |Q = m.c.(T2-T1)|
          |---------------|
          
     ● Mendidih (tidak mengalami perubahan suhu, namun terjadi perubahan wujud)
    Mendidih adalah peristiwa penguapan zat cair yang terjadi di seluruh bagian zat cair tersebut. Peristiwa ini dapat dilihat dengan munculnya gelembung-gelembung
    yang berisi uap air dan bergerak dari bawah ke atas dalam zat cair. Zat cair yang mendidih jika dipanaskan terus-menerus akan berubah menjadi uap. Banyaknya kalor yang diperlukan untuk
    mengubah 1 kg zat cair menjadi uap seluruhnya pada titik didihnya disebut kalor uap (U). Karena tidak terjadi perubahan suhu, maka besarnya kalor uap dapat
    dirumuskan:
            |-------|
            |Q = m.u|
            |-------|

 ✽ Keterangan:
Q = kalor yang diserap/dilepaskan (joule)
m = massa zat (kg)
U = kalor uap (joule/kg)

Contoh soal:
 Es massa 200 gram bersuhu -5°C dipanasi hinngga suhunya menjadi -1°C, jika kalor jenis es adalah 0,5 kal/gr°C. Tentukan berapa kalor yang diperlukan dalam proses
 tersebut!
 
✽Penyelesaian:
Diketahui:
m = 200 gram
c = 0,5 kal/gr°C
T1 = -5°C
T2 = -1°C
Ditanyakan:
Banyaknya kalor yang diserap atau dilepaskan (Q)
Jawab:
Q = m.c.(T2-T1)
Q = 200 x 0,5 x [-1-(-5)]
Q = 100 x 4 
Q = 400 kalor
Jadi, banyaknya kalor yang diserap atau dilepaskan adalah 400 kalor

Selamat mencoba:)""")
    contoh_kalor()
