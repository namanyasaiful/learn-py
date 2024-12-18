def urut(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def main():
    n = int(input("masukan jumlah elemen:"))
    array = []
    for i in range(n):
        angka = int(input(f"masukan elemen ke-{i+1}: "))
        array.append(angka)
        urut(array)
        print("array yang sudah di sorting:",array)
    urut(array)

if __name__ == "__main__":
    main()
# saifulloh fattah bintoro_2408256