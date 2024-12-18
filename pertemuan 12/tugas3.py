import time

def linear_search(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

def binary_search(data, target):
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

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38,
        40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74,
        75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]
target = 60

start_time = time.time()
linear_result = linear_search(array, target)
linear_time = time.time() - start_time

start_time = time.time()
binary_result = binary_search(array, target)
binary_time = time.time() - start_time

print("Hasil Linear Search:")
print(f"Indeks: {linear_result}, Waktu Eksekusi: {linear_time:.10f} detik\n")

print("Hasil Binary Search:")
print(f"Indeks: {binary_result}, Waktu Eksekusi: {binary_time:.10f} detik\n")

if linear_time < binary_time:
    print("Linear Search lebih cepat.")
else:
    print("Binary Search lebih cepat.")
# saifulloh fattah bintoro_2408256