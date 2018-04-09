import matplotlib.pyplot as plt
import numpy as np
import pickle
from pylab import hist
import mycorner
import seaborn as sns

sns.set_context("notebook", font_scale = 2)
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})


plt.figure(figsize =( 8,8))

p = pickle.load(open("MCMC_CC_Limit_Metallicity.pic", "rb"))
p = p[:,:-1]

d = p[:,0:4]


d= d[:, 1:3]
d[:,1] = 10**d[:,1]
#mycorner.hist2d(d[:,0], d[:,1], range = [(-1,1.3), (0,1)], levels = [0.68, 0.95, 0.997], smooth = 0.1, fill_contours = True) 
mycorner.hist2d(d[:,0], d[:,1], range = [(-1,1.3), (0,1)], levels = [0.68, 0.95, 0.997], fill_contours = True) 
plt.axhline(0.54, color = 'red', linestyle = 'dashed', linewidth = 2)
plt.xlabel("[M/H]")
plt.ylabel("C/O")
plt.tight_layout()
plt.savefig("ctoo_vs_metallicity.pdf")

plt.show()

