import numpy as np
import matplotlib.pyplot as plt
import pickle
from pylab import hist
import scipy.stats as st


def get_significance(alpha):
	z = st.norm.ppf(1.-alpha)
	print "should I be dividing alpha by 2?"
	return z

"""alpha = np.linspace(0.001, 0.999, 100)
plt.plot(alpha, st.norm.ppf(alpha))
plt.show()"""

solarctoo = np.log10(0.54)

plt.subplot(221)
p = pickle.load(open("Global_Cloud_samples.pic", "rb"))
ctoo = p[:,2]
hist(ctoo)
plt.axvline(np.log10(0.54), color = 'y')
plt.title("CC")
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
print "CC sig", get_significance(alpha)

plt.subplot(222)
p = pickle.load(open("Global_Cloud_noCH4_samples.pic", "rb"))
ctoo = p[:,2]
hist(ctoo)
plt.axvline(np.log10(0.54), color = 'y')
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
plt.title("CC no CH4")
print "CC no CH4 sig", get_significance(alpha)

plt.subplot(223)
p = pickle.load(open("MCMC_CC_QUENCH.pic", "rb"))
p = p[:,:-1]
ctoo = p[:,2]
#plt.clf()
#plt.plot(ctoo)
#plt.show()
hist(ctoo)
plt.axvline(np.log10(0.54), color = 'y')
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
plt.title("CC quench")
print "CC quench", get_significance(alpha)

plt.subplot(224)
p = pickle.load(open("MCMC_CC_Limit_Metallicity.pic", "rb"))
p = p[:,:-1]
ctoo = p[:,2]
hist(ctoo)
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
plt.axvline(np.log10(0.54), color = 'y')
plt.title("CC Z")
print "CC Z", get_significance(alpha), alpha
plt.show()

p = pickle.load(open("MCMC_Free.pic", "rb"))
p = p[:,:-1]
x = p[:,4]
hist(x)
plt.title("FREE")
plt.show()
