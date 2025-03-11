print("**Bir sayının tek mi çift mi olduğunu bulan program.***")
sayi = int(input("Sayınızı giriniz = "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
elif sayi % 2 == 0:
    print("Sayınız Çifttir.")
else:
    print("Sayınız Tektir.")
