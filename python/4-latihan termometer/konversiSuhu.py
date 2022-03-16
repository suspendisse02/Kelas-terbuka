print('\nProgram Konversi Temperatur\n')

celcius = float(input('Masukkan suhu dalam celcius : '))
print('suhu adalah ', celcius, 'Celcius')

reamur = 4/5 * celcius
print('suhu dalam reamur adalah ', reamur, 'Reamur')

fahrenheit = 9/5*celcius + 32
print('suhu dalam fahrenheit adalah ', fahrenheit, 'Reamur')
# Pr fahrenheit ke kelvin
fahrenheit_2 = float(input('Masukkan suhu dalam fahrenheit :'))
kelvin_3 = float(input('Masukkan suhu dalam Kelvin :'))

print(fahrenheit_2)
print(kelvin_3)
Kelvin_2 = (5/9)*((fahrenheit_2-32.0)+273.0)
print('F to K: ', Kelvin_2)

fahrenheit_3 = 9/5*(kelvin_3-273.0)+32.0

print('K to F: ', fahrenheit_3)

kelvin = celcius + 273
print('suhu dalam kelvin adalah ', kelvin, 'Reamur')
