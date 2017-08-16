import numpy as np
import matplotlib.pyplot as plt

r = [0.94, 0.38, 0.56]

z = [24.3, 100., 4.8] 
lo = [24.3, 0., 4.]
hi = [0., 1000., 21.5]


plt.errorbar(r, z, yerr = [lo, hi], fmt = '.k')
plt.plot(0.94, 12.4, '.k')
plt.yscale('log')

plt.ylim(0.1, 1000.)
plt.ylabel("Metallicity (x solar)")
plt.xlabel("Radius (Rj)")
plt.show()
