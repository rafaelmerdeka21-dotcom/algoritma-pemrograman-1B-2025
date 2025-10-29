jumlah_baris = int(input("Masukkan jumlah baris lampu:"))
for y in range(1, jumlah_baris + 1):
    print(f"\n---Baris Ke-{y}---")
    jumlah_lampu = int(input("Masukkan jumlah lampu di setiap baris:"))
    for x in range(1, jumlah_lampu + 1):
        if x % 3 == 0:
            print(f"Lampu ke-{x} pada baris {y} rusak")
        else:
            print(f"Lampu ke-{x} pada baris {y} menyala")
    if y == jumlah_baris:
        print("\nPriksa sambungan daya utama")