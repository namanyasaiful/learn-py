def jumlah_selisih (jmulai, mmulai, dmulai, jselesai, mselesai, dselesai):
    wmulai = jmulai * 3600 + mmulai * 60 + dmulai
    wselesai = jselesai * 3600 + mselesai * 60 + dselesai
    selisih = wselesai - wmulai

    jam = selisih //3600
    sisa = selisih %3600
    menit = selisih //60 
    detik = selisih %60

    return jam, menit, detik

jmulai = int(input("masukan jam mulai: "))
mmulai = int(input("masukan menit mulai: "))
dmulai = int(input("masukan detik mulai: "))

jselesai = int(input("masukan jam selesai: "))
mselesai = int(input("masukan menit selesai: "))
dselesai = int(input("masukan detik selesai: "))

jam, menit, detik = jumlah_selisih(jmulai, mmulai, dmulai, jselesai, mselesai, dselesai)

print(f"Selisih waktu: {jam} jam {menit} menit {detik} detik")
# saifulloh fattah bintoro_2408256