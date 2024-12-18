def cek_stok(stok, barang):
    for item in stok:
        if item.lower() == barang.lower():
            return True
    return False

barang = [
    "Laptop", "Keyboard", "Mouse", "Monitor", "Printer",
    "Tws", "Speaker", "Headset", "Webcam", "Router",
    "Handphone", "Tablet", "Power bank", "Ssd", "Hdd"
]

barang_dicari = input("Masukkan nama barang yang dicari: ")

if cek_stok(barang, barang_dicari):
    print(f"Barang '{barang_dicari}' tersedia di stok toko.")
else:
    print(f"Barang '{barang_dicari}' tidak tersedia di stok toko.")
# saifulloh fattah bintoro_2408256