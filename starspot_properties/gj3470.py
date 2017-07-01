import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34   #J/s
c = 3.0e8       #m/s
kb = 1.4e-23     #J/K

def blackbody(l,T): return 2*h*c**2/(l**5*(np.exp(h*c/(l*kb*T))-1))


Tstar = 3600
deltaT = 300
Tspot = Tstar - deltaT


A = 0.01 									#fractional spot area	


wave = 700*10.e-9
#integrates flux over kepler bandpass
spot_flux = blackbody(wave, Tspot)
star_flux = blackbody(wave, Tstar)


print "variability amplitude"
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

delta = 0.0057
plt.plot(wave*1e6, (Fquiet-Factive)/Factive*delta*1e6)
plt.xlabel("wavelength (um)")
plt.ylabel("Transit depth correction due to unocculted spots (ppm")
plt.show()


