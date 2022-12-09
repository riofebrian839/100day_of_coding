ber = int(input("Total belanja anda : "))
bur =input("Kode Hari : ")

if  bur ==" Senin":
    diskon = 1/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Selasa":
    diskon = 2/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Rabu":
    diskon = 3/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Kamis":
    diskon = 4/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Jumat":
    diskon = 5/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Sabtu":
    diskon = 6/100
    potongan = ber * diskon
    print(potongan)

elif bur =="Minggu":
    diskon = 7/100
    potongan = ber * diskon
    print(potongan)

else:
    print("Tidak dapat")
