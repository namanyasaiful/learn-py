import csv

try:
    # Baca file CSV
    with open("inventaris_barang.csv", "r") as file:
        reader = csv.reader(file)
        # Periksa jika file kosong
        try:
            header = next(reader)  # Ambil header
        except StopIteration:
            print("File 'inventaris_barang.csv' kosong.")
            exit()

        data = [row for row in reader if len(row) >= 4]  # Hanya ambil baris yang valid

    # Update data dengan stok akhir
    updated_data = []
    for row in data:
        try:
            stok_awal = int(row[1])       # Kolom 2: Stok Awal
            pengiriman = int(row[2])     # Kolom 3: Pengiriman
            penjualan = int(row[3])      # Kolom 4: Penjualan
            stok_akhir = stok_awal + pengiriman - penjualan
            row.append(stok_akhir)       # Tambahkan Stok Akhir ke baris
            updated_data.append(row)
        except ValueError:
            print(f"Baris memiliki nilai tidak valid: {row}")

    # Tambahkan header baru
    header.append("Stok Akhir")

    # Tulis kembali ke file
    with open("inventaris_barang.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(updated_data)

    print("Data inventaris telah diperbarui:")
    for row in updated_data:
        print(row)

except FileNotFoundError:
    print("File 'inventaris_barang.csv' tidak ditemukan.")
