def celciustofahrenheit(celcius):
    fahrenheit=(9.0/5.0*celcius)+32.0
    print(fahrenheit)


def fahrenheitocelcius(fahrenheit):
    celcius=(5.0/9.0)*(fahrenheit-32.0)
    print(celcius)


ctf = celciustofahrenheit
ftc = fahrenheitocelcius

suhu=input('Masukkan suhu:')
konversi = 'Masukkkan tipe suhu:'

if konversi=='c':
   fahrenheitocelcius(suhu)
   print('Adalah suhu Celcius')
else:
   celciustofahrenheit(suhu)
   print('Adalah suhu Fahrenheit')

# celcius=input('Masukkan angka celcius:')
# celciustofahrenheit(float(celcius))

# fahrenheit=input('Masukkan angka fahrenheit:')
# fahrenheitocelcius(float(fahrenheit))

