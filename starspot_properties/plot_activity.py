import matplotlib.pyplot as plt
import numpy as np

n = np.genfromtxt("WASP107_north_20170511-20170605.txt")
s = np.genfromtxt("WASP107_south_20170321-20170605.txt")

plt.axhline(0, color='0.5')

#plt.plot(n[:,0], n[:,1], '.k')
plt.plot(s[:,0], s[:,1], '.k')

plt.axvline(2457876.12557956, color = 'orange')		#Spitzer Channel 1 
plt.axvline(2457870.404354212, color = 'red')		#Spitzer Channel 2
plt.axvline(2457910.4, color = 'cyan')			#HST

plt.ylim(-0.02, 0.02)

plt.show()

