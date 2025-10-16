PIN_BENAR = "25070"
kesempatan = 3

while kesempatan > 0:
    pin_input = input("Masukkan 5 Digit PIN Anda: ")
    if pin_input == PIN_BENAR:
        print("PIN benar, akses diterima")
        break
    else:
        kesempatan = kesempatan - 1
        print("PIN salah, coba lagi. Sisa kesempatan:", kesempatan)
if kesempatan == 0:
    print("Akses ditolak, kartu diblokir") 