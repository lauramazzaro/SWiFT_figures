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

plt.figure(figsize=(10,10))
 
#_____________________________ z = 100m _______________________________

plt.subplot(3,1,1)

dh = loadmat('n_009_001_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_009_005.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{z1000}}$')

dh = loadmat('n_009_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{N}_{z1250}}$')

dh = loadmat('n_009_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(100/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{N}_{z1500}}$')

rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([-0.1,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(a)')

#_____________________________ z = 250m _______________________________

plt.subplot(3,1,2)

dh = loadmat('n_009_001_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')

dh = loadmat('n_009_005.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{z1000}}$')

dh = loadmat('n_009_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{N}_{z1250}}$')

dh = loadmat('n_009_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(250/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{N}_{z1500}}$')


plt.text(43,0.15,R'$\mathregular{{N}_{z1750}}$',fontsize=20)
rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

#plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.xticks([])
plt.ylim([-0.1,2])
plt.yticks([0,1,2])
plt.text(47, 1.7, '(b)')

#_____________________________ z = 350m _______________________________

plt.subplot(3,1,3)

dh = loadmat('n_009_001_001.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,'k',label=R'$\mathregular{{N}_{\theta}}$')
plt.text(21,0.15,R'$\mathregular{{N}_{\theta}}$',color = "black",fontsize=20)


dh = loadmat('n_009_005.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[0],label=R'$\mathregular{{N}_{z1000}}$')
plt.text(25,0.15,R'$\mathregular{{N}_{z1000}}$',color = line_cols[0],fontsize=20)

dh = loadmat('n_009_006.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[1],label=R'$\mathregular{{N}_{z1250}}$')
plt.text(31,0.15,R'$\mathregular{{N}_{z1250}}$',color = line_cols[1],fontsize=20)

dh = loadmat('n_009_007.mat')
X = np.arange(dh['TKE_res'].shape[1])*dh['dx'][0][0]
dat = dh['TKE_res'][int(350/20),:]
dat = dat/np.mean(dat[-dat.shape[0]/5:])
plt.plot(X/1000,dat,c=line_cols[5],label=R'$\mathregular{{N}_{z1500}}$')
plt.text(37,0.15,R'$\mathregular{{N}_{z1500}}$',color = line_cols[5],fontsize=20)


rect = matplotlib.patches.Rectangle((0,0.9),50,0.2,color='#e6e6e6')
plt.gca().add_patch(rect)

#plt.legend(bbox_to_anchor=(1.05,0.5), loc=6, borderaxespad=0.,borderpad=1,fontsize=16)

plt.xlabel('x (km)')
plt.ylabel(R'$\mathregular{q/q_o (-)}$')

plt.xlim([0,50])
plt.ylim([0,2])
plt.yticks([0.1,2])
plt.text(47, 1.7, '(c)')

plt.tight_layout()

plt.savefig('../../figure_6.png', dpi=600)

plt.show()


