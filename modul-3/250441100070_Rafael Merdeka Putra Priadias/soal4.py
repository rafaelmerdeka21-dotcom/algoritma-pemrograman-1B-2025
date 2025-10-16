while True:
    nama = input("Masukkan Nama Pembeli: ")
    jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
    if jumlah_barang == 0:
        print("Jumlah barang tidak sesuai")
        pass
    total = 0
    daftar_barang = "" 
    
    for i in range(jumlah_barang):
        nama_barang = input(f"Nama barang ke {i+1}: ")
        harga = int(input(f"Harga {nama_barang}: "))
        total += harga
        daftar_barang += f"{nama_barang} : Rp {harga}\n" 
         
    print("="*50)
    print("Nama pembeli :", nama)
    print("="*50)
    print("Daftar barang dan harga yang dibeli :")
    print(daftar_barang, end="") 
    print("="*50)
    print("Total harga: Rp", total)
    print("Terima kasih telah berbelanja di IndoMei.")

    lanjut = input("Apakah ada pembeli berikutnya? (y/n): ")
    if lanjut == "y":
        print("lanjut")
    else:
        print("selesai")
        break