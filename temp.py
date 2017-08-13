import numpy as np
import matplotlib.pyplot as plt


#constants (all SI units)
h = 6.626e-34		#Planck constant
k = 1.38e-23		#Boltzmann constant
c = 3.0e8		#speed of light


#return blackbody spectral radiance as a function of wavelength lambda (in m) and temperature T (Kelvin)
def bb(l, T):
	return 2*h*c**2/(l**5*(np.exp(h*c/(l*k*T)-1)))

l = 4.5e-6
depth = 0.021
Tp, Ts = 780, 4430
print bb(l, Tp)/bb(l, Ts)*depth*1e6

