import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = 3*np.sin(4*np.pi - x)
plt.plot(x, y, color='cyan')
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-3, -2, -1, 0, +1, +2, +3],
           [r'$-3$', r'$-2$', r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$'])
plt.text(-2 * np.pi, 2.5, r'$y=3\sin \left(4\pi -x\right)$',
         fontsize=12, bbox={'facecolor':'cyan', 'alpha':0.3})
plt.annotate('(0, 0) noktası', xy=[0, 0], xycoords='data', xytext=[40, 40], bbox=dict(boxstyle='round', color='k', fc='w', alpha=0.7),
             fontsize=14, textcoords='offset points',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=.2"))
plt.show()

