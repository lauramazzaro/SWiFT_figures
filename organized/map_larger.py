# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import glob
import matplotlib.ticker as mtick

plt.figure(figsize=(15,6))

crange = [1000,2000]


dh = loadmat('geo_data_larger.mat')

xlat_1 = dh['d01_xlat']
xlat_2 = dh['d02_xlat']
xlat_3 = dh['d03_xlat']
xlong_1 = dh['d01_xlong']
xlong_2 = dh['d02_xlong']
xlong_3 = dh['d03_xlong']
hgt_1  = dh['d01_hgt']
hgt_2 = dh['d02_hgt']
hgt_3 = dh['d03_hgt']

plt.subplot(1,2,1)

plt.contourf(xlong_1,xlat_1,hgt_1,100,cmap = "gist_earth")

i11 = 329
i12 = 329+529/11
i21 = 377
i22 = 377+529/11

plt.plot([xlong_1[i11,i21],xlong_1[i11,i22]],[xlat_1[i11,i21],xlat_1[i11,i22]],'r',linewidth=2)
plt.plot([xlong_1[i12,i21],xlong_1[i12,i22]],[xlat_1[i12,i21],xlat_1[i12,i22]],'r',linewidth=2)
plt.plot([xlong_1[i11,i21],xlong_1[i12,i21]],[xlat_1[i11,i21],xlat_1[i12,i21]],'r',linewidth=2)
plt.plot([xlong_1[i11,i22],xlong_1[i12,i22]],[xlat_1[i11,i22],xlat_1[i12,i22]],'r',linewidth=2)

i11 = 329+331/11
i12 = 329+331/11+529/11/3
i21 = 377+331/11
i22 = 377+331/11+529/11/3

plt.plot([xlong_1[i11,i21],xlong_1[i11,i22]],[xlat_1[i11,i21],xlat_1[i11,i22]],'k',linewidth=2)
plt.plot([xlong_1[i12,i21],xlong_1[i12,i22]],[xlat_1[i12,i21],xlat_1[i12,i22]],'k',linewidth=2)
plt.plot([xlong_1[i11,i21],xlong_1[i12,i21]],[xlat_1[i11,i21],xlat_1[i12,i21]],'k',linewidth=2)
plt.plot([xlong_1[i11,i22],xlong_1[i12,i22]],[xlat_1[i11,i22],xlat_1[i12,i22]],'k',linewidth=2)

plt.text(0.1,0.9,'d01',color='w',transform=plt.gca().transAxes)
plt.text(0.76,0.76,'d02',color='r',transform=plt.gca().transAxes)
plt.text(0.67,0.85,'d03',color='k',transform=plt.gca().transAxes)
plt.text(0.85,0.06,'(a)',color='w',fontsize='24',transform=plt.gca().transAxes)

plt.colorbar(ticks = [500,1000,1500,2000,2500,3000])


fmt = R'{x:,.0f}$^\circ$'
tick = mtick.StrMethodFormatter(fmt)
plt.gca().yaxis.set_major_formatter(tick) 
fmt = R'{x:,.0f}$^\circ$'
tick = mtick.StrMethodFormatter(fmt)
plt.gca().xaxis.set_major_formatter(tick) 

plt.xticks([-105,-103,-101])
plt.xlim(-105.85,-100.45)
plt.ylim(29.9,34.5)

plt.subplot(1,2,2)
plt.contourf(xlong_2,xlat_2,hgt_2,100,cmap = "gist_earth")
plt.colorbar(ticks = [970,1000,1030,1060,1090])
plt.xticks([-102.4,-102.2,-102.0])

fmt = R'{x:,.1f}$^\circ$'
tick = mtick.StrMethodFormatter(fmt)
plt.gca().yaxis.set_major_formatter(tick) 
fmt = R'{x:,.1f}$^\circ$'
tick = mtick.StrMethodFormatter(fmt)
plt.gca().xaxis.set_major_formatter(tick) 

i11 = 331 
i12 = 331 + 529/3
i21 = 331 
i22 = 331 + 529/3

plt.plot([xlong_2[i11,i21],xlong_2[i11,i22]],[xlat_2[i11,i21],xlat_2[i11,i22]],'k',linewidth=2)
plt.plot([xlong_2[i12,i21],xlong_2[i12,i22]],[xlat_2[i12,i21],xlat_2[i12,i22]],'k',linewidth=2)
plt.plot([xlong_2[i11,i21],xlong_2[i12,i21]],[xlat_2[i11,i21],xlat_2[i12,i21]],'k',linewidth=2)
plt.plot([xlong_2[i11,i22],xlong_2[i12,i22]],[xlat_2[i11,i22],xlat_2[i12,i22]],'k',linewidth=2)

i11 = 331+233/3
i12 = 331+233/3+802/3/3
i21 = 331+233/3
i22 = 331+233/3+802/3/3

plt.plot([xlong_2[i11,i21],xlong_2[i11,i22]],[xlat_2[i11,i21],xlat_2[i11,i22]],'b',linewidth=2)
plt.plot([xlong_2[i12,i21],xlong_2[i12,i22]],[xlat_2[i12,i21],xlat_2[i12,i22]],'b',linewidth=2)
plt.plot([xlong_2[i11,i21],xlong_2[i12,i21]],[xlat_2[i11,i21],xlat_2[i12,i21]],'b',linewidth=2)
plt.plot([xlong_2[i11,i22],xlong_2[i12,i22]],[xlat_2[i11,i22],xlat_2[i12,i22]],'b',linewidth=2)

plt.text(0.85,0.06,'(b)',color='w',fontsize='24',transform=plt.gca().transAxes)
plt.text(0.48,0.80,'d03',color='k',transform=plt.gca().transAxes)
plt.text(0.80,0.70,'d04',color='b',transform=plt.gca().transAxes)

plt.tight_layout()

plt.savefig('map_larger.png',dpi=600)

plt.show()
