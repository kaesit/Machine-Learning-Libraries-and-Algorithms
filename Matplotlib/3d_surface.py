from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def function(x, y):
     return (((x ** 2 + y ** 2) / 2) * np.exp(- (x ** 2 - y ** 3) / 4))


x = np.arange(-1.0, 1.0, 0.01)
y = np.arange(-1.0, 1.0, 0.01)

a, b = np.meshgrid(x, y)
z = function(a, b)
objectee = plt.figure(figsize=(14, 9))
ax = plt.axes(projection='3d')
surface = ax.plot_surface(a, b, z, rstride=1, cstride=1, cmap=plt.cm.jet, linewidth=0, antialiased=True)
objectee.colorbar(surface, shrink=0.6)
plt.title("$z=((x^2 + y^2) / 2) e^{-(x^2 - y^3) / 4}$")
plt.show()