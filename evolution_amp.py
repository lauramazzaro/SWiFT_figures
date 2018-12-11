# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('new_cmaps.py')

# Modify plotting parameters!
execfile('new_params.py')

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import datetime

plt.figure(figsize=(12,6))

times = [[20,00],[21,20],[21,25],[21,30],[21,35],[21,40],[21,45],[21,50],[21,55],[22,00],[22,05],[22,10],[22,15],[23,00]] 

t = [datetime.datetime(2000,12,01,times[i][0],times[i][1]) for i in np.arange(len(times))]

amp_n = np.linspace(0,20000,13)
amp_c = np.linspace(20000,0,13)


for i in np.arange(len(amp_n)):
   plt.plot([t[i],t[i+1]],[amp_n[i],amp_n[i]],c=line_cols[2])
   plt.plot([t[i],t[i+1]],[amp_c[i],amp_c[i]],c=line_cols[1])

for i in np.arange(len(amp_n)-1):
   plt.plot([t[i+1],t[i+1]],[amp_n[i],amp_n[i+1]],c=line_cols[2])
   plt.plot([t[i+1],t[i+1]],[amp_c[i],amp_c[i+1]],c=line_cols[1])

majorFormatter = mpl.dates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(majorFormatter)

plt.xlabel('Time (hh:mm UTC)')
plt.ylabel(R'Amplitude (kg s$^\mathrm{-4}$)')
plt.ylim(-1000,21000)
plt.yticks([0,5000,10000,15000,20000])

plt.text(0.1,0.54,R'F$_\mathrm{xy}$',color=line_cols[2],transform=plt.gca().transAxes,fontsize=30)
plt.text(0.1,0.42,R'F$_\mathrm{z}$',color=line_cols[1],transform=plt.gca().transAxes,fontsize=30)

plt.gcf().autofmt_xdate()

plt.tight_layout()

plt.savefig('evolution_amp.png', dpi=600)

plt.show()
