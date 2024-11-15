import matplotlib.pyplot as plt
import numpy as np

def fonksiyon(x, y):
     return (((x ** 2 + y ** 2) / 2) * np.exp(- (x ** 2 - y ** 3) / 4))

x = np.arange(-1.0, 1.0, 0.01)
y = np.arange(-1.0, 1.0, 0.01)
a, b = np.meshgrid(x, y)
z = fonksiyon(a, b)
im = plt.imshow(z, cmap=plt.cm.jet)
seviyeler = [-1, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1]
cizim = plt.contour(z, seviyeler, linewidths=1, cmap=plt.cm.Set2)
plt.clabel(cizim, inline=True, fmt='%1.1f', fontsize=10)
plt.colorbar(im, aspect=20, shrink = 0.6, orientation='vertical')
plt.title("$z=((x^2 + y^2) / 2) e^{-(x^2 - y^3) / 4}$")
plt.show()