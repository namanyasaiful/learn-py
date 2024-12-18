def antri():
    total = int(input("masukan jumlah antrian:"))
    antrian = []

    while len(antrian) < total :
        nomor = int(input("silahkan ambil nomor antrian:"))
        if nomor in antrian:
            print(f"nomor antrian {nomor} sudah ada")
            return
        else:
            antrian.append(nomor)
            antrian.sort()
            print("silahkan tunggu nomor antrian saat ini: ")
            for n in antrian: 
                print(n)
    print("antrian sudah penuh!")

antri()
# saifulloh fattah bintoro_2408256