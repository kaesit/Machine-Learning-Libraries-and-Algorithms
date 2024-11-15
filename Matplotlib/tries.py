import matplotlib.pyplot as plt
import numpy as np

#plt.text(0, 5, "Trying a job for learning deeply of 'plot' function")
plt.xlabel("Sevilme Hissi", fontsize=20, fontname='Bahnschrift')
plt.ylabel("Çalışma Motivasyonu", fontsize=20, fontname='Bahnschrift')
#x = [1, 2, 3, 4, 5, 6, 7]
#y = [7, 6, 5, 4, 3, 2, 1]
x = np.linspace(0, 5, 100)
y = (-x**2) + 25
#plt.scatter(x, y)
#plt.scatter(x ,y)
esik = 15
#plt.axis([-1, 6, -1, 28])
plt.title("Çalışma ve Sevginin Eğrisi", fontsize = 26, fontname='Bahnschrift')
plt.axhline(esik, color='blue', linestyle='-')
plt.text(3.162267, 15, "Mutluluk", color='Green', style='italic', weight='bold', size=12)
plt.text(0, 25, "Aşırı Zorlanma Sınırlarını Zorlama Depresyon", color='Red', style='italic', weight='bold', size=12)
plt.text(3, 0, "Amaçsızlık, Kolay Elde Edilebilirlik", color='Blue', style='italic', weight='bold', size=12)
plt.scatter(5, 0, color='black')
plt.scatter(3.162267, 15, color='pink')
plt.scatter(0, 25, color='purple')
plt.plot(x, y)
plt.grid()
mngr = plt.get_current_fig_manager()
mngr.set_window_title("Çalışma ve Sevginin Eğrisi")
mngr.window.setGeometry(320,120, 1200,720)
plt.show()
