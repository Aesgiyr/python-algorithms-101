satir = int(input("Satır sayısı giriniz: "))

# Üst kısım
for i in range(1, satir+1):
    for j in range(0, satir-i):
        print("*", end="")
    print("")

# Alt kısım
for i in range(1, satir+1):
    for j in range(satir-1, satir-i, -1):
        print("*", end="")
    print("")