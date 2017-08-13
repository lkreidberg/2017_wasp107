import mycorner as corner
import matplotlib.pyplot as plt
import numpy as np
import pickle
from pylab import hist


p = pickle.load(open("MCMC_CC_Limit_Metallicity.pic", "rb"))
p = p[:,:-1]

d = p[:,0:4]
ind = (d[:,1]<0.8)&(d[:,3]<-0.2)#&(d[:,0]<1000)&(d[:,2]<-0.25)
d = d[ind]

ctoo = np.log10(0.54)
print ctoo
print 1.0*sum(d[:,2]>ctoo)/(1.*len(d[:,2]))

labels = ["T_irr", "Z", "C/O", "P_cloud"]

plt.figure(figsize = (6,6))
#fig = corner.corner(d, labels = labels, plot_contours = False, no_fill_contours = True, plot_datapoints = False, range = [[500,1000], 0.997, 0.997, 0.997])
fig = corner.corner(d, labels = labels, smooth = 0.7)#, levels = [0.16, 0.5, 0.84]) 

plt.savefig("pairs.png")
