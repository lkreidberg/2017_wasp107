import numpy as np
import matplotlib.pyplot as plt
from lc_fit import LightCurveData, Model
import os, glob
import pickle
from pylab import *
import seaborn as sns
import matplotlib.gridspec as gridspec

sns.set_context("talk", rc={"lines.linewidth":1.5})
sns.set_style("white")
sns.set_style("ticks", {"xtick.direction":"in", "ytick.direction":"in"})
#sns.set_palette(sns.diverging_palette(220, 20, n=20))
sns.set_palette(sns.diverging_palette(40, 20, n=20, s=90))

path =  "lsq_fits"
files = glob.glob(os.path.join(path, "*.p"))	


per = 5.7214742

plt.figure()
gs = gridspec.GridSpec(2, 2, height_ratios =[1,5], hspace=0.05, wspace=0.25)

ax1 = plt.subplot(gs[0,0])
p = pickle.load(open("white_lc_fit.p", 'rb'))
data, model = p[0], p[1]
ind = model.phase > 0.5
model.phase[ind] -= 1
ind = model.phase_hr > 0.5
model.phase_hr[ind] -= 1
ind = np.argsort(model.phase_hr)
model.phase_hr, model.lc_hr = model.phase_hr[ind], model.lc_hr[ind]
ax1.plot(model.phase_hr*per*24., model.lc_hr , color = '0.5')
ax1.plot(model.phase*per*24., model.data_corr, marker='.', color = 'w', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5)
ax1.set_xlim(-3.2, 3.4)
ax1.set_ylim(0.973, 1.005)
ax1.yaxis.set_major_locator(FixedLocator(np.array([0.98, 0.99, 1.0])))
ax1.set_yticklabels(["0.98", "0.99", "1.0"])

#ax1.text(2.1, 0.985,'$\lambda$ ($\mu$m):\n1.12 - 1.65', fontsize=10)
ax1.text(2., 0.992,'broadband', fontsize=10)
ax2 = plt.subplot(gs[0,1])

ind = model.phase > 0.5
model.phase[ind] -= 1

x = np.linspace(0.1, 1.1)
ax2.fill_between(x, -1000, 1000, color = '0.7', zorder=-10)
plt.axhline(0., color ='0.5')
plt.plot(model.phase*per*24., model.resid/data.flux*1e6, marker='.', color = 'w', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5)
#ax2.text(1.8, 210., 'rms (ppm):\n' + '{0:d}'.format(int(model.rms*1e6)), fontsize=10)
ax2.text(1.7, 300., 'rms: 92 ppm', fontsize=10)
ax2.plot(model.phase*per*24., np.ones_like(model.phase)*data.wavelength, linewidth=0.)
ax2.set_ylim(-500, 700)
ax2.set_xlim(-3.2, 3.4)
ax2.set_xlabel("Time from central transit (hours)")

#ax2 = ax1.twinx()
ax3 = plt.subplot(gs[1,0])

ax3.text(2.5, 1.0028,'$\lambda$ ($\mu$m):', fontsize=10)

#ax1.text(2.1, 0.985,'$\lambda$ ($\mu$m):\n1.12 - 1.65', fontsize=10)
for i, f in enumerate(files):
	p = pickle.load(open(f, 'rb'))
	data, model = p[0], p[1]
	offset = -0.011*float(i)
	ind = model.phase > 0.5
	model.phase[ind] -= 1
	ind = model.phase_hr > 0.5
	model.phase_hr[ind] -= 1
	ind = np.argsort(model.phase_hr)
	model.phase_hr, model.lc_hr = model.phase_hr[ind], model.lc_hr[ind]
	ax3.plot(model.phase_hr*per*24., model.lc_hr + offset, color = '0.5')
	ax3.plot(model.phase*per*24., model.data_corr + offset, marker='.', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5)
	ax3.text(2.75, 0.992 + offset+0.001, '{0:0.2f}'.format(data.wavelength), fontsize=10)
			


	ax3.set_xlim(-3.2, 3.4)
	ax3.set_ylim(0.76, 1.015)
	ax3.set_xlabel("Time from central transit (hours)")
	ax3.set_ylabel("Relative flux (offset)")

ax4 = plt.subplot(gs[1,1])

#ax4 = ax3.twinx()

rms = []
#sns.set_palette(sns.diverging_palette(220, 20, n=20))
#c = sns.diverging_palette(220, 20, n=20)
c = sns.diverging_palette(40, 20, n=20, s=90)
ax4.text(2.8, 800,' rms', fontsize=10)
for i, f in enumerate(files):
	p = pickle.load(open(f, 'rb'))
	data, model = p[0], p[1]
	ind = model.phase > 0.5
	model.phase[ind] -= 1
	
	offset = -0.0022*float(i)*1e6
	plt.axhline(offset, color ='0.5')
	plt.plot(model.phase*per*24., model.resid/data.flux*1e6 + offset, marker='.', ms = 8, linestyle = 'None', markeredgecolor='k', markeredgewidth=0.5, color = c[i])
	ax4.text(2.8, offset - 1400, '{0:d}'.format(int(model.rms)), fontsize=10)
	rms.append(model.rms)
	ax4.plot(model.phase*per*24., np.ones_like(model.phase)*data.wavelength, linewidth=0.)
	ax4.set_xlim(-3.2, 3.4)
	ax4.set_ylim(-45000, 3500)
	ax4.yaxis.set_major_locator(FixedLocator(np.array([-40000, -30000, -20000, -10000, 0])))
	plt.gca().set_yticklabels(["0", "1e4", "2e4", "2e4", "3e4"])
	ax4.set_xlabel("Time from central transit (hours)")
	ax4.set_ylabel("Residuals (ppm, offset)") 


print "mean, median rms:", np.mean(np.array(rms)), np.median(np.array(rms))

plt.savefig("lc.png")
plt.savefig("lc.pdf")
plt.show()
