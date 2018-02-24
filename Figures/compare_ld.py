import numpy as np
import matplotlib.pyplot as plt
import os, glob

d = np.genfromtxt("tspec_LDfixT4310K.txt")
plt.errorbar(d[:,0], d[:,1], d[:,2])
e = np.genfromtxt("tspec_LDfixT4430K.txt")
plt.errorbar(e[:,0], e[:,1], e[:,2])
f = np.genfromtxt("tspec_LDfixT4550K.txt")
plt.errorbar(f[:,0], f[:,1], f[:,2])

print np.max((d[:,1] - np.mean(d[:,1]))**2 - (f[:,1] -np.mean(f[:,1]))**2)*1e6

plt.show()

path = "LD_coefficients"
files = glob.glob(os.path.join(path, "*141*"))

colors = ['red', 'blue', 'orange', 'yellow', 'green', 'purple']

for i, f in enumerate(files):
    d = np.genfromtxt(f)
    print f
    plt.plot(d[:,0], d[:,3], color = colors[i])
    #plt.plot(d[:,0], d[:,4], color = colors[i])

plt.legend()
plt.show()

    
