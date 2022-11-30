import random
randomsayi = random.randint(1,101)
for x in range(5,-1,-1):
    tahmin = int(input("1,100 arasında bir sayı giriniz : "))
    if tahmin > 100:
        print("Seçeceğin sayı maksimum 100 olmalı.")
        break
    if tahmin < 1:
        print("Seçeceğin pozitif bir tam sayı ve 100'e kadar olmalı.")
        break
    if tahmin == randomsayi:
        print("Tebrikler, doğru tahmin!")
        break 
    if tahmin > randomsayi:
        print("Daha küçük bir sayı giriniz!")
        print("Kalan hakkınız : " , x)
    if tahmin < randomsayi:
        print("Daha büyük bir sayı giriniz!")
        print("Kalan hakkınız : " , x)

else:
    print("Bulamadın beceriksiz seni :D")