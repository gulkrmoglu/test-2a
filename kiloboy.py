#Kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.Formül:(kilo/boy uzunluğunun karesi)
#Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#0-18.4=Zayıf
#18.5-24.9=Normal
#25.0-29.9=Fazla Kilolu
#30.0-34.9=Şişman (Obez)

name=input("Adınız nedir?: ")
kg=float(input("Kilonuz: "))
hg=float(input("Boyunuz: "))

index=(kg)/(kg**2)

zayif=(index >=0) and (index <=18.4)
normal=(index >=18.4)and (index <=24.9)
kilolu=(index >=24.9)and (index<=29.9)
obez=(index >=29.9) and (index<=34.9)

print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf:{zayif}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf:{normal}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf:{kilolu}')
print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf:{obez}')


