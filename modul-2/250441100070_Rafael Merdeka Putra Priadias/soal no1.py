print("Masukkan Nilai Anda")
nilai = int(input())
if nilai > 100 or nilai <= 0:
    print("Mohon maaf nilainya tidak ada")
else:
    if nilai >= 85:
        print("Nilai A")
        print("Masukkan presentase kehadiran")
        status = input()
        if status >= str(90) + "%":
            print("Selamat anda lulus terbaik")
        else:
            print("Nilai A")
    else:
        if nilai >= 70:
            print("Nilai B")
        else:
            if nilai >= 60:
                print("Nilai C")
            else:
                if nilai >= 50:
                    print("Nilai D")
                else:
                    print("Nilai E")

