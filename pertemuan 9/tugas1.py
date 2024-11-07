def fibonacci(n):
    deret = [0, 1]
    
    for i in range(2, n):
        berikutnya = deret[i - 1] + deret[i - 2]
        deret.append(berikutnya)
    return deret[:n]

jumlah_bilangan = int(input("Masukkan jumlah bilangan Fibonacci yang diinginkan (N): "))

if jumlah_bilangan <= 0:
    print("Masukkan angka positif lebih dari 0.")
else:
    hasil = fibonacci(jumlah_bilangan)
    print("Deret Fibonacci:", hasil)
# saifulloh fattah bintoro_2408256