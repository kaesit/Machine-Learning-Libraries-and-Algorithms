import matplotlib.pyplot as plt
import datetime
import numpy as np


plt.axis("auto")
plt.title("Eşik Değer Aşımı ", fontsize=14)
y = np.array([2, 4, 6, 3, 7, 12, 14, 13, 15, 12, 11, 9, 15, 1, 3, 8])
x = np.arange(len(y))
plt.plot(x, y, color='#3A6E5A')
esik = 9
altEsik = y < esik
plt.scatter(x[altEsik], y[altEsik], color='black')
ustEsik = np.logical_not(altEsik)
plt.scatter(x[ustEsik], y[ustEsik], color='red')
plt.axhline(esik, color='blue', linestyle='-')
plt.show()


"""

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

th = np.linspace(0, 2*np.pi, 128)


def demo(sty):
    mpl.style.use(sty)
    fig, ax = plt.subplots(figsize=(3, 3))

    ax.set_title(f'style: {sty!r}', color='C0')

    ax.plot(th, np.cos(th), '#3A6E5A', label='C1')
    ax.plot(th, np.sin(th), '#3A6E5A', label='C2')
    ax.legend()
    plt.show()


demo('default')
demo('seaborn-v0_8')
"""

