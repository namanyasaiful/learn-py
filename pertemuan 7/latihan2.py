# Inisialisasi variabel total
jumlah = 0
print("Masukkan angka-angka berturut-turut (masukkan angka negatif untuk berhenti):")
while True:
    angka = int(input())
    if angka < 0:
        break
    jumlah += angka
print("Total =", jumlah)
# saifulloh fattah bintoro_2408256