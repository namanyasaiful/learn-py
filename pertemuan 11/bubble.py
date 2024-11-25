import time  # Modul untuk menghitung waktu

def bubble_sort(arr):
    start_time = time.time()  # Catat waktu mulai
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()  # Catat waktu selesai
    print(f"Waktu eksekusi Bubble Sort: {end_time - start_time:.6f} detik")

# Contoh penggunaan
array = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38]
bubble_sort(array)
print("Hasil Bubble Sort:", array)
