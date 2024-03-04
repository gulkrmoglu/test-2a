#Fiyatın %18 lik kdv sini hesaplayan bir program yazın.
def kdv_hesapla(fiyat):
    kdv_orani = 0.18
    kdv_miktari = fiyat * kdv_orani
    return kdv_miktari

fiyat = float(input("Fiyatı girin: "))
kdv = kdv_hesapla(fiyat)

print("KDV tutarı:", kdv)