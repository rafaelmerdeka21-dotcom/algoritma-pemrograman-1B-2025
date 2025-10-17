while True:
    motor_matic = 50000
    motor_trail = 100000
    motor_sport = 75000
    diskon = 0
    asuransi = 0

    kendaraan_disewa = (input("jenis motor yang disewa:"))
    lama_sewa = int (input("Berapa lama sewanya:"))
    if asuransi > 3 or asuransi < 3:
        asuransi = (asuransi + 3) * motor_matic
    elif diskon == 10:
        subtotal = 150000
    elif diskon == 5:
        kupon = "AconkGG"
    else:
        print("Tidak ada diskon")
    print(f"Jadi harga sewanya sebesar: {asuransi}")
    


   
        


