def cek_anagram(kata1, kata2):
    kata_pertama = kata1
    kata_kedua = kata2

    if len(kata_pertama) != len(kata_kedua):
        return False

    if kata_pertama == kata_kedua:
        return False
    
    sorted_1 = sorted(kata_pertama)
    sorted_2 = sorted(kata_kedua)
    if sorted_1 == sorted_2:
        return True
    else:
        return False

print("--- Program Pengecekan Anagram ---")
print("Masukkan dua kata untuk diperiksa")


kata_1 = str(input("Masukkan kata pertama: "))
kata_2 = str(input("Masukkan kata kedua: "))

hasil_pengecekkan = cek_anagram(kata_1, kata_2)
if hasil_pengecekkan == True:
    print("\nStatus: '", kata_1, "' dan '", kata_2, "' ANAGRAM")
else:
    print("\nStatus: '", kata_1, "' dan '", kata_2, "' BUKAN anagram")