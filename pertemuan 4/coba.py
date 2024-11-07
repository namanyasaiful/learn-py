mobil = {
    "jenis" : "toyota",
    "model" : "kijang inova",
    "tahun" : "2019",
    "roda 4" : True,
    "nama sebutan" : ["kijang", "inova"]
}

# mobil.update({"tahun" : "2020", "jenis" : "musang"})\
mobil.pop("jenis")
print(mobil)