mahasiswa = {
    "alice" : "computer science", 
    "bob" : "mathematics", 
    "charlie" : "physic",
    "david" : "computer science",
    "eva" : "mathematics"
}

jumlah_per_jurusan = {}

for jurusan in mahasiswa.values():
    if jurusan in jumlah_per_jurusan:
        jumlah_per_jurusan[jurusan] += 1
    else:
        jumlah_per_jurusan[jurusan] = 1

for jurusan, jumlah in jumlah_per_jurusan.items():
    print(f"Prodi {jurusan} sebanyak {jumlah}")

# saifulloh fattah bintoro_2408256_RPL1B