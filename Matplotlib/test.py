import matplotlib.pyplot as plt

plt.axis([2009, 2015, 30, 80])
plt.title("Türkiye'nin taşıma sektörüne ait sera gazı emisyon değerleri")
plt.xlabel("Yıllar", fontsize=20, fontname='Bahnschrift', color='red')
plt.ylabel("Emisyon Değeri(bin Gg)", fontsize=20, fontname='Bahnschrift', color='red')
plt.text(2009.7, 47, "En Düşük", color='Green', style='italic', weight='bold', size=7)
plt.text(2013.7, 75, "En Yüksek", color='Purple', style='italic', weight='bold', size=7)
plt.grid()
plt.plot([2010, 2011, 2012, 2013, 2014], [45, 47, 62, 68, 73], 'bo')
plt.show()

