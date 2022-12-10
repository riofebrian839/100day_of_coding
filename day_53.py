kalimat = input("Tulis sebuah kalimat: ")

kata = kalimat.split()

kata.sort()
print("berikut urutkan kata kata : ")
for urut in kata:
    print(urut)
