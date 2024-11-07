n=10
jumlah=0
hasil = ""
# for i in range(1, n + 1) : 
#     print(f"angka sekarang: {i}", f"penjumlahan dari: {jumlah}+{i}",  "adalah: ", jumlah+i )
#     jumlah+=i
# print("total dari hasil looping: ", jumlah)

for i in range(1, n + 1):
    jumlah += i
    if i == n:
        hasil += f"{i}"
    else:
        hasil += f"{i} + "
print(f"{hasil} = {jumlah}")
print("total dari hasil looping: ", jumlah)
# saifulloh fattah bintoro_2408256