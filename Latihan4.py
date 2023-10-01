print()
print('  _______       ____  ______ _        _   _ _____ _               _____') 
print(' |__   __|/\   |  _ \|  ____| |      | \ | |_   _| |        /\   |_   _|')
print('    | |  /  \  | |_| | |__  | |      |  \| | | | | |       /  \    | | ') 
print('    | | / /\ \ |  _ <|  __| | |      | . ` | | | | |      / /\ \   | | ') 
print('    | |/ ____ \| |_| | |____| |____  | |\  |_| |_| |____ / ____ \ _| |_ ')
print('    |_/_/    \_\____/|______|______| |_| \_|_____|______/_/    \_\_____|')
print()                                                                        


import math

def hitung_nAkhir(uts, uas):
    'menghitung rata-rata per individu'
    return (uts + uas) / 2


def tampil_data(nim, nama, kelompok, uts, uas, nAkhir, hMutu):
    'menampilkan tabel data'
    print('{:<13}{:<45}{:<15}{:<8}{:<8}{:<18}{:<8}'.format('[NIM]', '[NAMA]', '[KELOMPOK]', '[UTS]', '[UAS]', '[NILAI AKHIR]', '[HURUF MUTU]'))
    for i in range(len(nim)):
        print('{:<13}{:<45}{:<15}{:<8}{:<8}{:<18}{:<8}'.format(nim[i], nama[i], kelompok[i], uts[i], uas[i], nAkhir[i], hMutu[i]))

#                           Huruf Mutu  Angka Mutu
#--------------------------------------------------
#  0 <= nilai akhir < 25         E          0
# 25 <= nilai akhir < 40         D          1
# 40 <= nilai akhir < 60         C          2
# 60 <= nilai akhir < 80         B          3
# 80 <= nilai akhir < 100        A          4
#--------------------------------------------------
def hitung_hMutu(nAkhir):
    mutu_mapping = {
        4: 'A',
        3: 'B',
        2: 'C',
        1: 'D',
        0: 'E'
    }
    return mutu_mapping[min(4, max(0, int(nAkhir) // 20))]


def ratarata(nilai):
    'menghitung rata-rata'
    jum = 0
    for i in range(len(nilai)):
        jum += nilai[i]
    mean = jum / len(nilai)
    return round(mean, 2)

def stDev(data, mean):
    'menghitung standar deviasi kumpulan data'
    ragam = sum((i - mean)**2 for i in data)/len(data)
    return round(math.sqrt(ragam), 2)


infile = open(r'''D:\Abel's stuff\Code\Python\Latihan 4\NilaiUTS-UAS_prediksi.csv''')
# Deklarasi Variabel
nim = []
nama = []
kel = []
uts = []
uas = []
nAkhir = []
hMutu = []
listVar = []

nilaiA = []
nilaiB = []
nilaiC = []
nilaiD = []
nilaiE = []
nilaiF = []
nilaiG = []
nilaiH = []
nilaiI = []

brs = infile.readline()
while True:
    brs = infile.readline()
    if brs == '':
        break
    brs = brs.strip().split(',')
    nim.append(brs[0])
    nama.append(brs[1])
    kel.append(brs[2])
    uts.append(int(brs[3]))
    uas.append(int(brs[4]))
    nAkhir.append(hitung_nAkhir(int(brs[3]), int(brs[4])))
    hMutu.append('')

# Lengkapi kolom huruf mutu
for i in range(len(nAkhir)):
    hMutu[i] = hitung_hMutu(nAkhir[i])

# Tampilkan datanya
tampil_data(nim, nama, kel, uts, uas, nAkhir, hMutu)


#Hitung Statistik nakhir, uts, dan uas
#Ini buat UTS
## Input nilai akhir per fakultas
for i in range(len(nim)):
    if nim[i][0] == 'A':
        nilaiA.append(uts[i])
    elif nim[i][0] == 'B':
        nilaiB.append(uts[i])
    elif nim[i][0] == 'C':
        nilaiC.append(uts[i])
    elif nim[i][0] == 'D':
        nilaiD.append(uts[i])
    elif nim[i][0] == 'E':
        nilaiE.append(uts[i])
    elif nim[i][0] == 'F':
        nilaiF.append(uts[i])
    elif nim[i][0] == 'G':
        nilaiG.append(uts[i])
    elif nim[i][0] == 'H':
        nilaiH.append(uts[i])
    elif nim[i][0] == 'I':
        nilaiI.append(uts[i])

## ini nilai rata-rata per fakultas
nUtsA = ratarata(nilaiA)
nUtsB = ratarata(nilaiB)
nUtsC = ratarata(nilaiC)
nUtsD = ratarata(nilaiD)
nUtsE = ratarata(nilaiE)
nUtsF = ratarata(nilaiF)
nUtsG = ratarata(nilaiG)
nUtsH = ratarata(nilaiH)
nUtsI = ratarata(nilaiI) 

##ini buat stdev
stdevUtsA = stDev(nilaiA, nUtsA)
stdevUtsB = stDev(nilaiB, nUtsB)
stdevUtsC = stDev(nilaiC, nUtsC)
stdevUtsD = stDev(nilaiD, nUtsD)
stdevUtsE = stDev(nilaiE, nUtsE)
stdevUtsF = stDev(nilaiF, nUtsF)
stdevUtsG = stDev(nilaiG, nUtsG)
stdevUtsH = stDev(nilaiH, nUtsH)
stdevUtsI = stDev(nilaiI, nUtsI)

##ini buat min
minUtsA = min(nilaiA)
minUtsB = min(nilaiB)
minUtsC = min(nilaiC)
minUtsD = min(nilaiD)
minUtsE = min(nilaiE)
minUtsF = min(nilaiF)
minUtsG = min(nilaiG)
minUtsH = min(nilaiH)
minUtsI = min(nilaiI)

##ini buat max
maxUtsA = max(nilaiA)
maxUtsB = max(nilaiB)
maxUtsC = max(nilaiC)
maxUtsD = max(nilaiD)
maxUtsE = max(nilaiE)
maxUtsF = max(nilaiF)
maxUtsG = max(nilaiG)
maxUtsH = max(nilaiH)
maxUtsI = max(nilaiI)

##ini buat keseluruhan IPB
meanUtsIPB = ratarata(uts)
stdevUtsIPB = stDev(uts, meanUtsIPB)
maxUtsIPB = max(uts)
minUtsIPB = min(uts)

##reset list
nilaiA = []
nilaiB = []
nilaiC = []
nilaiD = []
nilaiE = []
nilaiF = []
nilaiG = []
nilaiH = []
nilaiI = []


#Ini buat UAS
## Input nilai akhir per fakultas
for i in range(len(nim)):
    if nim[i][0] == 'A':
        nilaiA.append(uas[i])
    elif nim[i][0] == 'B':
        nilaiB.append(uas[i])
    elif nim[i][0] == 'C':
        nilaiC.append(uas[i])
    elif nim[i][0] == 'D':
        nilaiD.append(uas[i])
    elif nim[i][0] == 'E':
        nilaiE.append(uas[i])
    elif nim[i][0] == 'F':
        nilaiF.append(uas[i])
    elif nim[i][0] == 'G':
        nilaiG.append(uas[i])
    elif nim[i][0] == 'H':
        nilaiH.append(uas[i])
    elif nim[i][0] == 'I':
        nilaiI.append(uas[i])

## ini nilai rata-rata per fakultas
nUasA = ratarata(nilaiA)
nUasB = ratarata(nilaiB)
nUasC = ratarata(nilaiC)
nUasD = ratarata(nilaiD)
nUasE = ratarata(nilaiE)
nUasF = ratarata(nilaiF)
nUasG = ratarata(nilaiG)
nUasH = ratarata(nilaiH)
nUasI = ratarata(nilaiI) 

##ini buat stdev
stdevUasA = stDev(nilaiA, nUasA)
stdevUasB = stDev(nilaiB, nUasB)
stdevUasC = stDev(nilaiC, nUasC)
stdevUasD = stDev(nilaiD, nUasD)
stdevUasE = stDev(nilaiE, nUasE)
stdevUasF = stDev(nilaiF, nUasF)
stdevUasG = stDev(nilaiG, nUasG)
stdevUasH = stDev(nilaiH, nUasH)
stdevUasI = stDev(nilaiI, nUasI)

##ini buat min
minUasA = min(nilaiA)
minUasB = min(nilaiB)
minUasC = min(nilaiC)
minUasD = min(nilaiD)
minUasE = min(nilaiE)
minUasF = min(nilaiF)
minUasG = min(nilaiG)
minUasH = min(nilaiH)
minUasI = min(nilaiI)

##ini buat max
maxUasA = max(nilaiA)
maxUasB = max(nilaiB)
maxUasC = max(nilaiC)
maxUasD = max(nilaiD)
maxUasE = max(nilaiE)
maxUasF = max(nilaiF)
maxUasG = max(nilaiG)
maxUasH = max(nilaiH)
maxUasI = max(nilaiI)

##ini buat keseluruhan IPB
meanUasIPB = ratarata(uas)
stdevUasIPB = stDev(uas, meanUasIPB)
maxUasIPB = max(uas)
minUasIPB = min(uas)

##reset list
nilaiA = []
nilaiB = []
nilaiC = []
nilaiD = []
nilaiE = []
nilaiF = []
nilaiG = []
nilaiH = []
nilaiI = []

#Ini buat nilai akhir
## Input nilai akhir per fakultas
for i in range(len(nim)):
    if nim[i][0] == 'A':
        nilaiA.append(nAkhir[i])
    elif nim[i][0] == 'B':
        nilaiB.append(nAkhir[i])
    elif nim[i][0] == 'C':
        nilaiC.append(nAkhir[i])
    elif nim[i][0] == 'D':
        nilaiD.append(nAkhir[i])
    elif nim[i][0] == 'E':
        nilaiE.append(nAkhir[i])
    elif nim[i][0] == 'F':
        nilaiF.append(nAkhir[i])
    elif nim[i][0] == 'G':
        nilaiG.append(nAkhir[i])
    elif nim[i][0] == 'H':
        nilaiH.append(nAkhir[i])
    elif nim[i][0] == 'I':
        nilaiI.append(nAkhir[i])

## ini nilai rata-rata per fakultas
nAkhirA = ratarata(nilaiA)
nAkhirB = ratarata(nilaiB)
nAkhirC = ratarata(nilaiC)
nAkhirD = ratarata(nilaiD)
nAkhirE = ratarata(nilaiE)
nAkhirF = ratarata(nilaiF)
nAkhirG = ratarata(nilaiG)
nAkhirH = ratarata(nilaiH)
nAkhirI = ratarata(nilaiI) 

##ini buat stdev
stdevAkhirA = stDev(nilaiA, nAkhirA)
stdevAkhirB = stDev(nilaiB, nAkhirB)
stdevAkhirC = stDev(nilaiC, nAkhirC)
stdevAkhirD = stDev(nilaiD, nAkhirD)
stdevAkhirE = stDev(nilaiE, nAkhirE)
stdevAkhirF = stDev(nilaiF, nAkhirF)
stdevAkhirG = stDev(nilaiG, nAkhirG)
stdevAkhirH = stDev(nilaiH, nAkhirH)
stdevAkhirI = stDev(nilaiI, nAkhirI)

##ini buat min
minAkhirA = min(nilaiA)
minAkhirB = min(nilaiB)
minAkhirC = min(nilaiC)
minAkhirD = min(nilaiD)
minAkhirE = min(nilaiE)
minAkhirF = min(nilaiF)
minAkhirG = min(nilaiG)
minAkhirH = min(nilaiH)
minAkhirI = min(nilaiI)

##ini buat max
maxAkhirA = max(nilaiA)
maxAkhirB = max(nilaiB)
maxAkhirC = max(nilaiC)
maxAkhirD = max(nilaiD)
maxAkhirE = max(nilaiE)
maxAkhirF = max(nilaiF)
maxAkhirG = max(nilaiG)
maxAkhirH = max(nilaiH)
maxAkhirI = max(nilaiI)

##ini buat keseluruhan IPB
meanAkhirIPB = ratarata(nAkhir)
stdevAkhirIPB = stDev(nAkhir, meanAkhirIPB)
maxAkhirIPB = max(nAkhir)
minAkhirIPB = min(nAkhir)


#ini buat nampilin datanya
##ini buat uts
print("\n------------------------")
print("Statistik UTS")
print("------------------------")
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas/Sekolah", "Jumlah Mahasiswa", "Rata-rata", "St.Deviasi","Minimum","Maksimum"))
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Pertanian", len(nilaiA), nUtsA,stdevUtsA,minUtsA,maxUtsA))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Sekolah Kedokteran Hewan dan Biomedis", len(nilaiB), nUtsB,stdevUtsB,minUtsB,maxUtsB))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Perikanan dan Ilmu Kelautan", len(nilaiC), nUtsC,stdevUtsC,minUtsC,maxUtsC))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Peternakan", len(nilaiD), nUtsD,stdevUtsD,minUtsD,maxUtsD))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Kehutanan dan Lingkungan", len(nilaiE), nUtsE,stdevUtsE,minUtsE,maxUtsE))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Teknologi Pertanian", len(nilaiF), nUtsF,stdevUtsF,minUtsF,maxUtsF))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Matematika dan Ilmu Pengetahuan Alam", len(nilaiG), nUtsG,stdevUtsG,minUtsG,maxUtsG))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekonomi dan Manajemen", len(nilaiH), nUtsH,stdevUtsH,minUtsH,maxUtsH))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekologi Manusia", len(nilaiI), nUtsI,stdevUtsI,minUtsI,maxUtsI))
print("-"*103)
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}\n".format("IPB University", len(uts), meanUtsIPB,stdevUtsIPB,minUtsIPB,maxUtsIPB))

##ini buat uas
print("\n------------------------")
print("Statistik UAS")
print("------------------------")
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas/Sekolah", "Jumlah Mahasiswa", "Rata-rata", "St.Deviasi","Minimum","Maksimum"))
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Pertanian", len(nilaiA), nUasA,stdevUasA,minUasA,maxUasA))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Sekolah Kedokteran Hewan dan Biomedis", len(nilaiB), nUasB,stdevUasB,minUasB,maxUasB))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Perikanan dan Ilmu Kelautan", len(nilaiC), nUasC,stdevUasC,minUasC,maxUasC))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Peternakan", len(nilaiD), nUasD,stdevUasD,minUasD,maxUasD))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Kehutanan dan Lingkungan", len(nilaiE), nUasE,stdevUasE,minUasE,maxUasE))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Teknologi Pertanian", len(nilaiF), nUasF,stdevUasF,minUasF,maxUasF))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Matematika dan Ilmu Pengetahuan Alam", len(nilaiG), nUasG,stdevUasG,minUasG,maxUasG))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekonomi dan Manajemen", len(nilaiH), nUasH,stdevUasH,minUasH,maxUasH))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekologi Manusia", len(nilaiI), nUasI,stdevUasI,minUasI,maxUasI))
print("-"*103)
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}\n".format("IPB University", len(uas), meanUasIPB,stdevUasIPB,minUasIPB,maxUasIPB))

##ini buat Nliai Akhir
print("\n------------------------")
print("Statistik Nilai Akhir")
print("------------------------")
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas/Sekolah", "Jumlah Mahasiswa", "Rata-rata", "St.Deviasi","Minimum","Maksimum"))
print("{:47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Pertanian", len(nilaiA), nAkhirA,stdevAkhirA,minAkhirA,maxAkhirA))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Sekolah Kedokteran Hewan dan Biomedis", len(nilaiB), nAkhirB,stdevAkhirB,minAkhirB,maxAkhirB))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Perikanan dan Ilmu Kelautan", len(nilaiC), nAkhirC,stdevAkhirC,minAkhirC,maxAkhirC))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Peternakan", len(nilaiD), nUasD,stdevAkhirD,minAkhirD,maxAkhirD))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Kehutanan dan Lingkungan", len(nilaiE), nAkhirE,stdevAkhirE,minAkhirE,maxAkhirE))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Teknologi Pertanian", len(nilaiF), nAkhirF,stdevAkhirF,minAkhirF,maxAkhirF))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Matematika dan Ilmu Pengetahuan Alam", len(nilaiG), nAkhirG,stdevAkhirG,minAkhirG,maxAkhirG))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekonomi dan Manajemen", len(nilaiH), nAkhirH,stdevAkhirH,minAkhirH,maxAkhirH))
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}".format("Fakultas Ekologi Manusia", len(nilaiI), nAkhirI,stdevAkhirI,minAkhirI,maxAkhirI))
print("-"*103)
print("{:<47}{:<18}{:<11}{:<12}{:<9}{:<10}\n".format("IPB University", len(nAkhir), meanAkhirIPB,stdevAkhirIPB,minAkhirIPB,maxAkhirIPB))



# Membuat dictionary untuk huruf mutu setiap fakultas
hurufMutuCounts = {
    'A': {'Fakultas Pertanian': 0, 'Sekolah Kedokteran dan Biomedis': 0, 'Fakultas Perikanan dan Ilmu Kelautan': 0, 'Fakultas Peternakan': 0, 'Fakultas Kehutanan dan Lingkungan': 0, 'Fakultas Teknologi Pertanian': 0, 'Fakultas Matematika dan Ilmu Pengetahuan Alam': 0, 'Fakultas Ekonomi dan Manajemen': 0, 'Fakultas Ekologi Manusia': 0},
    'B': {'Fakultas Pertanian': 0, 'Sekolah Kedokteran dan Biomedis': 0, 'Fakultas Perikanan dan Ilmu Kelautan': 0, 'Fakultas Peternakan': 0, 'Fakultas Kehutanan dan Lingkungan': 0, 'Fakultas Teknologi Pertanian': 0, 'Fakultas Matematika dan Ilmu Pengetahuan Alam': 0, 'Fakultas Ekonomi dan Manajemen': 0, 'Fakultas Ekologi Manusia': 0},
    'C': {'Fakultas Pertanian': 0, 'Sekolah Kedokteran dan Biomedis': 0, 'Fakultas Perikanan dan Ilmu Kelautan': 0, 'Fakultas Peternakan': 0, 'Fakultas Kehutanan dan Lingkungan': 0, 'Fakultas Teknologi Pertanian': 0, 'Fakultas Matematika dan Ilmu Pengetahuan Alam': 0, 'Fakultas Ekonomi dan Manajemen': 0, 'Fakultas Ekologi Manusia': 0},
    'D': {'Fakultas Pertanian': 0, 'Sekolah Kedokteran dan Biomedis': 0, 'Fakultas Perikanan dan Ilmu Kelautan': 0, 'Fakultas Peternakan': 0, 'Fakultas Kehutanan dan Lingkungan': 0, 'Fakultas Teknologi Pertanian': 0, 'Fakultas Matematika dan Ilmu Pengetahuan Alam': 0, 'Fakultas Ekonomi dan Manajemen': 0, 'Fakultas Ekologi Manusia': 0},
    'E': {'Fakultas Pertanian': 0, 'Sekolah Kedokteran dan Biomedis': 0, 'Fakultas Perikanan dan Ilmu Kelautan': 0, 'Fakultas Peternakan': 0, 'Fakultas Kehutanan dan Lingkungan': 0, 'Fakultas Teknologi Pertanian': 0, 'Fakultas Matematika dan Ilmu Pengetahuan Alam': 0, 'Fakultas Ekonomi dan Manajemen': 0, 'Fakultas Ekologi Manusia': 0}
}

# Menghitung huruf mutu setiap fakultas
for i in range(len(nim)):
    huruf_mutu = hMutu[i]
    fakultas = nim[i][0]
    if fakultas == 'A':
        fakultas = 'Fakultas Pertanian'
    elif fakultas == 'B':
        fakultas = 'Sekolah Kedokteran dan Biomedis'
    elif fakultas == 'C':
        fakultas = 'Fakultas Perikanan dan Ilmu Kelautan'
    elif fakultas == 'D':
        fakultas = 'Fakultas Peternakan'
    elif fakultas == 'E':
        fakultas = 'Fakultas Kehutanan dan Lingkungan'
    elif fakultas == 'F':
        fakultas = 'Fakultas Teknologi Pertanian'
    elif fakultas == 'G':
        fakultas = 'Fakultas Matematika dan Ilmu Pengetahuan Alam'
    elif fakultas == 'H':
        fakultas = 'Fakultas Ekonomi dan Manajemen'
    elif fakultas == 'I':
        fakultas = 'Fakultas Ekologi Manusia'
    hurufMutuCounts[huruf_mutu][fakultas] += 1

# Pendefinisian nilai huruf mutu
values_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

# Membuat dictionary untuk penjumlahan setiap nilai fakultas
sum_values_per_fakultas = {}

# Membuat dictionary untuk jumlah mahasiswa setiap fakultas
count_data_per_fakultas = {}

# Melakukan for loop untuk setiap fakultas
for fakultas in hurufMutuCounts['A']:
    sum_fakultas = 0
    count_fakultas = 0
    
    # Melakukan for loop untuk setiap huruf mutu
    for huruf_mutu, count in hurufMutuCounts.items():
        sum_fakultas += count[fakultas] * values_mapping[huruf_mutu]  # Mencari penjumlahan IP
        count_fakultas += count[fakultas]
    
    # Menyetor penjumlahan tersebut ke dalam variabel untuk setiap fakultas
    sum_values_per_fakultas[fakultas] = sum_fakultas
    
    # Menyetor penjumlahan mahasiswa untuk setiap fakultas
    count_data_per_fakultas[fakultas] = count_fakultas

# Tabel output
print("\n-----------------------------")
print("Jumlah Huruf Mutu per Fakultas")
print("-------------------------------")
print("{:50}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format("Fakultas/Sekolah", 'A', 'B', 'C', 'D', 'E', 'Indeks Prestasi'))
for fakultas in hurufMutuCounts['A']:
    counts = [hurufMutuCounts[huruf_mutu][fakultas] for huruf_mutu in ['A', 'B', 'C', 'D', 'E']]
    sum_value = sum_values_per_fakultas[fakultas]
    count_fakultas = count_data_per_fakultas[fakultas]
    average_value = sum_value / count_fakultas
    print("{:50}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(fakultas, *counts, round(average_value,2)))
print("-" * 100)
