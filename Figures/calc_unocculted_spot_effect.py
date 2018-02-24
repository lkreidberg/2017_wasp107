import numpy as np

h = 6.626e-34   #J/s
c = 3.0e8       #m/s
kb = 1.4e-23     #J/K

def blackbody(l,T): 
    return 2*h*c**2/(l**5*(np.exp(h*c/(l*kb*T))-1))

#variability amplitude is 0.3% in the Kepler bandpass (Dai & Winn 2017)

l = 0.8e-6
depth = 0.021

delta = 0.01
Tstar =4430.
Tspot = 4130.

print "Kepler variability amplitude, high contrast", (delta*blackbody(l, Tspot) + (1 - delta)*blackbody(l, Tstar))/blackbody(l, Tstar)

"""delta = 0.02
Tstar =4430.
Tspot = 4280.

print "Kepler variability amplitude, low contrast", (delta*blackbody(l, Tspot) + (1 - delta)*blackbody(l, Tstar))/blackbody(l, Tstar)"""

l = np.array([1.1, 1.7])*1.e-6
l = np.array([1.1, 1.7])*1.e-6

delta *= 5

bbstar = blackbody(l, Tstar)
bbspot = blackbody(l, Tspot)

print (depth - depth*(1/(1 - delta*((1 - bbspot)/bbstar))))*1.e6




