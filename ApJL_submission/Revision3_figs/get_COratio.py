import numpy as np
import matplotlib.pyplot as plt
import pickle
from pylab import hist
import scipy.stats as st

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

solarctoo = np.log10(0.54)

files = ["CC_FULL_TP_samples.pic", "CC_locked_TP_shape_samples.pic", "CC_locked_TP_shape_Metallicity_Prior_samples.pic"]
ind = [4,2,2]

for i, f in enumerate(files):
    p = pickle.load(open(f, "rb"))
    ctoo = p[:,ind[i]]
    alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
    hist(ctoo)
    print f, "rules out solar C/O at significance:", get_significance(alpha/2.)

plt.show()
