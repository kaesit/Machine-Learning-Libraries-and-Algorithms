import seaborn as sb
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

veriseti = pd.read_excel('C:/Users/PC/Desktop/Programlama/ClassifficationProject/Pandas/EnergyStarScore.xlsx')
sb.heatmap(veriseti.corr(numeric_only = True), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.01)
