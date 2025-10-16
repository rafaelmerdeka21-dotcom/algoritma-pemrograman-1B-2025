kalimat = input("Masukkan sebuah kalimat: ")
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_angka = 0
for huruf in kalimat:
    if huruf in "aiueoAIUEO":
        jumlah_vokal = jumlah_vokal + 1
    elif (huruf >= 'a' and huruf <= 'z') or (huruf >= 'A' and huruf <= 'Z'):
        jumlah_konsonan = jumlah_konsonan + 1
    elif ( huruf >= '0' and huruf <= '9') :
        jumlah_angka = jumlah_angka + 1
jumlah_kata = len(kalimat.split())
print("\n--- Hasil Analisis Kalimat ---")
print("Jumlah huruf vokal:", jumlah_vokal)
print("Jumlah huruf konsonan:", jumlah_konsonan)
print("Jumlah angka :", jumlah_angka)
print("Jumlah kata:", jumlah_kata)