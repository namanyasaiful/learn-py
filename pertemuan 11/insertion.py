import time

def insertion_sort(arr):
    start_time = time.time()  # Catat waktu mulai
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()  # Catat waktu selesai
    print(f"Waktu eksekusi Insertion Sort: {end_time - start_time:.6f} detik")

# Contoh penggunaan
array = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38]
insertion_sort(array)
print("Hasil Insertion Sort:", array)
