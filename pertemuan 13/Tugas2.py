import csv

with open("inventaris_barang.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows()

def update_stok(nama_barang, perubahan):
    try:
        with open("inventaris_barang.csv", "r") as file:
            reader = csv.reader(file)
            data = list(reader)
        for row in data:
            if row[0] == nama_barang:
                row[1] = str(int(row[1]) + perubahan)
                print(f"Stok {nama_barang} berhasil diupdate menjadi {row[1]}")
                break
        else:
            print(f"Barang '{nama_barang}' tidak ditemukan.")
        with open("inventaris_barang.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    except FileNotFoundError:
        print("File inventaris_barang.csv tidak ditemukan.")

update_stok("Pulpen", -20)
update_stok("Laptop", 5)
# saifulloh fattah bintoro_2408256