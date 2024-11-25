angka = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
cari = 23

def binary(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = binary(angka, cari)

if result != -1:
    print(f"Angka {cari} ditemukan pada indeks {result}.")
else:
    print(f"Angka {cari} tidak ditemukan.")
# saifulloh fattah bintoro