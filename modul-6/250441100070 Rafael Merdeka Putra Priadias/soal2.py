def gabung_dan_urutkan_tuple(t1, t2):
    gabungan = t1 + t2
    daftar_list = []
    seen = set()
    
    for item in gabungan:
        if item not in seen:
            daftar_list.append(item)
            seen.add(item)
        
    n = len(daftar_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if daftar_list[j] < daftar_list[j+1]:
                daftar_list[j], daftar_list[j+1] = daftar_list[j+1], daftar_list[j]
                swapped = True

        if not swapped:
            break
    return tuple(daftar_list)

t1 = (3, 1, 4)
t2 = (1, 5, 9)
hasil = gabung_dan_urutkan_tuple(t1, t2)

print(f"Tuple 1: {t1}")
print(f"Tuple 2: {t2}")
print(f"Hasil Akhir: {hasil}")

t3 = (9, 2, 5, 5, 1, 0, 2)
t4 = (4, 8, 1, 5, 7, 7)

hasil_2 = gabung_dan_urutkan_tuple(t3, t4)
print(f"Tuple 3: {t3}")
print(f"Tuple 4: {t4}")
print(f"Hasil Akhir 2: {hasil_2}")