a=30
b=20
if a>b:
    print("a b'den büyüktür")
else:
    print("tam tersi")

a=10
b=10
if a>b:
    print("a b'den büyüktür")
elif a>b:
    print("a b'den küçüktür")
else:
    print("a b'ye eşittir")

num=int(input("Bir sayı giriniz: "))
if num >0:
    print("sayı pozitif")
elif num<0:
    print("sayı negatif")
else:
    print("sayı sıfır")

#Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol eden python uygulamasını yapın.
#Ehliyet alma koşulu en az 18 ve eğitim durumu lise veya üniversite olmalıdır.
isim=input("Adınızı giriniz: ")
yas=int(input("Yasınızı giriniz: "))
egitim=input("Eğitiminizi giriniz: ")
if(yas >= 18):
    if(egitim=='lise' or egitim=='üniversite'):
        print(f'{isim} ehliyet alabilirsin')
    else:
        print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz')
print(f'{isim} ehliyet alamazsın yaşın tutmuyor')

#Yazılı ortalaması girilen öğrencinin sınıf geçme durumunu (geçti-kaldı)gösterin.

ort=int(input("Ortalamanızı giriniz: "))
if(ort >=50):
    print("geçti")
else:
    print("kaldı")

#Yaşı girilen kişinin ehliyet alıp almayacağını gösteren programı yazın.
yas=int(input("Yaşınızı girin: "))
if(yas >=18):
    print("ehliyet alabilirsiniz")
else:
    print("yaşınız tutmuyor.Ehliyet alamazsınız")
