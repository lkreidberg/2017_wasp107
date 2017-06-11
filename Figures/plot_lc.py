import numpy as np
import matplotlib.pyplot as plt
from lc_fit import LightCurveData, Model
import os, glob
import pickle
from pylab import *
import seaborn as sns

sns.set_context("talk")
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})
#sns.set_palette(sns.cubehelix_palette(22, start=.5, rot=-1, light=0.4, dark = 0.6))
#sns.set_palette(sns.husl_palette(22, h=1., s=0.4))
sns.set_palette(sns.diverging_palette(220, 20, n=22))

path =  "lsq_fits"
files = glob.glob(os.path.join(path, "*.p"))	


per = 5.7214742

plt.figure()
ax1 = plt.subplot(121)
#ax2 = ax1.twinx()

ax1.text(2.5, 1.002,'$\lambda$ ($\mu$m)', fontsize=10)

for i, f in enumerate(files):
	p = pickle.load(open(f, 'rb'))
	data, model = p[0], p[1]
	offset = -0.01*float(i)
	ind = model.phase > 0.5
	model.phase[ind] -= 1
	ind = model.phase_hr > 0.5
	model.phase_hr[ind] -= 1
	ind = np.argsort(model.phase_hr)
	model.phase_hr, model.lc_hr = model.phase_hr[ind], model.lc_hr[ind]
	ax1.plot(model.phase_hr*per*24., model.lc_hr + offset, color = '0.5')
	ax1.plot(model.phase*per*24., model.data_corr + offset, marker='.', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5)
	#ax1.text(3., 1 + offset, '{0:d}'.format(int(model.rms))+", "+'{0:0.2f}'.format(data.wavelength), fontsize=10)
	ax1.text(2.7, 0.992 + offset+0.002, '{0:0.2f}'.format(data.wavelength), fontsize=10)
			
	#ax2.plot(model.phase*per*24., np.ones_like(model.phase)*data.wavelength, linewidth=0.)

	#ax2.set_ylabel("Wavelength ($\mu$m)")

	ax1.set_xlim(-3.2, 3.2)
	ax1.set_ylim(0.76, 1.01)
	ax1.set_xlabel("Time from central transit (hours)")
	ax1.set_ylabel("Relative flux (offset)")

ax3 = plt.subplot(122)
#ax4 = ax3.twinx()

ax3.text(2.6, 0.08,' rms\n(ppm)', fontsize=10)
#ax3.text(-3.5, 1,'$\lambda$ ($\mu$m)', fontsize=10)
for i, f in enumerate(files):
	#plt.plot(model.phase*per*24., np.ones_like(model.resid), color='0.5') 
	p = pickle.load(open(f, 'rb'))
	data, model = p[0], p[1]
	ind = model.phase > 0.5
	model.phase[ind] -= 1
	
	offset = -0.002*float(i)*1e2
	plt.axhline(offset, color ='0.5')
	ax3.plot(model.phase*per*24., model.resid/data.flux*1e2 + offset, marker='.', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5)
#	ax3.text(-3.5, offset-1, '{0:0.2f}'.format(data.wavelength), fontsize=10)
	ax3.text(2.8, offset - .1, '{0:d}'.format(int(model.rms)), fontsize=10)
	#ax4.plot(model.phase*per*24., np.ones_like(model.phase)*data.wavelength, linewidth=0.)
	ax3.set_xlim(-3.2, 3.4)
	ax3.set_ylim(-4.5, .35)
	ax3.set_xlabel("Time from central transit (hours)")
	ax3.set_ylabel("Residuals ($\\times10^{-2}$, offset)")
#	ax4.set_ylabel("Wavelength ($\mu$m)")

plt.tight_layout()
plt.show()
