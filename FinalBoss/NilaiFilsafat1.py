import pandas as pd
import matplotlib.pyplot as plt

def indexVal(val):
    if val == 'A':
        return 4
    elif val == 'AB':
        return 3.5
    elif val == 'B':
        return 3
    elif val == 'BC':
        return 2.5
    elif val == 'C':
        return 2
    elif val == 'D':
        return 1
    elif val == 'E':
        return 0


### NilaiFfilsafat1 ###

# reading data
dataFrame = pd.read_excel('Tugas08_NilaiFilsafat1_LENGKAP.xlsx')
HM_count = dataFrame['HM'].value_counts()
dataTable = pd.DataFrame(HM_count).reset_index()


# pie chart
fig, ax = plt.subplots(1, 2, figsize=(6, 6))
ax[0].axis('off')
ax[0].pie(HM_count, labels=HM_count.index, 
        autopct='%.2f%%', 
        colors=plt.cm.Paired.colors)
ax[0].set_title('Pie Chart Huruf Mutu Filsafat 1')

# table
ax[1].axis('off')
table = ax[1].table(cellText=dataTable.values, colLabels=dataTable.columns.values,
                    loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
ax[1].set_title('Tabel Huruf Mutu Filsafat 1')


# showing the figures
plt.tight_layout()
plt.show()


# Sorting data
dataFrame['Angka Mutu'] = dataFrame['HM'].apply(indexVal)
indexAll = dataFrame['Angka Mutu'].mean().round(2)
print('Indeks Prestasi Seluruh Kelas Pertanian Filsafat 1: ', indexAll)

# GPA per class
indexperClass = dataFrame.groupby('Kelas')['Angka Mutu'].mean().round(2)

# making the table and the bar chart
classTableData = pd.DataFrame(indexperClass).reset_index()
fig, ax = plt.subplots(1, 2, figsize=(6, 6))

# class table data
ax[0].axis('off')
table = ax[0].table(cellText=classTableData.values, colLabels=classTableData.columns.values,
                    loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
ax[0].set_title('Tabel Huruf Indeks Prestasi per Kelas')

# bar chart
ax[1].bar(indexperClass.index, indexperClass.values)
ax[1].set_title('Bar Chart rata-rata indeks prestasi per kelas')
ax[1].set_xlabel('Kelas')
ax[1].set_ylabel('Rata-rata indeks prestasi')

plt.show()
