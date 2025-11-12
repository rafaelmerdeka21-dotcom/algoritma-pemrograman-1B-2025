def bisa_dibagi(daftar):
    total_sum = sum(daftar)
    if total_sum % 2 != 0:
        return False
        
    target = total_sum // 2

    kemungkinan_sums = {0}
    
    for angka in daftar:
        sums_baru = set()
        for s in kemungkinan_sums:
            jumlah_baru = s + angka
            if jumlah_baru == target:
                return True

            if jumlah_baru < target:
                sums_baru.add(jumlah_baru)

        kemungkinan_sums.update(sums_baru)
    return False

def tambah_angka(daftar):
    try:
        angka = int(input("Masukkan angka untuk ditambah: "))
        daftar.append(angka)
        print(f"Angka {angka} ditambahkan.")
    except ValueError:
        print("Error: Input harus berupa angka.")

def tampilkan_angka(daftar):
    if not daftar:
        print("Daftar masih kosong.")
    else:
        print(f"Daftar saat ini: {daftar}")

def ubah_angka(daftar):
    tampilkan_angka(daftar)
    try:
        indeks = int(input(f"Masukkan indeks (0 s/d {len(daftar)-1}) yang ingin diubah: "))
        if 0 <= indeks < len(daftar):
            nilai_baru = int(input("Masukkan nilai baru: "))
            daftar[indeks] = nilai_baru
            print("Angka berhasil diubah.")
        else:
            print("Error: Indeks tidak valid.")
    except ValueError:
        print("Error: Input harus berupa angka.")

def hapus_angka(daftar):
    try:
        angka = int(input("Masukkan angka yang ingin dihapus: "))
        if angka in daftar:
            daftar.remove(angka) # Hanya menghapus 1 kemunculan pertama
            print(f"Angka {angka} berhasil dihapus.")
        else:
            print("Error: Angka tidak ditemukan.")
    except ValueError:
        print("Error: Input harus berupa angka.")

def main():
    daftar_angka = []
    
    while True:
        print("\n--- MENU PROGRAM PARTISI ---")
        print("1. Tambah Angka (Create)")
        print("2. Tampilkan Angka (Read)")
        print("3. Ubah Angka (Update)")
        print("4. Hapus Angka (Delete)")
        print("5. Cek Partisi")
        print("6. Keluar")
        
        pilihan = input("Pilih menu [1-6]: ")
        
        if pilihan == '1':
            tambah_angka(daftar_angka)
        elif pilihan == '2':
            tampilkan_angka(daftar_angka)
        elif pilihan == '3':
            ubah_angka(daftar_angka)
        elif pilihan == '4':
            hapus_angka(daftar_angka)
        elif pilihan == '5':
            if not daftar_angka:
                print("Daftar kosong, tidak bisa dicek.")
            else:
                hasil = bisa_dibagi(daftar_angka)
                print(f"Hasil Pengecekan: {hasil}")
                if hasil:
                    print("-> Daftar BISA dibagi menjadi dua bagian dengan jumlah sama.")
                else:
                    print("-> Daftar TIDAK BISA dibagi menjadi dua bagian dengan jumlah sama.")
        elif pilihan == '6':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")


main()