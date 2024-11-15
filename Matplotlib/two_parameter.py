"""import matplotlib.pyplot as plt
import datetime

plt.axis('auto')
plt.title("Makine Sıcaklık Takip Grafiği ", fontsize=20, fontname='Bahnschrift')
plt.xlabel("Saat", fontsize=14, fontname='Bahnschrift')
plt.ylabel("Sıcaklık", fontsize=14, fontname='Bahnschrift')
y1 = [120, 122, 124.5, 126, 126.4]
y2 = [100, 102, 103.5, 104, 105]
y3 = [200, 56, 32, 120, 60]
#x = [datetime.datetime.now() + datetime.timedelta(minutes=i)for i in range(len(y1))]
x = [datetime.date(2018, 1, 1), datetime.date(2018, 1, 2),
     datetime.date(2018, 2, 5), datetime.date(2018, 4, 5), 
     datetime.date(2018, 5, 5)]

plt.grid()
plt.plot(x, y1, 'sr')
plt.plot(x, y2, 'bo')
plt.plot(x, y3, "cD")
plt.legend(['Makine 1', 'Makine 2', 'Makine 3'], loc=1)
plt.gcf().autofmt_xdate()
plt.show()

"""

import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=0, zdir='z', label='curve in (x, y)')

# Plot scatterplot data (20 2D points per colour) on the x and z axes.
colors = ('r', 'g', 'b', 'k')

# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.sample(20 * len(colors))
y = np.random.sample(20 * len(colors))
c_list = []
for c in colors:
    c_list.extend([c] * 20)
# By using zdir='y', the y value of these points is fixed to the zs value 0
# and the (x, y) points are plotted on the x and z axes.
ax.scatter(x, y, zs=0, zdir='y', c=c_list, label='points in (x, z)')

# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Customize the view angle so it's easier to see that the scatter points lie
# on the plane y=0
ax.view_init(elev=20., azim=-35, roll=0)

plt.show()