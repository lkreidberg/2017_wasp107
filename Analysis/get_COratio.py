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

plt.subplot(221)
p = pickle.load(open("Global_Cloud_samples.pic", "rb"))
ctoo = p[:,2]
hist(ctoo)
plt.axvline(np.log10(0.54), color = 'y')
plt.title("CC")
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
print "CC sig", get_significance(alpha/2.)

plt.subplot(222)
p = pickle.load(open("Global_Cloud_noCH4_samples.pic", "rb"))
ctoo = p[:,2]
hist(ctoo)
plt.axvline(np.log10(0.54), color = 'y')
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
plt.title("CC no CH4")
print "CC no CH4 sig", get_significance(alpha/2.)

q = [0.16, 0.5, 0.84]
print 10.**quantiles(ctoo, q)

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
print "CC quench", get_significance(alpha/2.)

plt.subplot(224)
p = pickle.load(open("MCMC_CC_Limit_Metallicity.pic", "rb"))
p = p[:,:-1]
ctoo = p[:,2]
hist(ctoo)
alpha = 1.0*sum(ctoo>solarctoo)/len(ctoo)*1.0
plt.axvline(np.log10(0.54), color = 'y')
plt.title("CC Z")
print "CC Z", get_significance(alpha/2.), alpha

print "3 sigma upper limit on metallicity from CC Z case:"
ind = np.argsort(ctoo)
ctoo = ctoo[ind]
upperlim = int(np.ceil(0.95*len(ctoo)))
print 10.**ctoo[upperlim]
q = [0.997]
print "3 sig Z", 10**quantiles(ctoo, q)


#plt.show()
plt.clf()

p = pickle.load(open("MCMC_Free.pic", "rb"))
#p = p[:,:-1]
plt.subplot(131)
plt.title("H2O")
x = p[:,3]-6
hist(x)
q = [0.16, 0.84]
print "68percent conf h2o", 10**quantiles(x, q)

plt.subplot(132)
plt.title("CH4")
x = p[:,4]-6
hist(x)
CH4 = np.log10(4.4e-3)
CH4 = np.log10(0.00132)
alpha = 1.0*sum(x>CH4)/len(x)*1.0
print "CH4 sig", get_significance(alpha/2)
print "alpha", alpha
q = [0.9974]
print quantiles(x, q)
q = [0.16, 0.84]

print "68percent conf ch4", 10**quantiles(x, q)

alpha = 1.0*sum(x>np.log10(1.228e-4))/len(x)*1.0
sig = get_significance(alpha/2)
print "rule out best expectations, (3.7xsolar, 650K, 0.0005 bar cloud top)", sig

#print "test", get_significance(0.003/2)

plt.subplot(133)
plt.title("NH3")
x = p[:,5]-6
hist(x)

#plt.show()

plt.clf()
ctoo = 10**(p[:,4]-6)/10**(p[:,3]-6)
hist(np.log10(ctoo))
plt.axvline(np.log10(0.54), color = 'y')
print sum(ctoo>0.54), len(ctoo)
plt.show()
