def cari_mahasiswa(daftar_mahasiswa, nama):
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.lower() == nama.lower():
            return True
    return False

daftar_mahasiswa = [
    "aji", "jira", "sandra", "bowo", "nugi",
    "joko", "ismail", "dudung", "jajang", "tata",
    "kusnadi", "asep", "lilis", "ismi", "isma",
    "mawar", "nini", "nana", "jaki", "juki"
]

mahasiswa_dicari = input("Masukkan nama mahasiswa yang dicari: ")

if cari_mahasiswa(daftar_mahasiswa, mahasiswa_dicari):
    print(f"Mahasiswa '{mahasiswa_dicari}' ditemukan dalam daftar.")
else:
    print(f"Mahasiswa '{mahasiswa_dicari}' tidak ditemukan dalam daftar.")
# saifulloh fattah bintoro_2408256