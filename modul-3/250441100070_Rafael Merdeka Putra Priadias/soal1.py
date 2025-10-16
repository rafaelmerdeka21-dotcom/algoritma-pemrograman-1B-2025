n = int(input("Masukkan batas atas (n): "))
if n == 0 or n == 1:
    print("0 atau 1 bukan bilangan prima")
else:
    print("Bilangan prima dari 1 sampai", n, "adalah:")
    for angka in range(2, n + 1):
        prima = True
        for i in range(2, angka):
            if (angka % i) == 0:
                prima = False
                break
        if prima:
            print(angka)