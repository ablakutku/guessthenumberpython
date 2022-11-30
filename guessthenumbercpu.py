import random

x = 1
y = 100


ktahmin = int(input("1 ila 100 arasında sayı tutun ve CPU onu bilmeye çalışsın : "))


for i in range(7,0,-1):
    cpurandom = random.randint(x,y)
    if cpurandom == ktahmin:
        print("Tuttuğun sayı : " , cpurandom)
        print("Seni yendim hahahaha!")
        break
    elif cpurandom != ktahmin:
        print("Tuttuğun sayı : ",cpurandom)
        print("Kalan hak : ",i)
    kb = input("Tuttuğun sayı daha mı büyük daha mı küçük? (k,b) : ")
    if kb == "k":
        y = cpurandom
        cpurandom > y
        continue
    if kb == "b":
     x = cpurandom
    cpurandom < x
    continue    