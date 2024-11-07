mobil_lama = {
    "Merk": "Honda",
    "Tipe": "HRV",
    "Tahun": 2018,
    "Warna": "Hitam",
    "NoPol": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Transmisi": "Manual",
}

print(mobil_lama)
merkb = input("masukan merk baru: ")
tipeb = input("masukan tipe baru: ")
tahunb = input("masukan tahun baru: ")
warnab = input("masukan warna baru: ")
nopolb = input("masukan no. polisi baru: ")
bensinb = input("masukan bensin baru: ")
transmisib = input("masukan transmisi baru: ")

mobil_lama.update({
    "Merk": merkb,
    "Tipe": tipeb,
    "Tahun": tahunb,
    "Warna": warnab,
    "NoPol": nopolb,
    "Bensin": bensinb,
    "Transmisi": transmisib
})
print(mobil_lama)
#SAIFULLOH FATTAH BINTORO_2408256_RPL1B