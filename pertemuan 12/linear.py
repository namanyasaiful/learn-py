def linear_search(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1 

data_list = [10, 20, 30, 40, 50]
target_value = 30
result = linear_search(data_list, target_value)

if result != -1:
    print(f"angka {target_value} ditemukan pada indeks {result}.")
else:
    print(f"angka {target_value} tidak ditemukan.")
    # saifulloh fattah bintoro_2408256