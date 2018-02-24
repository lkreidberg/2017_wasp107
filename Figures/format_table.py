import numpy as np
import matplotlib.pyplot as plt

d = np.genfromtxt("w107_spectrum_06-22-17.txt")
d2 = np.genfromtxt("w107_spectrum_02-22-18-dw-freeld.txt")
d3 = np.genfromtxt("w107_spectrum-02-22-18-analytic.txt")
l = np.genfromtxt("W107_22bins.dat", skip_header = 17)

ld = np.genfromtxt("w107_freeld_02-22-18.txt")

print "increase in errors for mr", np.median(d3[:,2]/d[:,2])
print "increase in errors for freeld", np.median(d2[:,2]/d[:,2])


n = len(d[:,0])

print np.mean(d[:,1])


#wavelength, transit depth 1, transit depth 2, transit depth 3, PHOENIX u1, PHOENIX u2, fitted LD

print "\\begin{deluxetable*}{LLLLLLL}"
print "\\tablecolumns{7}"
print "\\tablewidth{0pt}"
print "\\tablecaption{WASP-107b Transmission Spectrum and Limb Darkening Coefficients\label{table:tspec}}"
print "\\tablehead{"
print "\colhead{Wavelength} & \colhead{Transit Depth} & \colhead{Transit Depth} & \colhead{Transit Depth} & \colhead{$u_1$} & \colhead{$u_2$} & \colhead{$u$} \\\\"
print "\colhead{(micron)} & \colhead{(method 1)\\tablenotemark{*}} & \colhead{(method 2)} & \colhead{(method 3)} & \colhead{(PHOENIX)} & \colhead{(PHOENIX)} & \colhead{(fitted)}}"
print "\\startdata"

for i in range(n):
	print '{0:0.3f}'.format(l[i,0]), '-', '{0:0.3f}'.format(l[i+1,0]), '&',  '{0:0.6f}'.format(d[i,1]), '\pm', '{0:0.1e}'.format(d[i,2]), '&', '{0:0.6f}'.format(d2[i,1]), '\pm', '{0:0.1e}'.format(d2[i,2]), '&', '{0:0.6f}'.format(d3[i,1]), '\pm', '{0:0.1e}'.format(d3[i,2]), '&', '{0:0.2f}'.format(l[i,3]), '&', '{0:0.2f}'.format(l[i,4]), '&',  ld[i,1], "\pm", ld[i,2] ,'\\\\' 

print "\enddata"
print "\\tablenotetext{*}{Our retrieval analysis uses the transit depths from method 1.}"
print "\\tablecomments{comments}"
print "\end{deluxetable*}"


print "mean 1 - 2", np.mean(d[:,1] - np.mean(d2[:,1]))*1e6
print "mean 1 - 3", np.mean(d[:,1] - np.mean(d3[:,1]))*1e6
print "mean 2 - 3", np.mean(d2[:,1] - np.mean(d3[:,1]))*1e6

d[:,1] -= np.mean(d[:,1])
d2[:,1] -= np.mean(d2[:,1])
d3[:,1] -= np.mean(d3[:,1])

plt.errorbar(d[:,0], d[:,1], d[:,2], fmt = '.k', label = 'method 1')
#plt.errorbar(d2[:,0], d2[:,1], d2[:,2], fmt = '.r', label = 'method 2')
plt.errorbar(d[:,0], d2[:,1], d2[:,2], fmt = '.r', label = 'method 2')
#plt.errorbar(d3[:,0], d3[:,1], d3[:,2], fmt = '.b', label = 'method 3')
plt.errorbar(d[:,0], d3[:,1], d3[:,2], fmt = '.b', label = 'method 3')

print "method 1 - 2"
print np.mean(np.abs(d[:,1] - d2[:,1])/np.sqrt(d[:,2]**2 + d2[:,2]**2))
print np.max(np.abs(d[:,1] - d2[:,1])/np.sqrt(d[:,2]**2 + d2[:,2]**2))
print "method 1 - 3"
print np.mean(np.abs(d[:,1] - d3[:,1])/np.sqrt(d[:,2]**2 + d3[:,2]**2))
print np.max(np.abs(d[:,1] - d3[:,1])/np.sqrt(d[:,2]**2 + d3[:,2]**2))
print "method 2 - 3"
print np.mean(np.abs(d2[:,1] - d3[:,1])/np.sqrt(d2[:,2]**2 + d3[:,2]**2))
print np.max(np.abs(d2[:,1] - d3[:,1])/np.sqrt(d2[:,2]**2 + d3[:,2]**2))


plt.legend()
plt.ylabel("Relative Transit Depth")
plt.xlabel("Wavelength (microns)")
plt.tight_layout()
plt.savefig("spectrum_comparison.pdf")
