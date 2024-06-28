print("Lütfen sahip olduğunuz çay dönüm miktarını giriniz;")
donum = float(input())
verim = float((donum * 750) + (donum * 800) + (donum * 600)) / 3 #Her sürgünde dönüm başına rekolte değişir
sürgün = verim * 3
fiyat = 17 #Özel sektör ve Çaykur fiyat farkı sebebiyle ortalama alınmıştır
toplam = sürgün * fiyat
print("Tahmini yıllık çay veriminiz;")
print(sürgün)
print("Tahmini yıllık kazancınız;")
print(int(toplam))