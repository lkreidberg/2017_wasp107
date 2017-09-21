import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
from astropy.convolution import convolve
from astropy.convolution import Gaussian1DKernel

sns.set_context("notebook", font_scale = 1.2)
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})

g = Gaussian1DKernel(stddev=10)

plt.figure(figsize=(8,4))
#pickle = hi_res_wlgrid, hi_res_-2sigma, hi_res_-1sigma, hi_res_median, hi_res_+1sigma, hi_res+2sigma, data_wl_grid, raw_data, data_err, median_binned_model

d= np.genfromtxt("w107_spectrum_06-22-17.txt")
plt.errorbar(d[:,0], d[:,1]*100., d[:,2]*100., linestyle = 'none', zorder = 100, marker = 'o', color = 'w', markeredgecolor = 'k', ecolor ='k', markeredgewidth = 1.3)

d0 = np.genfromtxt("/Users/lkreidberg/Desktop/Projects/Data_reduction/HST/WASP107_HST14916/analysis/fit_2017_08_24_13:25.txt")
#offset = 0.025
offset = 0.0
plt.errorbar(d0[:,0], 100*d0[:,1]**2+offset, 100.*2.*d0[:,1]*d0[:,2], fmt ='.k')

#d = np.genfromtxt("wasp107b_10xsolar_0.1mbarcloud.dat")
#plt.plot(d[:,0]*1e6, convolve(d[:,1], g, boundary = 'extend')-0.08)

p = pickle.load(open("WASP107b_Global_Cloud_limit_Metallicity_spectra.pic", "rb"))
#print "outliers", (p[9] - p[7])/p[8]
w = p[0]

plt.fill_between(w, p[1], p[5], color = "navy", alpha = '0.2')
plt.fill_between(w, p[2], p[4], color = "navy", alpha = '0.3')
#plt.plot(w, p[3], color = 'navy', label = "Best fit model")

# best fit
pb = pickle.load(open("Model_best_fit.pic", "rb"))
plt.plot(pb[0], pb[1]*100., color = 'navy', label = 'Best fit model')
print 'outliers', (p[7] - pb[3]*100.)/p[8]


plt.ylabel("Transit depth (%)")
plt.ylim(2.01, 2.1)
plt.xlabel("Wavelength (microns)")

x2 = plt.gca().twinx()
scaleheight = 460./1.e6*100.
plt.plot(w,p[3]/scaleheight - np.min(p[3]/scaleheight), linewidth=0.)

plt.ylabel("Scale heights")
plt.xlim(0.8, 1.7)

plt.tight_layout()
plt.savefig("combined_spectra.png")
plt.show()

