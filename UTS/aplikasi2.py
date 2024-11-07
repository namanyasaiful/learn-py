ganjil = 0
genap = 0 
print("Silahkan Masukan bilangan untuk menghitung jumlah bilangan")

while True : 
    angka = int(input("masukan bilangan: "))
    if angka < 0 :
        break
    if angka %2==0 : 
        genap += angka
    else :
        ganjil += angka
print(f"Jumlah bilangan ganjil = {ganjil}")
print(f"Jumlah bilangan genap = {genap}")
# saifulloh fattah bintoro_2408256