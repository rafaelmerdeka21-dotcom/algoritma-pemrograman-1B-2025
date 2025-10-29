n = int(input("Masukkan nilai n: "))
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=" ")
    spaces = (i - 1) * 2 * 2
    print(" " * spaces, end="")

    for k in range(i, n + 1):
        print(k, end=" ")
    print()
