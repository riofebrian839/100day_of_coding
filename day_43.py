#PT DELTA TRANS
tarif_KM = 10000

jarak =int(input("Masukkan Jarak tempuh :"))

print("=========================")

if jarak >10:
    bayar = jarak * tarif_KM
    diskon = 50/100 * bayar
    potongan = bayar - diskon
    print("Jumlah Bayar :",bayar)
    print("Discount     :",diskon)
    print("Total Bayar  :",potongan)

else:
    bayar = jarak * tarif_KM
    diskon = 5/100
    print("Jumlah Bayar :",bayar)
    print("Discount     :")
    print("Total Bayar  :",bayar)

