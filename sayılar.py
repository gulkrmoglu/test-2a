#1-220 arası sayıları ekranda listeleyen program yazın.

for i in range(1,101):
    print(i)

#1-360 arası çift sayıları ekranda listeleyen program yazın.
    
for i in range(1,101):
    if i %2==0:
        print(i)

#1-100 arası tek sayıları ekranda listeleyen program yazın.
        
for i in range(1,101):
    if i %2!=0:
        print(i)

#1-100 arası 4'e ve 6'a tam bölünen sayıları ekranda listeleyen program yazın.

for i in range(1,101):
    if i %4==0 or i %6==0:
        print(i)
#1'den ititbaren kullanıcın girdiği sayıya kadar sayıları listeleyen program yazın.
sayi=int(input("Bir sayı giriniz: "))
for i in range(1,sayi+1):
    print(i)


  