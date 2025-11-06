def cetak_hasil_gaji(nama, jabatan, gaji_pokok):
    tunjangan = 0
    if jabatan == 'Manager':
        tunjangan = 0.10 * gaji_pokok
    elif jabatan == 'Staff':
        tunjangan = 0.05 * gaji_pokok

    pajak = 0.05 * gaji_pokok
    gaji_bersih = (gaji_pokok + tunjangan) - pajak 
    print("\n--- Rincian Gaji Karyawan ---")
    print("Nama Karyawan  :", nama)
    print("Jabatan        :", jabatan)
    print("Gaji Pokok     : Rp", gaji_pokok)
    print("Tunjangan      : Rp", tunjangan)
    print("Potongan Pajak : Rp", pajak)
    print("-" * 34)
    print("Gaji Bersih    : Rp", gaji_bersih)
    print("-" * 34)

print("--- Program Perhitungan Gaji Karyawan ---")
nama_karyawan = str(input("masukkan nama karyawan: "))
jabatan_karyawan = str(input("Masukkan jabatan (Manager/Staff): "))
gaji_karyawan = int(input("Masukkan gaji pokok: Rp, "))

if jabatan_karyawan != "Manager" and jabatan_karyawan != "Staff":
    print("\nPeringatan: Jabatan '", jabatan_karyawan, "' tidak terdaftar")
    print("Tunjangan akan dihitung sebagai Rp 0")

cetak_hasil_gaji(nama_karyawan, jabatan_karyawan, gaji_karyawan)