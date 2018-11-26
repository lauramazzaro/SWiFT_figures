# 'x_conv_neut_amp_w.py'

# Plots TKE vs. x for a few heights for all nested runs without perturbations

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../../new_cmaps.py')

# Modify plotting parameters!
execfile('../../new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib
from matplotlib import gridspec

plt.figure(figsize=(15,15))
 
#_____________________________ z = 854m _______________________________

plt.subplot(3,1,1)

plt.gca().yaxis.grid(which='major', linestyle='--',linewidth=2,color=line_cols[-2])

dh = loadmat('c_008.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-2]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{NP}}$')

dh = loadmat('c_009.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-2]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{w1250}}$')

dh = loadmat('c_012.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-2]
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{w5000}}$')

dh = loadmat('c_011.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-2]
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{w10000}}$')

plt.text(1.2,1.2,R'$\mathregular{{C}_{NP}}$',fontsize=24,color='black')
plt.text(1.6,1.2,R'$\mathregular{{C}_{z1250}}$',fontsize=24,color=line_cols[0])
plt.text(2,1.2,R'$\mathregular{{C}_{z5000}}$',fontsize=24,color=line_cols[1])
plt.text(2.4,1.2,R'$\mathregular{{C}_{z10000}}$',fontsize=24,color=line_cols[2])

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'TKE $\mathregular{(m^2 s^{-2})}$')

plt.xlim([0,4.2])
plt.xticks([])
plt.ylim([1,3])
plt.yticks([1,2,3])
plt.text(4.0, 2.7, '(a)')

#_____________________________ z = 423m _______________________________

plt.subplot(3,1,2)

plt.gca().yaxis.grid(which='major', linestyle='--',linewidth=2,color=line_cols[-2])

dh = loadmat('c_008.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-2]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{NP}}$')

dh = loadmat('c_009.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-2]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{w1250}}$')

dh = loadmat('c_012.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-2]
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{w5000}}$')

dh = loadmat('c_011.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-2]
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{w10000}}$')

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'TKE $\mathregular{(m^2 s^{-2})}$')

plt.xlim([0,4.2])
plt.xticks([])
plt.ylim([1,3])
plt.yticks([1,2,3])
plt.text(4.0,2.7, '(b)')

#_____________________________ z = 202m _______________________________

plt.subplot(3,1,3)

plt.gca().yaxis.grid(which='major', linestyle='--',linewidth=2,color=line_cols[-2])

dh = loadmat('c_008.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-2]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{C}_{NP}}$')

dh = loadmat('c_009.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-2]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{C}_{w1250}}$')

dh = loadmat('c_012.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-2]
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{w5000}}$')

dh = loadmat('c_011.mat')
X = np.arange(dh['TKE_res'].shape[1]-2)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-2]
plt.plot(X/1000,dat,c=line_cols[2],label=R'$\mathregular{{C}_{w10000}}$')

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'TKE $\mathregular{(m^2 s^{-2})}$')
plt.xlim([0,4.2])
#plt.xticks([])
plt.ylim([1,3])
plt.yticks([1,2,3])
plt.text(4.0, 2.7, '(c)')

plt.tight_layout()

plt.savefig('00_convective.png', dpi=600)

plt.show()


