# Plots TKE vs. x for a few heights for all nested runs

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_cmaps.py')

# Modify plotting parameters!
execfile('/Users/lauramazzaro/Documents/Work/Perts/Article/Figures/new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib

# --------- INPUT ----------

y_crop = 5000

crange = [0,0.25,0.5,0.75]

# ------------- Theta ---------------

fig,axs = plt.subplots(3,1,figsize=(8,12))

dh = loadmat('n_008_001.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[0].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[0].set_ylabel('z (km)')
#axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_xlim([0,50])
axs.flat[0].set_xticks([])
axs.flat[0].set_yticks([0.2,0.6,1.0,1.4])
axs.flat[0].text(-10,1.4,'(a)')

# ------------- z-force ---------------

dh = loadmat('n_008_005.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[1].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[1].set_ylabel('z (km)')
#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,50])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([0.2,0.6,1.0,1.4])
axs.flat[1].text(-10,1.4,'(b)')

# ------------- xy-Force  ---------------

dh = loadmat('n_008_003.mat')

dx = dh['dx'][0][0]
y_ind = np.ceil(y_crop/dx)

X = np.arange(dh['TKE_res'].shape[1])*dx/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[2].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[2].set_ylabel('z (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,50])
axs.flat[2].set_yticks([0.4,0.8,1.2])
axs.flat[2].text(-10,1.4,'(c)')

plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.79,0.02])
fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('../../figure_8.png', dpi=600)

plt.show()

