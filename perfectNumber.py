num = int(input("Bir sayı gir mükemmel mi kontrol edeyim: "))
sum = 0 # 8589869056=12 Dakika aldı  
for i in range(num):
    if(i==0):
        continue
    elif((num%i)==0):
        print("Bölenler: "+ str(i))
        sum+=i
print("Toplam: "+ str(sum))
if sum == num:
    print("Sayınız Mük")
else:
    print("Sayınız Mük Değil")