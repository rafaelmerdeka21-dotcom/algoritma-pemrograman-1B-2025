# Harga tiket normal
tiket_normal = 50000
# Memasukkan inputan usia           
usia = int(input("Masukkan usia anda :"))

# validasi usia rentang (0-100)
if usia < 0 or usia > 100:
    print("Usiamu Tidak logis!!")
else:
    # Melanjutkan Kondisi
    print("Usia logis!!!")
    # Melanjutkan Kondisi
    status_pelajar = input("Pelajar SMA dengan kartu pelajar? (ya/tidak): ")
    hari = input("Masukkan hari: ")
    diskon = 0

    # Apabila kondisi sudah terpenuhi
    if usia <= 12:
        diskon = 0.5
    else:
        status_pelajar = input("Pelajar SMA dengan kartu pelajar? (ya/tidak): ")
        if status_pelajar == "ya":
            diskon = 0.3
        elif hari == "selasa":
            diskon = 0.2
    tiket_normal = 50000

    # Menghitung harga akhir
    potongan = tiket_normal * diskon
    harga_akhir = tiket_normal - potongan

    # Biaya yang harus dibayarkan
    print(f"Mendapatkan diskon sebesar: {int(diskon * 100)}%")
    print(f"Harga yang harus dibayar: Rp {int(harga_akhir)}")

