kupon = {
    "ELBIASA": 10,
    "ELLIMUT": 25,
    "RAFAELGTG": 50
}

def tampilkan_kupon(daftar_kupon):
    print("\n--- Kupon Tersedia ---")
    if not daftar_kupon:
        print("Tidak ada kupon.")
    else:
        for kode, persen in daftar_kupon.items():
            print(f"Kode: {kode} ({persen}%)")

def proses_transaksi(daftar_kupon):
    
    try:
        total_belanja = int(input("Masukkan total belanja: Rp "))
    except ValueError:
        print("Input belanja tidak valid.")
        return

    kode_kupon = input("Masukkan kode kupon (kosongi jika tidak): ")
    total_bayar = total_belanja

    print("\n--- Hasil Transaksi ---")
    print(f"Belanja Awal: Rp {total_belanja}")
    
    if kode_kupon in daftar_kupon:
        persen = daftar_kupon[kode_kupon]
        diskon = total_belanja * (persen / 100)
        total_bayar = total_belanja - diskon
        
        print(f"Kupon Valid: {kode_kupon} ({persen}%)")
        print(f"Diskon: -Rp {diskon}")
        
        del daftar_kupon[kode_kupon]
        print(f"(Info: Kupon {kode_kupon} telah digunakan.)")
        
    elif kode_kupon:
        print(f"Kupon '{kode_kupon}' TIDAK VALID.")
        
    else:
        print("Tidak ada kupon digunakan.")
        
    print(f"Total Bayar:    Rp {total_bayar}")

def main():
    
    while True:
        print("\n--- Menu Kupon ---")
        print("1. Tampilkan Kupon")
        print("2. Proses Transaksi")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == '1':
            tampilkan_kupon(kupon)
        elif pilihan == '2':
            proses_transaksi(kupon)
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

main()