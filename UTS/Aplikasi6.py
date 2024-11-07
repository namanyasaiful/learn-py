item = ""

while True : 
    angka = int(input("masukan nilai ke N: "))
    for i in range(2, angka):
        if (angka % i  == 0) :
            print(angka, "bukan bilangan prima")
            break
        else:
            print(angka, "adalah bilangan prima")
# saifulloh fattah bintoro_2408256