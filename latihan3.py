mahasiswa = {
    "Alice" : {"Age": 20 , "major": "computer science"},
    "Bob" : {"Age": 21 , "major": "macthematics"},
    "Charlie" : {"Age": 19 , "major": "physics"}
}

nama = input("Inputkan nama siswa: ").capitalize()
data = mahasiswa.get(nama)
print(f"Umur {nama} adalah {data['Age']} dan Prodinya adalah {data['major'].capitalize()}")

# Saifulloh fattah bintoro_2408256_RPLB1