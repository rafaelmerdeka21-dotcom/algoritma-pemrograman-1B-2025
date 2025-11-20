inventaris = {
    "A001": ["Buku Tulis", 5000, 50],
    "B002": ["Pensil 2B", 3000, 100]
}

def tampilkan_semua(data_inventaris):
    print("\n--- Daftar Inventaris ---")
    if not data_inventaris:
        print("Inventaris kosong.")
    else:
        for id_brg, info in data_inventaris.items():
            print(f"ID: {id_brg}, Nama: {info[0]}, Harga: Rp{info[1]:,}, Stok: {info[2]}")

def cari_barang(data_inventaris):
    id_cari = input("Masukkan ID barang yang dicari: ")
    
    if id_cari in data_inventaris:
        info = data_inventaris[id_cari]
        print(f"\nBarang Ditemukan:")
        print(f"ID: {id_cari}, Nama: {info[0]}, Harga: Rp{info[1]:,}, Stok: {info[2]}")
    else:
        print(f"\nBarang dengan ID '{id_cari}' tidak ditemukan.")

def tambah_barang(data_inventaris):
    id_baru = input("Masukkan ID barang baru: ")

    if id_baru in data_inventaris:
        print(f"Gagal! ID '{id_baru}' sudah ada di inventaris.")
        return
        
    try:
        nama_baru = str(input("Masukkan nama barang: "))
        harga_baru = int(input("Masukkan harga: "))
        stok_baru = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Input Harga dan Stok harus berupa angka")
        return
    
    data_inventaris[id_baru] = [nama_baru, harga_baru, stok_baru]
    print(f"Barang '{nama_baru}' dengan ID '{id_baru}' berhasil ditambahkan")

def perbarui_stok(data_inventaris):
    id_update = input("Masukkan ID barang yang stoknya ingin diperbarui: ")
    
    if id_update in data_inventaris:
        nama_barang = data_inventaris[id_update][0]
        stok_saat_ini = data_inventaris[id_update][2]
        
        print(f"Stok '{nama_barang}' saat ini: {stok_saat_ini}")
        
        try:
            jumlah_perubahan = int(input("Masukkan perubahan stok (positif untuk menambah, negatif untuk mengurangi): "))
        except ValueError:
            print("Perubahan stok harus berupa angka")
            return

        stok_baru = stok_saat_ini + jumlah_perubahan
        
        if stok_baru < 0:
            print(f"Gagal! Stok tidak bisa menjadi negatif (Stok saat ini: {stok_saat_ini})")
        else:
            data_inventaris[id_update][2] = stok_baru
            print(f"Stok untuk '{nama_barang}' berhasil diperbarui menjadi {stok_baru}.")
    else:
        print(f"\nBarang dengan ID '{id_update}' tidak ditemukan.")

def hapus_barang(data_inventaris):
    id_hapus = input("Masukkan ID barang yang ingin dihapus: ")
    
    if id_hapus in data_inventaris:
        nama_barang_terhapus = data_inventaris[id_hapus][0]
        del data_inventaris[id_hapus]
        print(f"Barang '{nama_barang_terhapus}' (ID: {id_hapus}) berhasil dihapus.")
    else:
        print(f"\nBarang dengan ID '{id_hapus}' tidak ditemukan.")

def main(): 
    while True:
        print("\n--- Menu Inventaris Gudang ---")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang (berdasarkan ID)")
        print("3. Tambah Barang Baru")
        print("4. Perbarui Stok Barang")
        print("5. Hapus Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_semua(inventaris)
        elif pilihan == '2':
            cari_barang(inventaris)
        elif pilihan == '3':
            tambah_barang(inventaris)
        elif pilihan == '4':
            perbarui_stok(inventaris)
        elif pilihan == '5':
            hapus_barang(inventaris)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()