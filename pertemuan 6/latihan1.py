barang = int(input("Masukan jumlah barang :"))

if barang < 100 : 
    harga = 5000
elif barang >= 100 : 
    harga = 4000
elif barang > 150 : 
    harga = 2500

jumlah = barang*harga 
print(f"total harga barang {barang} barang adalah {jumlah}")
# Saifulloh Fattah Bintoro_2408256