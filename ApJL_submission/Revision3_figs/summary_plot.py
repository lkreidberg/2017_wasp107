import numpy as np
import matplotlib.pyplot as plt
import pickle
from pylab import hist
import scipy.stats as st
import seaborn as sns

sns.set_context("notebook") 
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})

def quantiles(d, q):
        ind = np.argsort(d)
        d = d[ind]
        return_quantile = np.zeros_like(q)
        n = len(d)
        for i in range(0, len(q)):
                return_quantile[i] = d[int(q[i]*float(n))]
        return return_quantile

def get_significance(alpha): 
        z = st.norm.ppf(1.-alpha)
#	print "should I be dividing alpha by 2?"		YESS! check with significance test of alpha = 0.003
	return z

plt.figure(figsize = (8,4))
plt.subplot(121)

solarctoo = np.log10(0.54)

#files = ["CC_FULL_TP_samples.pic", "CC_locked_TP_shape_samples.pic", "CC_locked_TP_shape_Metallicity_Prior_samples.pic"]
#ind = [4,2,2]

files = ["CC_FULL_TP_samples.pic", "CC_locked_TP_shape_Metallicity_Prior_samples.pic"]
ind = [4,2]
labels = ['Parameterized T/P', 'Isothermal profile']
colors = ['red', 'blue']

for i, f in enumerate(files):
    p = pickle.load(open(f, "rb"))
    ctoo = p[:,ind[i]]
    alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
    hist(ctoo,histtype = 'step', label = labels[i], normed = True, color = colors[i], linewidth = 2.)
    print f, "rules out solar C/O at significance:", get_significance(alpha/2.)
    q = quantiles(ctoo, [0.16, 0.5, 0.84])
    print "0.16, 0.5, 0.84 quantiles", q[1], "+", q[2] - q[1], "-", q[1] - q[0]

plt.axvline(solarctoo, color = '0.5')

plt.legend(loc = 'upper right', frameon = True)
plt.xlabel("log10(C/O)")
plt.ylabel("Probability Density")


plt.subplot(122)
files = ["CC_FULL_TP_TP.pic", "CC_locked_TP_shape_TP.pic"]

for i, f in enumerate(files):
    P, T_array = pickle.load(open(f, "rb"))

    qs = [0.16, 0.5, 0.84]
    Tlo, Tmid, Thi = [], [], []
    for j in range(len(P)):
        q = quantiles(T_array[:, j], qs)
        Tlo.append(q[0])
        Tmid.append(q[1])
        Thi.append(q[2])

    plt.plot(np.array(Tmid), P, color = colors[i], label = labels[i])
    plt.fill_betweenx(P, np.array(Tlo), np.array(Thi), color = colors[i], linestyle = 'dashed', alpha = 0.2)
plt.gca().set_yscale('log')

#plt.legend(loc = 'upper left')
plt.ylim(1.e-3, 1e-6)
plt.xlim(300, 1000)
plt.xlabel("Temperature (K)")
plt.ylabel("Pressure (bar)")

plt.tight_layout()
plt.savefig("comparison.pdf")
plt.show()

