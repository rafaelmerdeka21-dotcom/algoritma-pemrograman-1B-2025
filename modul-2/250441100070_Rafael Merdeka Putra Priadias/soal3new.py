#  Program Perhitungan Tarif Parkir Mall
lama_parkir = int(input("Masukkan lama parkir (jam): "))
status_vip = input("Apakah Anda member VIP? (ya/tidak): ")

# Cek status VIP
if status_vip == "ya":
    biaya = 0 
    print("Anda adalah member VIP, parkir gratis.")
elif lama_parkir <=1:
    print("salah")
else:
    # Non VIP
    jumlah_hari = lama_parkir // 24
    sisa_jam = lama_parkir % 24
    total_hari = jumlah_hari * 20000
    # Biaya parkir sehari penuh
    biaya_harian = jumlah_hari * 20000

    # Biaya sisa jam di hari terakhir
    biaya_sisa = 0
    if 0 < sisa_jam <= 2:
        biaya_sisa = 50000
    elif 2 < sisa_jam < 7:
        biaya_sisa = 5000 + (sisa_jam - 2) * 3000
    elif sisa_jam >= 7:
        biaya_sisa = 20000 # JIka sisa 7 jam atau lebih, biaya maksimal harian
    total_biaya = biaya_harian + biaya_sisa
    print(f"Total Biaya Parkir Anda sebesar: Rp{total_biaya}") 