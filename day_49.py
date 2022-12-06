berat  =int(input("Masukkan BB anda :"))
tinggi =float(input("Masukkan TB anda :"))
BMI = berat / (tinggi * tinggi)

if(BMI < 17.0):
    print("Kurus,Kekurangan berat badan berat")
elif(BMI >17.0 and BMI <=18.4):
    print("Kurus,kekurangan berat badan ringan")
elif(BMI >18.5 and BMI <=25.0):
    print("Normal")
elif(BMI >25.0 and BMI <=27.0):
    print("Gemuk,Kelebihan berat badan tingkat ringan")
elif(BMI >27.0):
    print("Gemuk,Kelebihan berat badan tingkat berat")
