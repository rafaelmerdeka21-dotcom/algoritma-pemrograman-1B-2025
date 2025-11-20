kontak = {
    "Andi": ["08123456789", "andi@email.com"],
    "Budi": ["08765432100", "budi@email.com"]
}

def tampilkan_semua_kontak(daftar_kontak):
    print("\n--- Daftar Kontak ---")
    if not daftar_kontak:
        print("Belum ada kontak.")
    else:
        for nama, info in daftar_kontak.items():
            print(f"Nama: {nama}, Telp: {info[0]}, Email: {info[1]}")

def cari_kontak(daftar_kontak):
    nama_cari = input("Masukkan nama yang dicari: ")
    
    if nama_cari in daftar_kontak:
        info = daftar_kontak[nama_cari]
        print(f"\nKontak Ditemukan:")
        print(f"Nama: {nama_cari}, Telp: {info[0]}, Email: {info[1]}")
    else:
        print(f"\nKontak dengan nama '{nama_cari}' tidak ditemukan.")

def tambah_kontak(daftar_kontak):
    nama = input("Masukkan nama baru: ")
    if nama in daftar_kontak:
        print(f"Kontak dengan nama '{nama}' sudah ada.")
        return
        
    telepon = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")
    
    daftar_kontak[nama] = [telepon, email]
    print(f"Kontak '{nama}' berhasil ditambahkan.")

def perbarui_email_kontak(daftar_kontak):
    nama_update = input("Masukkan nama kontak yang emailnya ingin diperbarui: ")
    
    if nama_update in daftar_kontak:
        email_baru = input("Masukkan email baru: ")
        daftar_kontak[nama_update][1] = email_baru 
        print(f"Email untuk '{nama_update}' berhasil diperbarui.")
    else:
        print(f"\nKontak dengan nama '{nama_update}' tidak ditemukan.")

def hapus_kontak(daftar_kontak):
    nama_hapus = input("Masukkan nama kontak yang ingin dihapus: ")
    
    if nama_hapus in daftar_kontak:
        del daftar_kontak[nama_hapus]
        print(f"Kontak '{nama_hapus}' berhasil dihapus.")
    else:
        print(f"\nKontak dengan nama '{nama_hapus}' tidak ditemukan.")

def main():
    
    while True:
        print("\n--- Menu Contact Book ---")
        print("1. Tampilkan Semua Kontak")
        print("2. Cari Kontak (berdasarkan nama)")
        print("3. Tambah Kontak Baru")
        print("4. Perbarui Email Kontak")
        print("5. Hapus Kontak")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tampilkan_semua_kontak(kontak)
        elif pilihan == '2':
            cari_kontak(kontak)
        elif pilihan == '3':
            tambah_kontak(kontak)
        elif pilihan == '4':
            perbarui_email_kontak(kontak)
        elif pilihan == '5':
            hapus_kontak(kontak)
        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()