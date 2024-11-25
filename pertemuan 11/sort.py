def tree(arr):
    if not arr:
        return []
    angka = arr[0]
    kiri = tree([x for x in arr[1:] if x < angka])
    kanan = tree([x for x in arr[1:] if x >= angka])
    return kiri + [angka] + kanan

if __name__ == "__main__":
    data = [5, 3, 7, 2, 8, 6, 4, 1, 9]
    print(data)
    urut = tree(data)
    print(urut)
