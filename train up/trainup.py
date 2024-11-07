kiri = ["p1", "i1", "p2", "i2", "p3", "i3"]
kanan = []
perahu = []

langkah = [
    (["p1", "i1"], ["p1"]),
    (["p2", "i2"], ["i1"]),    
    (["p3", "i3"], ["p2"]),    
    (["p1", "i1"], ["i2"]),    
    (["p2", "i2"], None)
]

print("Awal. Sisi kiri:", kiri, "Perahu:", perahu, "Sisi kanan:", kanan)

for i, (naik, kembali) in enumerate(langkah, 1):
    perahu = naik
    
    for orang in naik:
        kiri.remove(orang)
    kanan.extend(naik)
    print(f"Sisi kiri: {kiri} Perahu: {perahu} Sisi kanan: {kanan}")
    
    if kembali:
        for orang in kembali:
            kiri.append(orang)
        print(f"Sisi kiri: {kiri} Perahu: {perahu} Sisi kanan: {kanan}")

print("Semua pasangan sudah berada di seberang.")
# saifulloh fattah bintoro_2408256 