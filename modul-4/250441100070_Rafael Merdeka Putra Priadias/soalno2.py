gaji_pokok = 100000
bns_shif_mlm = 50000

gaji_mingguan = 0
total_jm_lmbr = 0
bns_mlm = 0
bns_lembur = 0

print("---Program Hitung Gaji Mingguan (7 Hari)---")
for hari in range(1, 8):
    print(f"\n---Hari Ke-{hari}---")
    jm_lmbr = -1
    while jm_lmbr < 0:
        jm_lmbr = int(input("Masukkan jam lebur:"))
        if jm_lmbr < 0:
            print("Jam lembur tdk blh negatif, Coba lagi!!!!")
    
    shif_mlm = input("Apakah masuk shif mlm (y/n)?")
    gaji_today = gaji_pokok
    bns_lmbr_today = 0
 
    if 1 <= jm_lmbr <= 3:
        bns_lmbr_today = jm_lmbr * 25000
    elif jm_lmbr == 4 :
        bns_lmbr_today = 100000
    elif jm_lmbr == 6:
        bns_lmbr_today = 200000
    elif jm_lmbr == 8:
        bns_lmbr_today = 300000
    elif jm_lmbr >= 8:
        bns_lmbr_today = 300000
    elif jm_lmbr > 8:
        print("Lembur melebihi batas!!!, tidak dihitung")
   
    if shif_mlm == "y":
        gaji_today += bns_shif_mlm
        bns_mlm += bns_shif_mlm
    
    gaji_mingguan += gaji_today + bns_lmbr_today
    total_jm_lmbr += jm_lmbr
print("\n---Bayaran Seminggu---")
print(f"Total jam lembur : {total_jm_lmbr} jam")
print(f"Total bonus shif malam : Rp.{bns_mlm}")
print(f"Total gaji mingguan : Rp.{gaji_mingguan}")

