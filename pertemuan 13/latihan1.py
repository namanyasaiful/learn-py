import os

file_name = "file_list.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        content = file.readlines()
        fruits = [line.strip().split() for line in content]
        fruits = [fruit for sublist in fruits for fruit in sublist]
        print("Isi file sebagai list:", fruits)
else:
    print("File tidak ditemukan")
# saifulloh fattah bintoro_2408256