dummy_data = """\
Alice: 85
Bob: 78
Charlie: 92
Diana: 88
Edward: 74
Fiona: 95
George: 81
Hannah: 87
Ian: 70
Julia: 89
Kevin: 77
Laura: 93
Mike: 68
Nina: 85
Oscar: 79
Paul: 90
Quinn: 76
Rachel: 82
Steve: 80
Tina: 88
"""

with open("nilai_siswa.txt", "w") as file:
    file.write(dummy_data)

try:
    with open("nilai_siswa.txt", "r") as file:
        total_nilai = 0
        jumlah_siswa = 0

        for line in file:
            nama, nilai = line.split(":")
            total_nilai += int(nilai.strip())
            jumlah_siswa += 1

    rata_rata = total_nilai / jumlah_siswa
    print(f"Nilai rata-rata ujian adalah: {rata_rata:.2f}")

except FileNotFoundError:
    print("File nilai_siswa.txt tidak ditemukan.")
# saifulloh fattah bintoro_2408256