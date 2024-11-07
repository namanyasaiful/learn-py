buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
ganti = buah.index("ceri")
buah[ganti] = "cherry"

tambah = input("masukan nama buah baru :")
nama = int(input(f"masukan posisi index: {tambah} (0-{len(buah)}): "))
buah.insert(nama, tambah)
print(buah)

buah.sort()

print("list buah yang sudah diurutkan", buah)