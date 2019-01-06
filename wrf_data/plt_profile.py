# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=[5,10])

dh = np.load('s_z_20000_0400_0500.npz')

z = np.array([1009.2,1020.3,1032.0,1044.5,1057.8,1072.0,1087.1,1103.1,1120.1,1138.2,1157.5,1177.9,1199.7,1223.0,1247.7])-1009.2+5
U = np.mean((dh['u']**2+dh['v']**2)**(1/2.),axis=0)

plt.plot(U,z,color="#8329E8",linewidth=2)

dh = np.load('tower_stable_profile.npz')

plt.plot(dh['U'],dh['z'],'k',linewidth=2)

plt.xlabel(R'U (m s$^\mathrm{-1}$)')
plt.ylabel('z (m)')
plt.ylim([0,200])
plt.xticks([4,8,12,16])

plt.tight_layout()

plt.savefig('s_profs.png',dpi=600)

plt.show()

