 mini project dasar dasar pemrograman
 nama: zahra aurellya herdiansyah
 kelas: si b 2024
 nim: 2409116062

flowchart mini project
![miniproject drawio](https://github.com/user-attachments/assets/44c3f9c1-3fc3-4cfb-9228-cecced8e3eee)


screenshoot output pada terminal:
apabila tidak mendapat diskon
![Screenshot 2024-09-30 143840](https://github.com/user-attachments/assets/048fc8c4-bdb3-4882-9602-30e0b2256205)
apabila mendapat diskon
![Screenshot 2024-09-30 143551](https://github.com/user-attachments/assets/3ba95a7a-0e36-4013-88ae-fd989ce7e596)
penjelasan:
muncul variabel daftar harga, selanjutnya  memilih barang yang ingin dibeli dari daftar barang di atas dan berapa jumlah yang dipesan, lanjut  apakah ingin menambah barang lain atau tidak, apabila menjawab iya maka akan muncul lagi pertanyaan sebelumnya, setelah menjawab tidak akan muncul detail pembayaran, dilanjut dengan mengisi nama pembeli, lalu muncul output menu yang dipesan,  jumlah yang dipesan, total biaya, dan apabila total biaya lebih dari 250000 akan mendapatkan diskon sebesar 25%, dan juga yang terakhir ada total  yang harus dibayar.

penjelasan python:
1. yang pertama yaitu saya memasukkan variabel barang beserta harganya ![Screenshot 2024-10-01 075412](https://github.com/user-attachments/assets/de67779a-60e5-439e-9aaa-a4a7a6dad6b4)
2. menuliskan print daftar harga, dan juga nanti di dimunculkan barang beserta harganya menggunkan for, print apabila pembelian diatas 250000 akan mendapatkan diskon 25% ![Screenshot 2024-10-01 075417](https://github.com/user-attachments/assets/77ef6afd-e580-4e5d-85c1-dd7b761de029)
3. pada beli barang = [] digunakan untuk menyimpan barang yang dibeli
4. bayar = 0 digunakan untuk menyimpan berapa harga yang harus dibayar oleh pembeli
5. jumlah = 0 digunakan untuk menghitung berapa jumlah yang dibeli oleh pembeli ![Screenshot 2024-10-01 075423](https://github.com/user-attachments/assets/782e6207-9fd5-43fa-83bc-1a790ab85077)
6. baris ke 19 - 20 digunakan untuk mengisi nama barang yang dipilih dan jumlah pesan
7. belibarang.append digunakan menyimpan pasangan barang yang dipilih dan jumlah pesanannya
8. baris ke 22 - 23 digunakan menghitung total biaya dengan mengalikan jumlah yang dipesan dengan harga barang yang bersangkutan dan juga dapat mengapdet total jumlah barang yang dipesan ![Screenshot 2024-10-01 075430](https://github.com/user-attachments/assets/4656282e-d341-4519-a07e-21655c024920)
9. disini menggunakan while untuk perulangan/looping apabila ingin beli barang lain, jika iya maka akan muncul  kembali pertanyaan mengenai pilih barang dan jumlah pesan yang ingin dipilih  dan juga menyimpan barang dan jumlah yang dipesan ke dalam list belibarang, jika tidak maka akan mencetak baris kosong ![Screenshot 2024-10-01 092003](https://github.com/user-!
10. selanjutkan akan muncul detail pembayaran, lalu meng input nama pembeli ![Screenshot 2024-10-01 092026](https://github.com/user-attachments/assets/5b23af28-a234-4cdc-b583-a37e9baecf82)
11. akan dimunculkan print menu apa saja dipesan sebelumnya, dan memulai loop melalui setiap item dalam list belibarang,  setiap item dalam belibarang itu tuple yang berisi nama barang dan jumlah yang dipesan, untuk item[1] merujuk pada jumlah barang yang dipesan dan item[0] merujuk pada nama barang ![Screenshot 2024-10-01 092032](https://github.com/user-attachments/assets/c8fb4f53-6712-498e-b13a-d33e1d3df855)
12. menampilkan jumlah yang dipesan dengan mencetak total jumlah barang yang telah dipesan oleh pengguna, juga mencetak total biaya sebelum penerapan diskon, setelah itu apabila dari total biaya melebihi  250000 akan mendapat diskon sebesar 25% dengan cara mengalikan total biaya dikali 25% setelah itu totalnya dengan bayar dikurangi diskon dan menampilkan anda mendapatkan diskon, apabila tidak melebihi 250000 akan langsung muncul total = bayar dan menampilkan anda tidak mendapatkan diskon, terakhir maka muncul berapa total yang harus di  bayar dari  variabel total ![Screenshot 2024-10-01 092046](https://github.com/user-attachments/assets/7ea5c8df-4800-49c3-a266-284ade112479)

 

