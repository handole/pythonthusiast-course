siswa = [
    {'nama': 'Joko'},
    {'nama': 'Komo'},
    {'nama': 'Geri'},
    {'nama': 'Joko'},
    {'nama': 'Geri'}
]

tampung = []

for murid in siswa:
    if murid not in tampung:
        tampung.append(murid)

print(tampung)