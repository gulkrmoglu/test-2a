#İki bağımsız değişken alan bir işlev oluşturun: orijinal price ve discount tam sayı olarak yüzde ve indirimden sonraki son fiyatı döndüren.
def indirimli_fiyat(price,discount):
    indirim_miktari=price*(discount/100)
    son_fiyat=price-indirim_miktari
    return round(son_fiyat,2)
print(indirimli_fiyat(80,20))

#Bu şekilde belirtilen orijinal fiyat ve indirim yüzdesi kullanılarak indirimli fiyat hesaplanır ve iki 
#ondalık basamağa yuvarlanır.