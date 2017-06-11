import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34   #J/s
c = 3.0e8       #m/s
kb = 1.4e-23     #J/K

def blackbody(l,T): return 2*h*c**2/(l**5*(np.exp(h*c/(l*kb*T))-1))

kep_response = np.genfromtxt("kepler_response.txt", skip_header = 2)
kep_response[:,0] = kep_response[:,0]/1.e9					#gets wavelength in m

wave = kep_response[:,0]

Tstar = 4300
deltaT = 300
Tspot = Tstar - deltaT

delta_wave = wave[1] - wave[0]

A = 0.006 									#fractional spot area	

#integrates flux over kepler bandpass
spot_flux = np.sum(blackbody(wave, Tspot)*delta_wave)
star_flux = np.sum(blackbody(wave, Tstar)*delta_wave)


print "variability at Kepler wavelengths"
print spot_flux*A/star_flux*1e2

wave = np.linspace(0.5, 5, 100)*1.e-6
spot_flux = blackbody(wave, Tspot)
star_flux = blackbody(wave, Tstar)

#conservative case? half of spots are persistent
Fquiet = star_flux*(1. - A) + spot_flux*A
Factive = star_flux*(1.-2*A) + spot_flux*2.*A

#conservative case? half of spots are persistent
Fquiet = star_flux 
Factive = star_flux*(1.-A) + spot_flux*A

delta = 0.021
plt.plot(wave*1e6, (Fquiet-Factive)/Factive*delta*1e6)
plt.xlabel("wavelength (um)")
plt.ylabel("Transit depth correction due to unocculted spots (ppm")
plt.show()


