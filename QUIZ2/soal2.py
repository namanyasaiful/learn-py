def cari():
    n = int(input("Masukkan jumlah elemen array: "))
    array = []
    for i in range(n):
        angka = int(input(f"Masukkan elemen ke-{i + 1}: "))
        array.append(angka)
    angka_cari = int(input("Masukkan angka yang akan dicari: "))
    if angka_cari in array:
        index = array.index(angka_cari)
        print(f"Angka {angka_cari} ditemukan di indeks {index}.")
    else:
        print("Maaf nilai yang dicari tidak ada di array.")

cari()
# saifulloh fattah bintoro_2408256