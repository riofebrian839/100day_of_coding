def main():
    print("Selamat datang di bank kami...")
    saldo = 10000000
    fe = int(input("Masukkan PIN : "))
    if fe == 123456:
            print("1.Cek Saldo""\n2.Tarik Tunai""\n3.Transfer")
            menu =int(input("Pilih Menu : "))
            if menu == 1:
                saldo_anda ="Rp.10.000,000,00"
                print("Saldo Anda Adalah :",saldo_anda)

            elif menu == 2:
                bat =int(input("Jumlah Tunai Yang Akan Ditarik : Rp. "))
                ser = saldo - bat
                print("Sisa Saldo Anda = Rp.",ser)
                print("Tarik Tunai Telah Selesai")
            
            elif menu == 3:
                kepada = int(input("Masukkan Nomor Rekening Yang Akan Dituju : "))
                jumlah = int(input("Jumlah Nominal Yang Akan DiTransfer = "))
                but = saldo - jumlah
                print("Transfer Selesai...!")
                print("Sisa Saldo Anda = Rp.",but)
            
    else:
        print("PIN salah")
        print("Silahkan Diulangi..")


main()
