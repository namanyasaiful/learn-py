import csv
import os

def baca_inventaris(file_path):
    inventaris = []
    if not os.path.exists(file_path):  # Cek apakah file ada
        print(f"File '{file_path}' tidak ditemukan. Pastikan file ada di direktori yang benar.")
        return inventaris

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventaris.append({'Nama Barang': row['Nama Barang'], 'Stok': int(row['Stok'])})
    except KeyError:
        print("File CSV tidak memiliki kolom yang sesuai (Nama Barang, Stok).")
    except ValueError:
        print("File CSV memiliki nilai yang tidak valid (Stok harus berupa angka).")
    return inventaris

def tulis_inventaris(file_path, data):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Nama Barang', 'Stok']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def update_stok(inventaris):
    nama_barang = input("Masukkan nama barang: ")
    operasi = input("Apakah Anda ingin menambah (pengiriman) atau mengurangi (penjualan) stok? (pengiriman/penjualan): ").strip().lower()
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    for item in inventaris:
        if item['Nama Barang'].lower() == nama_barang.lower():
            if operasi == 'pengiriman':
                item['Stok'] += jumlah
                print(f"Stok barang '{nama_barang}' berhasil ditambahkan.")
            elif operasi == 'penjualan':
                if jumlah <= item['Stok']:
                    item['Stok'] -= jumlah
                    print(f"Stok barang '{nama_barang}' berhasil dikurangi.")
                else:
                    print("Stok tidak mencukupi!")
            else:
                print("Operasi tidak valid!")
            break
    else:
        print("Barang tidak ditemukan!")

file_path = 'inventaris_barang.csv'
inventaris = baca_inventaris(file_path)

while True:
    print("\n=== Menu ===")
    print("1. Lihat Inventaris")
    print("2. Update Stok")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        if not inventaris:
            print("Data inventaris kosong.")
        else:
            for item in inventaris:
                print(f"{item['Nama Barang']}: {item['Stok']}")
    elif pilihan == '2':
        update_stok(inventaris)
        tulis_inventaris(file_path, inventaris)
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")
# saifulloh fattah bintoro_2408256