# Hitung Luas Segitiga Sederhana
def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)

luas_segitiga()

#Menghitung Luas Persegi Panjang
def luas_persegi_panjang():
    p = int(input("Masukan panjang persegi panjang:"))
    l = int(input("Masukan lebar persegi panjang:"))
    luas = p * l
    print("Luas Persegi Panjang adalah: ", luas)

luas_persegi_panjang()

#Menghitung Luas Lingkaran
def luas_lingkaran():
    r = int(input('Masukan jari-jari lingkarang: '))
    luas = 3.14 * r * r
    print("Luas Lingkarang adalah: ", luas)