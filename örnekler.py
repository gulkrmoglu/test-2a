#Girilen iki sayının ortalamasını bulun
sayi1=int(input("Bir sayı giriniz: "))
sayi2=int(input("Bir sayı giriniz: "))
ortalama=(sayi1+sayi2)/2
print("Ortalama {}".format(ortalama))

#Girilen vize ve final notu ortalmasını hesaplayan birprogram yazın.
vize=float(input("Vize notunu giriniz: "))
final=float(input("Final notunu giriniz: "))
ortalama=((vize*0.3)+(final*0.70))
print("Ortalama {}".format(ortalama))

#Girilen 3 yazılı notunun ortalamasını bulun.
yazili1=float(input("1.yazılı notunu giriniz: "))
yazili2=float(input("2.yazılı notunu giriniz: "))
yazili3=float(input("3.yazılı notunu giriniz: "))
ortalama=(yazili1+yazili2+yazili3)/3
print("Ortalama {}".format(ortalama))

#Girilen bir sayının0-100 arasında olup olmadığını kontrol ediniz.
sayi=int(input("Bir sayı giriniz: "))
sonuc=(sayi>0) and (sayi < 100)
print(f'Sayı 0 ile 100 arasında mı?: {sonuc}')

