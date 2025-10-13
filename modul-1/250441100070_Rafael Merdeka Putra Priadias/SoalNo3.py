import math
math.comb

bola_merah = 8
bola_biru = 6
bola_diambil = 3
print("Bola merah ada:", bola_merah)
print("Bola biru ada:", bola_biru)
print("Bola diambil secara acak:", bola_diambil)
total_bola = bola_merah + bola_biru
jumlah_kombinasi = math.comb(total_bola, bola_diambil)
print("Total semua bola dalam kota:", total_bola)
print("Banyak kemungkinan kombinasi bola yang dapat diambil yaitu:", jumlah_kombinasi)