buku_tulis = 5000
pensil = 4500
pajak = 0.1
print("Buku yang dibeli sebanyak 3 unit")
print("Pulpen yang dibeli sebanyak 2 unit")
print("Harga buku per unit:", buku_tulis)
print("Harga pulpen per unit:",pensil)
print("Pajak pembelian sebesar:", pajak)
harga_sebelum = (3 * buku_tulis) + (2 * pensil)
terkena_pajak = harga_sebelum * pajak
print("Pajaknyaa sebesar:", int(terkena_pajak))
print("Total Harga yang Harus dibayar:", int(harga_sebelum + terkena_pajak))