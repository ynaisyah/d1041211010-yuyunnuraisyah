# Hitung Luas Segitiga Sederhana
def luas_segitiga():
    a = int(input("Masukkan alas segitiga: "))
    t = int(input("Masukkan tinggi segitiga: "))
    luas = a * t / 2
    print("Luas segitiga adalah: ", luas)

luas_segitiga()

def luas_lingkaran():
    r = int(input("Masukan jari-jari lingkaran: "))
    luas = 3.14 * r * r
    print("Luas Lingkaran adalah: ", luas)

luas_lingkaran()