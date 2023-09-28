#mengimport random module untuk membuat kumpulan data random yang berupa angka
import random

#membuat data yang masih kosong
data = []
#menginput jumlah data yang diinginkan user kemudian di simpan di variabel n
n = int(input('jumlah data yang diinginkan:'))
#membuat perulangan untuk mengisi data dengan angka random sebanyak n buah
for i in range(n):
    #menambahkan angka random ke dalam data kosong dari range 0 sampai 100
    #menggunakan fungsi append
    data.append(random.randint(0, 100))

#memunculkan kumpulan data
print(' ')
print('Data :')
print(data)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0

#menghitung/mengidentifikasi banyaknya frekuensi data dari tiap rentang nilai
for x in data:
    if 0 <= x <= 10:
        a = a + 1
    elif  11 <= x <= 20:
        b = b + 1
    elif 21 <= x <= 30:
        c = c + 1
    elif 31 <= x <= 40:
        d = d + 1
    elif 41 <= x <= 50:
        e = e + 1
    elif 51 <= x <= 60:
        f = f + 1
    elif 61 <= x <= 70:
        g = g + 1
    elif 71 <= x <= 80:
        h = h + 1
    elif 81 <= x <= 90:
        i = i + 1
    elif 91 <= x <= 100:
        j = j + 1

#membuat grafik distribusi frekuensi dengan karakter bintang (*)
print(' ')
print('Distribusi Frekuensi')
print('====================')
print('Nilai 0 - 10: '+'*'*(a))
print('Nilai 11 - 20: '+'*'*(b))
print('Nilai 21 - 30: '+'*'*(c))
print('Nilai 31 - 40: '+'*'*(d))
print('Nilai 41 - 50: '+'*'*(e))
print('Nilai 51 - 60: '+'*'*(f))
print('Nilai 61 - 70: '+'*'*(g))
print('Nilai 71 - 80: '+'*'*(h))
print('Nilai 81 - 90: '+'*'*(i))
print('Nilai 91 - 100: '+'*'*(j))
