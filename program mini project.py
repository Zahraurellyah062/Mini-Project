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

belibarang = []
bayar = 0
jumlah = 0

beli = input("Pilih barang :")
jumlah1 = int(input("jumlah pesan :"))
belibarang.append((beli, jumlah1))
bayar += jumlah1 * barang[beli]
jumlah += jumlah1

while True:
    beli_barang_lain = input("Beli barang lain?\nTekan (iya/tidak):")
    if beli_barang_lain == 'iya':
        beli2 =  input("Pilih barang :")
        jumlah2 = int(input("jumlah pesan :"))
        belibarang.append((beli2, jumlah2))
        bayar += jumlah2 * barang[beli2]
        jumlah += jumlah2
    elif beli_barang_lain == 'tidak':
        print("")
        break
else:
    print("eror")


print("=====================Detail Pembayaran=================")

pembeli = input("nama pembeli:")

print("menu yang dipesan :")
for item in belibarang:
    print(f"{item[1]} x {item[0]}")

print("jumlah yang dipesan:",jumlah)
print("Total Biaya :",bayar)
if bayar > 250000:
    diskon =bayar*25/100
    total =bayar - diskon
    print("Anda mendapatkan diskon 25%")
else :
    total = bayar
    print("Anda tidak mendapatkan diskon")
print("Total yang harus dibayar :",total)