#Girilen bir sayının pozitif çift sayı olup olamdığını kontrol ediniz.

sayi=int(input("Bir sayı giriniz: "))
sonuc=(sayi>0) and (sayi%2==0)
print(f"girilen sayı pozitif mi çift mi?:{sonuc}") 

#Email ve parola bilgileri ile giriş kontrolü yapınız.
email='email@gulkara.com'
password='123456'
girilenEmail=input("Mailinizi girin: ")
girilenPassword=input("Şifrenizi girin: ")
sonuc=(girilenEmail==email)and(girilenPassword==password)
print(f"mail ve şfreniz girildi mi?: {sonuc}")

#Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
sayi1=int(input("sayi1: "))
sayi2=int(input("sayi2: "))
sayi3=int(input("sayi3: "))
result=(sayi1 > sayi2) and (sayi1 > sayi3)
print(f'a en büyük sayıdır:{result}')
result=(sayi2 > sayi1) and (sayi2 > sayi3)
print(f'b en büyük sayıdır:{result}')
result=(sayi3 > sayi1) and (sayi3 > sayi2)
print(f'c en büyük sayıdır:{result}')


