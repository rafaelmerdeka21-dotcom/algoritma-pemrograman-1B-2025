daftar_kunjungan = []
id_antrian_terakhir = 0

def tampilkan_menu():
    """Menampilkan menu utama ke pengguna."""
    print("\n" + "="*40)
    print("   Sistem Kunjungan Santri (IDN)")
    print("="*40)
    print("1. Tambah Data Pengunjung (Create)")
    print("2. Tampilkan Daftar Pengunjung (Read)")
    print("3. Hapus Data Pengunjung (Delete)")
    print("4. Keluar")
    print("="*40)

def tambah_kunjungan():
    id_antrian_terakhir = 0
    print("\n--- Tambah Data Pengunjung Baru ---")
    nama_pengunjung = input("Nama Pengunjung: ")
    nama_santri = input("Nama Santri yang Dijenguk: ")
    
    daerah_valid = ["Sumatra", "Kalimantan", "Jawa"]
    while True:
        daerah_asal = input("Daerah Asal (Sumatra/Kalimantan/Jawa): ").capitalize()
        if daerah_asal in daerah_valid:
            break
        else:
            print("Input tidak valid. Harap masukkan 'Sumatra', 'Kalimantan', atau 'Jawa'.")
    
    id_antrian_terakhir += 1
    data_baru = [id_antrian_terakhir, nama_pengunjung, nama_santri, daerah_asal]
    daftar_kunjungan.append(data_baru)
    
    print(f"\nData berhasil ditambahkan!")
    print(f"Pengunjung: {nama_pengunjung} (Asal: {daerah_asal})")
    print(f"ID Antrian: {id_antrian_terakhir}")

def tampilkan_kunjungan():
    print("\n" + "="*40)
    print("       Daftar Kunjungan Saat Ini")
    print("="*40)

    if not daftar_kunjungan:
        print("Belum ada data kunjungan.")
        return

    pengunjung_sumatra = []
    pengunjung_kalimantan = []
    pengunjung_jawa = []

    for kunjungan in daftar_kunjungan:
        daerah = kunjungan[3]
        
        if daerah == "Sumatra":
            pengunjung_sumatra.append(kunjungan)
        elif daerah == "Kalimantan":
            pengunjung_kalimantan.append(kunjungan)
        elif daerah == "Jawa":
            pengunjung_jawa.append(kunjungan)

    print("\n--- Daerah: SUMATRA ---")
    if not pengunjung_sumatra:
        print(" (Tidak ada pengunjung)")
    else:
        for data in pengunjung_sumatra:
            print(f"  ID: {data[0]} | Pengunjung: {data[1]} | Menjenguk: {data[2]}")

    print("\n--- Daerah: KALIMANTAN ---")
    if not pengunjung_kalimantan:
        print(" (Tidak ada pengunjung)")
    else:
        for data in pengunjung_kalimantan:
            print(f"  ID: {data[0]} | Pengunjung: {data[1]} | Menjenguk: {data[2]}")

    print("\n--- Daerah: JAWA ---")
    if not pengunjung_jawa:
        print(" (Tidak ada pengunjung)")
    else:
        for data in pengunjung_jawa:
            print(f"  ID: {data[0]} | Pengunjung: {data[1]} | Menjenguk: {data[2]}")

def hapus_kunjungan():
    """
    Fitur 'Delete': Menghapus data pengunjung berdasarkan ID Antrian.
    """
    print("\n--- Hapus Data Pengunjung ---")
 
    if not daftar_kunjungan:
        print("Daftar kunjungan kosong, tidak ada yang bisa dihapus.")
        return
        
    print("Daftar saat ini (untuk referensi):")
    for data in daftar_kunjungan:
        print(f"  ID: {data[0]}, Pengunjung: {data[1]}, Daerah: {data[3]}")
    
    try:
        id_hapus = int(input("\nMasukkan ID Antrian yang ingin dihapus: "))
    except ValueError:
        print("Input tidak valid. ID harus berupa angka.")
        return

    data_ditemukan = None
    
    for data in daftar_kunjungan:
        if data[0] == id_hapus:
            data_ditemukan = data
            break 

    if data_ditemukan:
        daftar_kunjungan.remove(data_ditemukan)
        print(f"\nData dengan ID {id_hapus} (Pengunjung: {data_ditemukan[1]}) telah dihapus.")
    else:
        print(f"\nData dengan ID Antrian {id_hapus} tidak ditemukan.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tambah_kunjungan()
        elif pilihan == '2':
            tampilkan_kunjungan()
        elif pilihan == '3':
            hapus_kunjungan()
        elif pilihan == '4':
            print("\nTerima kasih. Program ditutup.")
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 4.")

main()