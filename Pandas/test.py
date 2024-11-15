import pandas as pd
import numpy as np
#*import seaborn as sb

"""
seri1 = pd.Series(["Code", "Love", 18], index=['C', 'L', 0])
print(seri1)

seri2 = pd.Series([10, 15, 20, 25, 30, 25])
print(seri2[1:4], "\n")

notlar = {"Matematik":70, "Bilgisayar":90, "Elektronik":96, "İstatistik":56}
seri3 = pd.Series(notlar)
print(seri3 * 1.05)
print(np.sqrt(seri3))
print(seri3[seri3 >= 90])
print(seri2.unique())



"""

"""
ogrenciler_dict = {
     "okulNo":pd.Series([101, 110, 606],index=["Asel", "Betül", "Niyazi"]),
     "ortalama":pd.Series([90, 95, 97], index=["Asel", "Betül", "Niyazi"]),
     "bolum":pd.Series(["Makine Müh.", "Bilgisayar Müh.", "Mekatronik Müh."], index=["Asel", "Betül", "Niyazi"]),
     "dogumTarihi":pd.Series([2000, 2000, 1998], index=["Asel", "Betül", "Niyazi"])
}

tablo = pd.DataFrame(ogrenciler_dict)
print(tablo, "\n", "\n")
print(tablo[tablo["ortalama"] < 93])

""" 

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

veriseti = pd.read_excel('C:/Users/PC/Desktop/Programlama/ClassifficationProject/Pandas/EnergyStarScore.xlsx')
print(veriseti.sample(3), "\n")

print(veriseti.sample(frac=0.01), "\n")

print(veriseti.head(6), "\n")

print(veriseti[['Bina Adı', 'ESS', 'BA']].head(6), "\n")

print(veriseti[veriseti.ESS >= 95].head(6), "\n")

print(veriseti[(veriseti.ESS >= 60) & (veriseti.ESS <=70)].head(6), "\n")

print(veriseti[200:301])

print(veriseti.corr(numeric_only = True))

#glue = sb.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
#sb.heatmap(glue)

#print(sb.heatmap(veriseti.corr(numeric_only = True), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.01))

#veriseti = pd.read_csv('C:/Users/PC/Desktop/Programlama/ClassifficationProject/Pandas/DogrusalRegresyon.csv')

#veri = pd.read_excel("C:/Users/PC/Desktop/Programlama/ClassifficationProject/Pandas/EnergyStarScore.xlsx")