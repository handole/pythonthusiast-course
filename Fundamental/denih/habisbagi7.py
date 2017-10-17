def habisbagi(angkawal,angkakhir):
    for angkawal in range(angkawal, angkakhir):
        if angkawal%5==0 and angkawal%7==0:
           return angkawal

angkawal=input('Masukkan angkawal:')
angkakhir=input('Masukkan angkakhir:')
print(habisbagi(angkawal,angkakhir))