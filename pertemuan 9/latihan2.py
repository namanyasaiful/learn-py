
def jumlah(*angka):
    total = sum(angka)
    rata = total / len(angka)
    return total, rata

ketik = input("Masukkan angka (pisahkan dengan spasi): ")
baris = [int(x) for x in ketik.split()]
total, rata = jumlah(*baris)

print(f"Total: {' + '.join(map(str, baris))} = {total}")
print(f"Rata-rata: {total} / {len(baris)} = {rata}")
# saifulloh fattah bintoro_2408256