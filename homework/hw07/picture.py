import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0,60.0,120)

y1 = -4*x + 80
y2 = -(2/3)*x + 30
y3 = np.minimum(y1, y2)


plt.fill_between(x,0,y3,facecolor='grey', alpha=0.5)

plt.plot(x, y1, label=r'$y = -4*x + 80$')
plt.plot(x, y2, label=r'$y = -(2/3)*x + 30$')

plt.xlim((0.0, 60.000))
plt.ylim((0.0, 100.000))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
