print("** 1'den X'e kadar olan sayıların toplamını bulan program **")
sayi = int(input("X'iniz = "))

# For döngüsü ile toplam
top = 0
for i in range(1, sayi + 1):
    top += i
print("For döngüsü ile toplam:", top)

# While döngüsü ile toplam
toplam = 0
i = 1

while i <= sayi:
    toplam += i
    i += 1

print("While döngüsü ile toplam:", toplam)
