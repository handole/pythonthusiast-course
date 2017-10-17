import math

#fungsi luas dan keliling
def luas_persegipanjang(panjang, lebar):
    return panjang * lebar

def keliling_persegipanjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_bujursangkar(sisi):
    return sisi * sisi

def keliling_bujursangkar(sisi):
    return 4 * sisi

def luas_lingkaran(jari):
    return math.pi * jari * jari

def keliling_lingkaran(jari):
    return 2 * math.pi * jari

def luas_segitiga(alas, tinggi):
    return (alas * tinggi) / 2

def keliling_segitiga(a, b, c):
    return a + b + c