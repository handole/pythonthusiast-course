import luaskeliling

# input angka untuk persego
print('PERSEGI PANJANG')
panjang = int(input('Masukan panjang : '))
lebar = int(input('Masukkan lebar\t: '))

luas = luaskeliling.luas_persegipanjang(panjang, lebar)
keliling = luaskeliling.keliling_persegipanjang(panjang, lebar)

print('Panjang\t\t: %d' % panjang)
print('Lebar\t\t: %d' % lebar)
print('Luasnya\t\t: %d' % luas)
print('Kelilingnya\t: %d' % keliling)
print('')
# input angka bujursangkar
print('###########################################')
print('BUJUR SANGKAR')
sisi = int(input('Masukan sisi: '))

luas = luaskeliling.luas_bujursangkar(sisi)
keliling = luaskeliling.keliling_bujursangkar(sisi)

print('Sisi\t\t: %d' % sisi)
print('Luasnya\t\t: %d' % luas)
print('Kelilingnya\t: %d' % keliling)
print('')

# input angka lingkaran
print('###########################################')
print('LINGKARAN')
jari = int(input('Masukkan jari-jari:'))

luas = luaskeliling.luas_lingkaran(jari)
keliling = luaskeliling.keliling_lingkaran(jari)

print('Jari-jari\t: %d' % jari)
print('Luasnya\t: %d' % luas)
print('Kelilingnya\t: %d' % keliling)
print('')

# input angka untuk segitiga
print('###########################################')
print('SEGITIGA')
alas = int(input('Masukkan alas: '))
tinggi = int(input('Masukkan tingginya: '))
a = alas
b = int(input('Masukkan sisi b: '))
c = int(input('Masukkan sisi c: '))

luas = luaskeliling.luas_segitiga(alas, tinggi)
keliling = luaskeliling.keliling_segitiga(a, b, c)

print('Alasnya \t: %d' % alas)
print('Tingginya \t: %d' % tinggi)
print('sisi a \t: %d' % a)
print('Sisi b \t: %d' % b)
print('Sisi c \t: %d' % c)
print('Luasnya \t: %d' % luas)
print('Kelilingnya \t: %d' % keliling)
