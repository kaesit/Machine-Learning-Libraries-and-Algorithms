import matplotlib.pyplot as plt
import numpy as np

"""
x = np.linspace(-5, 5, 1000)
y = (x**3) + ((4) * (x**2)) + 4*x + 6
plt.text(0, 110, '$y=x^3+4x^2+5x+6$', fontsize=20, bbox={'facecolor': 'green', 'alpha': 0.5})

plt.grid()
plt.plot(x, y)
plt.show()
"""


x = np.linspace(-20, 20, 1000)
y = (x**2) + (-9)
plt.text(-100, 270, '$y=x^2-9$', fontsize=20, bbox={'facecolor': 'green', 'alpha': 0.5})
#y = (x**2) - 1
plt.grid()
plt.plot(x, y)
plt.show()
