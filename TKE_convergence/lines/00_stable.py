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

dh = loadmat('s_001.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-10]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('s_002.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][75,:-10]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{uv1000}}$')

#dh = loadmat('s_003.mat')
#X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
#dat = dh['TKE_res'][75,:-10]
#plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{uv5000}}$')

plt.text(1.6,0.02,R'$\mathregular{{S}_{NP}}$',fontsize=24,color='black')
plt.text(2,0.02,R'$\mathregular{{S}_{xy5000}}$',fontsize=24,color=line_cols[0])
plt.text(2.4,0.02,R'$\mathregular{{S}_{z5000}}$',fontsize=24,color=line_cols[1])
#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{TKE (m^2 s^{-2})}$')

plt.xlim([0,4.1])
#plt.xticks([])
plt.ylim([0,0.3])
plt.yticks([0,0.1,0.2,0.30])
plt.text(3.9, 1.3, '(a)')

##_____________________________ z = 423m _______________________________
#
plt.subplot(3,1,2)

plt.gca().yaxis.grid(which='major', linestyle='--',linewidth=2,color=line_cols[-2])

dh = loadmat('s_001.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-10]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('s_002.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][50,:-10]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{uv1000}}$')

#dh = loadmat('s_003.mat')
#X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
#dat = dh['TKE_res'][50,:-10]
#plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{uv5000}}$')


plt.text(43,0.15,R'$\mathregular{{N}_{z1750}}$',fontsize=20)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)


#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{TKE (m^2 s^{-2})}$')

plt.xlim([0,4.1])
#plt.xticks([])
plt.ylim([0,0.3])
plt.yticks([0,0.1,0.2,0.3])
plt.text(3.9, 1.3, '(b)')

#_____________________________ z = 202m _______________________________

plt.subplot(3,1,3)

plt.gca().yaxis.grid(which='major', linestyle='--',linewidth=2,color=line_cols[-2])

dh = loadmat('s_001.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-10]
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{NP}}$')

dh = loadmat('s_002.mat')
X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
dat = dh['TKE_res'][30,:-10]
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{uv1000}}$')

#dh = loadmat('s_003.mat')
#X = np.arange(dh['TKE_res'].shape[1]-10)*dh['dy'][0][0]
#dat = dh['TKE_res'][30,:-10]
#plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{C}_{uv5000}}$')


plt.text(43,0.15,R'$\mathregular{{N}_{z1750}}$',fontsize=20)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)


plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{TKE (m^2 s^{-2})}$')

plt.xlim([0,4.1])
#plt.xticks([])
plt.ylim([0,0.3])
plt.yticks([0,0.1,0.2,0.3])
plt.text(3.9, 1.3, '(c)')


plt.tight_layout()

plt.savefig('00_stable.png', dpi=600)

plt.show()


