belanja = int(input("Total Belanja Rp. = "))

if belanja > 50000:
    print("Selamat Anda Mendapatkan Diskon 5%")

    diskon = belanja * 5/100
    bayar = belanja - diskon

    print("Total Belanja Anda, Rp. ", belanja)
    print("Potongan Harga, Rp. ", diskon)
    print("Anda Cukup Bayar, Rp. ", bayar)

    print("Terimasih Sudah Belanja Di Tokoh Kami")
