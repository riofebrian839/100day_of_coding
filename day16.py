Nama = input ("Masukkan Nama Anda :")
Tahun = int (input("Tahun Berapa Anda Lahir :"))

if Tahun >= 1965 and Tahun <= 1979:
    print (Nama,"Berdasarkan Tahun Lahir Anda Tergolong Generasi X")
elif Tahun >= 1980 and Tahun <= 1994:
    print (Nama,"Berdasarkan Tahun Lahir Anda Tergolong Generasi Y")
elif Tahun >= 1995:
    print (Nama,"Berdasarkan Tahun Lahir Anda Tergolong Generasi Z")

