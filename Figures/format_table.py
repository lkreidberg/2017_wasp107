import numpy as np

d = np.genfromtxt("w107_spectrum_06-22-17.txt")

n = len(d[:,0])
bins = np.linspace(1.12, 1.65, 21)

print np.mean(d[:,1])
for i in range(n):
#	print '{0:0.3f}'.format(d[i,0]), '&', '{0:0.0f}'.format((d[i,1] - np.mean(d[:,1]))*1.e6), '&', '{0:0.0f}'.format(d[i,2]*1e6), '\\\\' 
	#print '{0:0.3f}'.format(d[i,0]), '&', '{0:0.6f}'.format(d[i,1]), '&', '{0:0.1e}'.format(d[i,2]), '\\\\' 
	print '{0:0.3f}'.format(bins[i]), '--', '{0:0.3f}'.format(bins[i+1]), '&', '{0:0.6f}'.format(d[i,1]), '&', '{0:0.1e}'.format(d[i,2]), '\\\\' 
