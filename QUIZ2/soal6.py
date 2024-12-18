def main():
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    siswa = [(
        input("Masukkan nama siswa: "), 
        float(input("Masukkan nilai akhir siswa: "))
    ) for _ in range(jumlah_siswa)]

    siswa.sort(key=lambda x: x[1], reverse=True)

    while True:
        nama_dicari = input("Masukkan nama siswa (ketik 'keluar' untuk selesai): ").strip()
        if nama_dicari.lower() == "keluar":
            print("Terima kasih.")
            break

        for i, (nama, nilai) in enumerate(siswa):
            if nama == nama_dicari:
                if i < 3:
                    print(f"{nama} berada di rangking {i + 1} dengan nilai {nilai}.")
                else:
                    print(f"{nama} berada di rangking {i + 1}. Belajar lebih giat ya!")
                break
        else:
            print(f"{nama_dicari} tidak ditemukan.")

if __name__ == "__main__":
    main()
# saifulloh fattah bintoro_2408256