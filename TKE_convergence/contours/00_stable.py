# Plots TKE vs. x for a few heights for all nested runs

# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../../new_cmaps.py')

# Modify plotting parameters!
execfile('../../new_params.py')

import matplotlib.pyplot as plt
from scipy.io import loadmat
import numpy as np
import matplotlib

# --------- INPUT ----------

crange = [0,0.5,1]

# ------------- NP ---------------

fig,axs = plt.subplots(4,1,figsize=(8,16))

dh = loadmat('s_001.mat')

dy = dh['dy'][0][0]

X = np.arange(dh['TKE_res'].shape[1])*dy/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[0].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[0].set_ylabel('z (km)')
#axs.flat[0].set_xlabel('x (km)')
axs.flat[0].set_xlim([0,4.3])
axs.flat[0].set_xticks([])
axs.flat[0].set_yticks([0.0,1.0,2.0,3.0])
axs.flat[0].text(-.5,3,'(a)')

# ------------- uv-5000 ---------------

dh = loadmat('s_002.mat')

dy = dh['dy'][0][0]

X = np.arange(dh['TKE_res'].shape[1])*dy/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[1].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[1].set_ylabel('z (km)')
#axs.flat[1].set_xlabel('x (km)')
axs.flat[1].set_xlim([0,4.3])
axs.flat[1].set_xticks([])
axs.flat[1].set_yticks([0.0,1.0,2.0,3.0])
axs.flat[1].text(-.5,3,'(b)')

# ------------- w-5000 ---------------

dh = loadmat('s_003.mat')

dy = dh['dy'][0][0]

X = np.arange(dh['TKE_res'].shape[1])*dy/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[2].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[2].set_ylabel('z (km)')
axs.flat[2].set_xlabel('x (km)')
axs.flat[2].set_xlim([0,4.3])
axs.flat[2].set_yticks([0.0,1.0,2.0,3.0])
axs.flat[2].text(-.5,3,'(c)')

# ------------- uv-3000 ---------------

dh = loadmat('s_004.mat')

dy = dh['dy'][0][0]

X = np.arange(dh['TKE_res'].shape[1])*dy/1000
Z = np.squeeze(np.average(dh['z_axis'][:,:],axis=1))/1000
im = axs.flat[3].contourf(X,Z,dh['TKE_res'],np.linspace(crange[0],crange[-1],75),cmap=cmaps['viridis'],extend='max')

axs.flat[3].set_ylabel('z (km)')
axs.flat[3].set_xlabel('x (km)')
axs.flat[3].set_xlim([0,4.3])
axs.flat[3].set_yticks([0.0,1.0,2.0,3.0])
axs.flat[3].text(-.5,3,'(c)')
plt.tight_layout()

fig.subplots_adjust(bottom=0.2)

cbar_ax = fig.add_axes([0.165,0.1,0.79,0.02])
fig.colorbar(im,cax=cbar_ax,ticks=crange,orientation='horizontal')

plt.savefig('00_stable.png', dpi=600)

plt.show()

