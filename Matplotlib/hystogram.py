import matplotlib.pyplot as plt

x = [56, 52, 48, 16, 45, 20, 52, 52, 36, 60, 70, 52, 36, 56, 20, 80, 56, 36, 44, 36,
     56, 48, 68, 56, 80, 64, 60, 12, 56, 60, 36, 72, 24, 60, 60, 12, 54, 75, 23, 65, 
     12, 65, 12, 65, 62, 67, 12, 87, 43, 98, 46, 65, 24, 43, 34, 23, 65, 23, 64, 65,
     56, 52, 48, 16, 45, 20, 52, 52, 36, 60, 70, 52, 36, 56, 20, 80, 56, 36, 44, 36] # 4 satır her satırda yirmi(20) not var ve bu notların her biri ayrı bir öğrenciye aittir.

X = [14, 43, 44, 12, 90, 100] # tek satır altı(6) not var ve bu notların her biri ayrı bir öğrenciye aittir.

#a = {100: 1, 90:2, 85:3, 50:10, 30:5, 0:20} # bir sözlük yapısı ilk baştaki değer notu karşısında ki anahtarı ise o notu kaç kişinin aldığını gösterir

#keylist = [key for key, val in a.items() for _ in range(val)] # yukarıda ki sözlüğü histrogram grafiğine uygulanabilir şekilde bir arraye dönüştürür

plt.title("NTP Sınavı Not Dağılımı Histogramı")
plt.xlabel("Notlar")
plt.ylabel("Öğrenci Sayısı")
plt.axis([0, 100, 0, 25])
plt.grid(True)
n, bins, patches = plt.hist(x, bins=25,facecolor='red', alpha=0.75)
plt.show()