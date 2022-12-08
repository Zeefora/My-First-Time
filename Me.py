"""
Semua sintaksis dasar bahasa pemograman dari :
1. Sekuensial : Langkah berurutan
2. Percabangan : Langkah melompat jika terpenuhi
3. Perulangan : Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu, Berkata :"Nak pergilah ke toko"')
print('Budi Menjawab :"Baik,apa yang harus saya lakukan di toko?"')
print('Ibu Menjawab :"Beli 1 botol susu,dan jika ada telur beli 6 butir telur"')
print("Maka Budi pergi ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 15
jumlah_telur = 20
print(f"Jumlah botol susu {jumlah_botol_susu} btl")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya,dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")
