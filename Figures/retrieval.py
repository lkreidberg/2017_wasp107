import matplotlib.pyplot as plt
import numpy as np
import pickle
from pylab import hist
import matplotlib as mpl

def quantiles(d, q):
        ind = np.argsort(d)
        d = d[ind]
        return_quantile = np.zeros_like(q)
        n = len(d)
        for i in range(0, len(q)):
                return_quantile[i] = d[int(q[i]*float(n))]
        return return_quantile

mpl.rcParams['font.sans-serif'] = 'Arial'
mpl.rcParams['font.size'] = 18
mpl.rcParams['lines.linewidth'] = 1.4

p = pickle.load(open("MCMC_CC_Limit_Metallicity.pic", "rb"))
p = p[:,:-1]

d = p[:,0:4]
#ind = (d[:,1]<0.8)&(d[:,3]<-0.2)#&(d[:,0]<1000)&(d[:,2]<-0.25)
#d = d[ind]
nbins = 30
q = [0.16, 0.5, 0.84]

plt.subplot(221)
hist(d[:,1], histtype ='stepfilled', color = 'k', facecolor='#b7c9e2', bins = nbins, alpha = 0.8, normed = True)

plt.gca().set_yticklabels([])
plt.xlabel("[Fe/H]")
plt.ylabel("Frequency")
plt.xlim(-2, np.max(d[:,1]))

plt.gca().text(0.08, 0.95, "a", transform=plt.gca().transAxes, fontsize=18, fontweight='bold', va='top')

lo, med, hi = quantiles(d[:,1], q)
print "metal", lo, med, hi
plt.axvline(lo, color = '0.1', linestyle = 'dashed')
plt.axvline(med, color = '0.1', linestyle = 'dashed')
plt.axvline(hi, color = '0.1', linestyle = 'dashed')
plt.axvline(0., color = '#c44240', linestyle = 'solid')
plt.gca().text(0.52, 0.7, "solar", transform=plt.gca().transAxes, fontsize=18, va='top', rotation = 90)

##############################

plt.subplot(222)
hist(d[:,2], histtype ='stepfilled', color = 'k', facecolor='#b7c9e2', bins = nbins, alpha = 0.8, normed = True)

plt.gca().get_yaxis().set_visible(False)		
plt.xlabel("log(C/O)")
plt.gca().text(0.08, 0.95, "b", transform=plt.gca().transAxes, fontsize=18, fontweight='bold', va='top')

lo, med, hi = quantiles(d[:,2], q)
print "C/O", 10**lo, 10**med, 10**hi
plt.axvline(lo, color = '0.1', linestyle = 'dashed')
plt.axvline(med, color = '0.1', linestyle = 'dashed')
plt.axvline(hi, color = '0.1', linestyle = 'dashed')
plt.axvline(np.log10(0.54), color = '#c44240', linestyle = 'solid')
plt.gca().text(0.62, 0.7, "solar", transform=plt.gca().transAxes, fontsize=18, va='top', rotation = 90)

##############################

plt.subplot(223)
hist(d[:,0], histtype ='stepfilled', color = 'k', facecolor='#b7c9e2', bins = nbins, alpha = 0.8, normed  = True)

plt.xlim(200, 1400)
plt.xlabel("$T_\mathrm{irr}$")
plt.ylabel("Frequency")

plt.gca().set_xticklabels([200, 400, 600, 800, 1000, 1200])
plt.gca().set_yticklabels([])

plt.gca().text(0.08, 0.95, "c", transform=plt.gca().transAxes, fontsize=18, fontweight='bold', va='top')

lo, med, hi = quantiles(d[:,0], q)
print "T", lo, med, hi
plt.axvline(lo, color = '0.1', linestyle = 'dashed')
plt.axvline(med, color = '0.1', linestyle = 'dashed')
plt.axvline(hi, color = '0.1', linestyle = 'dashed')

##############################

plt.subplot(224)
hist(d[:,3], histtype ='stepfilled', color = 'k', facecolor='#b7c9e2', bins = nbins, alpha = 0.8, normed = True)

plt.xlabel("log($P_\mathrm{cloud}$)")
plt.xlim(-6, 0)
plt.gca().get_yaxis().set_visible(False)		#LK

plt.gca().text(0.08, 0.95, "c", transform=plt.gca().transAxes, fontsize=18, fontweight='bold', va='top')

lo, med, hi = quantiles(d[:,3], q)
print "P", lo, med, hi
plt.axvline(lo, color = '0.1', linestyle = 'dashed')
plt.axvline(med, color = '0.1', linestyle = 'dashed')
plt.axvline(hi, color = '0.1', linestyle = 'dashed')

plt.tight_layout(w_pad = 0.05)

plt.savefig("retrieval.pdf")
