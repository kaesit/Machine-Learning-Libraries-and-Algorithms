import matplotlib.pyplot as plt
import numpy as np

programlama_notlari = [46, 42, 38, 16, 35, 10, 42, 54, 23, 23, 31, 65, 76, 24, 76, 23, 54, 12, 23, 65,
                       46, 32, 83, 43, 14, 15, 24, 45, 32, 32, 13, 66, 66, 54, 36, 23, 64, 82, 73, 25,
                       43, 40, 100, 94, 99, 91, 72, 76, 12, 56, 43, 76, 12, 34, 73, 43, 74, 22, 33, 55,
                       54, 13, 86, 12, 76, 34, 74, 71, 82, 49, 21, 49, 60, 93, 93, 81, 83, 73, 98, 45]

olasilik_notlari = [43, 54, 18, 16, 35, 10, 42, 54, 23, 23, 31, 65, 76, 24, 76, 23, 54, 12, 23, 65,
                       46, 32, 83, 43, 14, 15, 24, 45, 32, 32, 13, 66, 66, 54, 36, 23, 64, 82, 73, 25,
                       43, 20, 1, 45, 22, 91, 54, 43, 12, 56, 43, 76, 12, 34, 73, 43, 74, 22, 33, 55,
                       32, 11, 22, 51, 77, 33, 74, 71, 82, 49, 21, 49, 60, 93, 93, 81, 83, 73, 98, 45]

print("Programlama Ortalama: ", np.mean(programlama_notlari))
print("Programlama Standart Sapma: ", np.std(programlama_notlari))
print("Olasılık Ortalama: ", np.mean(olasilik_notlari))
print("Programlama Standart Sapma: ", np.std(olasilik_notlari))

ortalamar = [50.5125, 46.0625]
standart_sapmalar = [25.8973906745448, 24.48690657780194]

ders_sayisi = np.arange(2)
ders_ortlamasi_standart_sapmasi_bar_chart = plt.bar(ders_sayisi, ortalamar, yerr=standart_sapmalar, color='blue', 
                                                    error_kw={'ecolor': '0.2', 'capsize':10}, 
                                                    alpha=0.2, label='Dersler')
plt.title("Grafik")
plt.xlabel('Dersler')
plt.ylabel("Ders ortalamaları")
plt.xticks(ders_sayisi, ['Programlama', 'Olasılık'])

def etiket(bar_variable):
     for i in bar_variable:
          yukseklik = i.get_height()
          plt.text(i.get_x() + i.get_width() / 2., 1.05 * yukseklik, '%d' % int(yukseklik), ha='left', va='bottom')

etiket(ders_ortlamasi_standart_sapmasi_bar_chart)
plt.show()