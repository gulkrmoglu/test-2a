
#Bu meydan okumada bir çiftçi sizden, tüm hayvanları arasında kaç bacağın sayılabileceğini ona söylemenizi istiyor. Çiftçi üç tür yetiştiriyor:
#Tavuklar 2 bacak
#İnekler 4 bacak
#Kediler 4 bacak
#Çiftçi hayvanlarını saydı ve size her tür için bir ara toplam verdi. Tüm hayvanların toplam bacak sayısını döndüren bir fonksiyon uygulamanız gerekir .
def toplam_bacak_sayisi(tavuklar,inekler,kediler):
    tavuk_bacak=tavuklar*2
    inek_bacak=inekler*4
    kedi_bacak=kediler*4 
    toplam_bacak=tavuk_bacak+inek_bacak+kedi_bacak
    return toplam_bacak
print(toplam_bacak_sayisi(5,2,3) )

