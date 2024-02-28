#Kullanıcıdan 2 vize (½60) ve final (½40) notunu alıp ortalama hesaplayınız.Eğer ortalama 50 ve üstündeyse geçti 
#değilse kaldı yazdırın.
#a) Ortalama 50  olsa bile final notu en az 50 olmalıdır.
#b)Finalden 70 alındığında ortalamanın önemi olmasın.

vize1=float(input("vize1: ")) 
vize2=float(input("vize2: ")) 
final=float(input("final: ")) 

ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
#a result=(ortalama >=50) and (final >=50)
result=(ortalama >50) or (final>=70)

print(f'öğrencinin ortalaması:{ortalama} ve geçme durumu:{result}')
