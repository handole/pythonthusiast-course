message = 'ada pesan dari bumi datar'
sebutan = 'bumi datar'
jumlah = 4
panjang = 200

print(message)
print(sebutan)
print(jumlah)
print(panjang)

if jumlah <= 1:
    print('Jumlah anggota belum mencukupi')
    print('Silahkan cari anggota baru')
else:
    print('Anggota sudah terpenuhi, silahkan dilanjutkan pencucianya')

if panjang < 100:
    print('Belum terpenuhi syarat menjadi anggota')
elif panjang >= 200:
    print('Sudah terpenuhi syarat menjadi anggota')
else:
    print('Lanjutkan')

for i in range(2, 3, 10):
    print(message)


while jumlah > 1:
    print('Jumlah saat ini %s' % jumlah)
    print('Masih Mencukupi')
    jumlah = jumlah - 1


daftar_anggota = []
print(daftar_anggota)
daftar_anggota.append('Joko')
daftar_anggota.append('Juki')
daftar_anggota.append('Jiko')
daftar_anggota.append('Jaka')
daftar_anggota.append('Jojo')
print(daftar_anggota)

for da in daftar_anggota:
    print('Daftar nama anggota bumi data %s, ' % (da))


manusia = {}
manusia['nama'] = 'Prabowo'
manusia['sex'] = 'Laki-laki'
manusia['status'] = 'Duda'
print(manusia)
manusia['nama'] = 'Prabowo Widodo'
print(manusia)
manusia['alamat'] = 'Jakarta'
print(manusia)


import json
print(json.dumps(manusia))  #dumps itu membuang