def faktorial_dari(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_dari(n - 1)

print("Semoga membantu membuka brangkas Pak Tungtung")

n = int(input("Masukkan nilai n nya: "))
if n < 0:
    print("Faktorial tidak terdefinisi untuk bilangan negatif")
else:
    hasil = faktorial_dari(n)
    print("Hasil faktorial dari", n, "adalah", hasil)
    print("Gunakan angka ini untuk kombinasi brankas!")
