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
    
## Nilai Filsafat 2 ##

### All data
dataFrame = pd.read_excel('Tugas08_NilaiFilsafat2_LENGKAP.xlsx') 
HM_count = dataFrame['HM'].value_counts()

## Letter Grade
# Table
dataTable = pd.DataFrame(HM_count).reset_index()
fig, ax = plt.subplots(1, 2, figsize=(8, 8))
ax[0].axis('off')
table = ax[0].table(cellText=dataTable.values, colLabels=dataTable.columns.values,
                    loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
ax[0].set_title('Tabel Huruf Mutu Filsafat 2')

# Pie Chart
ax[1].axis('off')
ax[1].pie(HM_count, labels=HM_count.index, 
        autopct='%.2f%%', 
        colors=plt.cm.Paired.colors)
ax[1].set_title('Pie Chart Huruf Mutu Filsafat 2')

# Showing the figures
plt.tight_layout()
plt.show()


## GPA
dataFrame['Angka Mutu'] = dataFrame['HM'].apply(indexVal)
indexAll = dataFrame['Angka Mutu'].mean().round(2)
print('Indeks Prestasi Seluruh Kelas Pertanian Filsafat 2: ', indexAll)


### Per class
## GPA
indexPerClass = dataFrame.groupby('Kelas')['Angka Mutu'].mean().round(2)

# making the table and the bar chart
classTableData = pd.DataFrame(indexPerClass).reset_index()
fig, ax = plt.subplots(figsize=(8, 6))

# class table data
ax.axis('off')
table = ax.table(cellText=classTableData.values, colLabels=classTableData.columns.values,
                    loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(0.8, 0.8)
ax.set_title('Tabel Huruf Indeks Prestasi per Kelas')
plt.show() 

# bar chart
plt.bar(indexPerClass.index, indexPerClass.values)
plt.title('Bar Chart rata-rata indeks prestasi per kelas')
plt.xlabel('Kelas')
plt.ylabel('Rata-rata indeks prestasi')
plt.xticks(rotation=45)
plt.show() # showed the table and bar chart seperately because of the size 

## Letter Grade
classIndex = dataFrame['Kelas'].unique()
for kelas in classIndex:

    # Table
    fig, ax = plt.subplots(1, 2, figsize=(8, 8))
    ax[0].axis('off')
    table = ax[0].table(cellText=dataFrame[dataFrame['Kelas'] == kelas]['HM'].value_counts().reset_index().values, 
                        colLabels=['HM', 'Jumlah'], loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    ax[0].set_title(f'Tabel Huruf Mutu Filsafat 2 ({kelas})')

    # Pie Chart
    ax[1].axis('off')
    ax[1].pie(dataFrame[dataFrame['Kelas'] == kelas]['HM'].value_counts(), 
            labels=dataFrame[dataFrame['Kelas'] == kelas]['HM'].value_counts().index, 
            autopct='%.2f%%', 
            colors=plt.cm.Paired.colors)
    ax[1].set_title(f'Pie Chart Huruf Mutu Filsafat 2 ({kelas})')

    # Showing the figures
    plt.tight_layout()
    plt.show()