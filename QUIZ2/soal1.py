bukuP = []

def tambah_buku():
    judul = input("masukan judul buku:")
    penulis = input("masukan penulis buku:")
    tahun_terbit = input("masukan tahun terbit buku:")
    status = "tersedia"
    kodeB = input("masukan kode buku:")
    bukuP.append({
        "judul": judul,
        "penulis": penulis,
        "tahun_terbit": tahun_terbit,
        "status": status,
        "kodeB": kodeB,
    })
    print("buku sudah ditambahkan!")

def pinjam():
    kodeB = input("masukan kode buku:")
    for buku in bukuP:
        if buku["kodeB"] == kodeB:
            if buku ["status"] == "tersedia" :
                buku["status"] = "dipinjam"
                print(f"buku '{buku["judul"]}' berhasil dipinjam")
            else :
                print("buku sudah dipinjam")
                return

def kembali():
    kodeB = input("masukan kode buku:")
    for buku in bukuP:
        if buku["kodeB"] == kodeB:
            if buku["status"] == "dipinjam":
                buku["status"] == "tersedia"
                print(f"buku '{buku['judul']}' berhasil dikembalikan")
                return
            else:
                print("buku sedang tidak dipinjam")

def lihat_buku_tersedia():
    print("daftar buku tersedia")
    for buku in bukuP:
        if buku["status"] == "tersedia":
            print(f"judul: {buku['judul']}, penulis: {buku['penulis']}, tahun terbit {buku['tahun_terbit']}, kode buku {buku['kodeB']}")
        else:
            print("buku tidak tersedia")

def lihat_buku_tidak():
    print("daftar buku dipinjam")
    for buku in bukuP:
        if buku["status"] == "dipinjam":
            print(f"judul: {buku['judul']}, penulis: {buku['penulis']}, tahun terbit {buku['tahun_terbit']}, kode buku {buku['kodeB']}")
        else:
            print("buku tidak dipinjam")

def main():
    while True:
        print("1. Tambah buku")
        print("2. Pinjam buku")
        print("3. Kembali buku")
        print("4. Lihat buku tersedia")
        print("5. Lihat buku tidak tersedia")
        print("6. Exit")
        pilihan = input("masukan pilihan:")
        if pilihan == "1":
            tambah_buku()
        elif pilihan == "2":
            pinjam()
        elif pilihan == "3":
            kembali()
        elif pilihan == "4":
            lihat_buku_tersedia()
        elif pilihan == "5" :
            lihat_buku_tidak()
        elif pilihan == "6":
            break

if __name__ == "__main__":
    main()
# saifulloh fattah bintoro_2408256