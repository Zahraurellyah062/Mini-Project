barang = {
    "Kursi" :150000,
    "Meja" :200000,
    "Lemari" :250000,
    "Lampu" :50000,
    "Kipas" :80000
}

print("======================Daftar Harga=====================")
for i in barang :
    print("Daftar Harga :",i,"\t Harga : ",barang[i])
print("Pembelian diatas Rp 250.000,- mendapatkan diskon 25%")
print("=======================================================")
beli =input("Pilih barang :")
jumlah1 =int(input("jumlah pesan :"))

beli_barang_lain = input("Beli barang lain?\nTekan (iya/tidak):")
if beli_barang_lain == "iya":
    beli2 =input("Pilih barang :")
    jumlah2 =int(input("jumlah pesan :"))
    bayar2 = jumlah1*barang[beli] + jumlah2*barang[beli2]
    jumlah3 = jumlah1 + jumlah2
elif beli_barang_lain == "tidak":
    print("")
    bayar = jumlah1*barang[beli]
    jumlah4 = jumlah1
else:
    print("error")


print("=====================Detail Pembayaran=================")
print("Beli barang lain?:" , beli_barang_lain)
if beli_barang_lain == "iya":
    print("menu yang dipesan :", beli + " dan " + beli2)
    print("jumlah yang dipesan:",jumlah3)
    print("Total Biaya :",bayar2)
    if bayar2 > 250000:
        diskon =bayar2*25/100
        total =bayar2 - diskon
        print("Anda mendapatkan diskon 25%")
    else :
        total = bayar2
elif beli_barang_lain == "tidak":
    print("menu yang dipesan :",beli)
    print("jumlah yang dipesan:",jumlah4)
    print("Total Biaya :",bayar)
    if bayar > 250000:
        diskon =bayar*25/100
        total =bayar - diskon
        print("Anda mendapatkan diskon 25%")
    else :
        total = bayar
else:
    print("menu yang dipesan :",beli)
    print("jumlah yang dipesan:",jumlah4)
    print("Total Biaya :",bayar)
    if bayar > 250000:
        diskon =bayar*25/100
        total =bayar - diskon
        print("Anda mendapatkan diskon 25%")
    else :
        total = bayar

print("Total yang harus dibayar :",total)