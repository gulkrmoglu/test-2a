# Bir tamsayıyı alıp saniyeye çeviren bir program yazınız .

def convert(minutes):
    return minutes * 60
print(convert(7))
print(convert(67))

#Saniyelere dönüşen bir program yazınız.
def seconds(hours):
   return hours *60*60
print(seconds(9))

#Yaşı yıl olarak alan ve yaşı gün olarak döndüren bir fonksiyon oluşturun.

def yas_gunu(yas):
    if yas <= 0:
        return"Geçersiz yas: "
    yas_gunu=yas*365
    return yas_gunu
print(yas_gunu(35))
print(yas_gunu(26))

#Galibiyet,beraberlik ve mağlubiyet sayılarını alan ve bir futbol takımının şu ana kadar elde ettiği puanları hesaplayan bir fonksiyon oluşturun.
#Galibiyetler 3 puan alır
#Beraberlikler 1 puan alır
#Mağlubiyetler 0 puan alır
#Girişler, değerinden büyük veya ona eşit sayılar olacaktır 0.

def puanHesapla(galibiyet,beraberlik,maglubiyet):

        if galibiyet < 0 or beraberlik < 0 or maglubiyet < 0:
            return "Geçersiz giriş. Galibiyet, beraberlik ve mağlubiyet sayıları pozitif tam sayı olmalıdır."
   
        puan = (galibiyet * 3) + (beraberlik * 1) + (maglubiyet * 0)
        return puan

print(puanHesapla(5,3,2))
print(puanHesapla(-2,4,0))
    
