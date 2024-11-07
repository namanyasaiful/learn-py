besar = None
total = 0
gagal = 0

while gagal < 3:
    angka = int(input("Masukkan angka: "))

    total += angka
    
    if besar is None:
        besar = angka
    elif angka > besar:
        besar = angka
        gagal = 0 
    else:
        gagal += 1
    if gagal == 3:
        print(f"Angka terbesar yang dimasukkan: {besar}")
        print(f"Jumlah total semua angka yang dimasukkan: {total}")