import pandas  as pd

csvFile = pd.read_csv("pertemuan 14/tugas/DataMahasiswa.csv")
df = pd.DataFrame(csvFile)
# # urutkan = df.sort_values(by='Nama')

# selected_columns = ['NIM', 'Nama', 'L/P', 'Status', 'SKS', 'IP', 'Lama Studi(Smt)']
# urutkan_kolom = csvFile[selected_columns]

# # print(df.head(10))
# # print(urutkan.head(10))
# print(urutkan_kolom)

# selected_columns = ['NIM', 'Nama', 'L/P', 'Status', 'SKS', 'IPK', 'Lama Studi(Smt)']
# filtered_df = df[selected_columns]

# average_ipk = filtered_df['IPK'].mean()

# print("Nilai rata rata IPK:")
# print(average_ipk)

# gender_counts = df['L/P'].value_counts()
# laki = gender_counts.get('L', 0)
# cewe = gender_counts.get('P', 0)

# print("jumlah mahasiswa laki laki:", laki)
# print("jumlah mahasiswa perempuan:", cewe)

# urutkan = df[(df['L/P'] == 'P') & (df['Status'] == 'Terdaftar')]

# print("Data mahasiswi perempuan dengan status terdaftar:")
# print(urutkan)

m = df[df['Status'] != 'Terdaftar']

print("Data mahasiswi perempuan dengan status bukan terdaftar:")
print(m)