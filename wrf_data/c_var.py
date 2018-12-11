# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime

plt.figure(figsize=(15,10))

dh_xy = np.load('c_xy_20000_2000_2200.npz')
dh_z = np.load('c_z_20000_2000_2300.npz')
dh_u = np.load('unp_2000_2300.npz')
dh_t = np.load('../experimental_data/tower_all.npz')



print 'Approximate heights plotted: '+ str(np.mean(dh_u['z'][:,4]-dh_u['z'][:,0])) + 'm and '+str(np.mean(dh_u['z'][:,10]-dh_u['z'][:,0]))+'m'

# Format datetime: 
t_xy = dh_xy['t']
t_z = dh_z['t']
t_u = dh_u['t']
#print "Loading t is soooo slow...."
#t_t = dh_t['t']
#print 'There we go!'

# Extract U:
u_xy = dh_xy['u'][:,[4,10]]
u_z = dh_z['u'][:,[4,10]]
u_u = dh_u['u'][:,[4,10]]
u_t = dh_t['u'][:,[5,8]]

ave_t = 10

u_xyave = np.zeros(u_xy.shape)
ave_ind_xy = np.linspace(0,len(t_xy),(t_xy[-1]-t_xy[0])*60/ave_t)
for i in np.arange(len(ave_ind_xy)-1):
   istart = ave_ind_xy[i]
   iend = ave_ind_xy[i+1]
   umean = np.mean(u_xy[istart:iend],0)
   u_xyave[istart:iend,:] = [umean for p in np.arange(istart,iend)]

u_xyfluct = u_xy - u_xyave
var_xy = u_xyfluct*u_xyfluct

u_zave = np.zeros(u_z.shape)
ave_ind_z = np.linspace(0,len(t_z),(t_z[-1]-t_z[0])*60/ave_t)
for i in np.arange(len(ave_ind_z)-1):
   istart = ave_ind_z[i]
   iend = ave_ind_z[i+1]
   umean = np.mean(u_z[istart:iend],0)
   u_zave[istart:iend,:] = [umean for p in np.arange(istart,iend)]

u_zfluct = u_z - u_zave
var_z = u_zfluct*u_zfluct

u_uave = np.zeros(u_u.shape)
ave_ind_u = np.linspace(0,len(t_u),(t_u[-1]-t_u[0])*60/ave_t)
for i in np.arange(len(ave_ind_u)-1):
   istart = ave_ind_u[i]
   iend = ave_ind_u[i+1]
   umean = np.mean(u_u[istart:iend],0)
   u_uave[istart:iend,:] = [umean for p in np.arange(istart,iend)]

u_ufluct = u_u - u_uave
var_u = u_ufluct*u_ufluct


u_tave = np.zeros(u_t.shape)
ave_ind_t = np.linspace(0,u_t.shape[0],(u_t.shape[0])*60/ave_t)
for i in np.arange(len(ave_ind_t)-1):
   istart = ave_ind_t[i]
   iend = ave_ind_t[i+1]
   umean = np.mean(u_t[istart:iend],0)
   u_tave[istart:iend,:] = [umean for p in np.arange(istart,iend)]

u_tfluct = u_t - u_tave
var_t = u_tfluct*u_tfluct




t_u = [datetime.datetime(2013,11,8,int(t_u[i])+12,int((t_u[i]*60)%60),int((t_u[i]*60*60)%60),int((t_u[i]*60*60*10)%10)) for i in np.arange(len(t_u)) ]
t_xy = [datetime.datetime(2013,11,8,int(t_xy[i])+12,int((t_xy[i]*60)%60),int((t_xy[i]*60*60)%60),int((t_xy[i]*60*60*10)%10)) for i in np.arange(len(t_xy)) ]
t_z = [datetime.datetime(2013,11,8,int(t_z[i])+12,int((t_z[i]*60)%60),int((t_z[i]*60*60)%60),int((t_z[i]*60*60*10)%10)) for i in np.arange(len(t_z)) ]


plt.subplot(2,1,1)
plt.xticks([])
plt.plot(t_t,U_t[:,0],'k',linewidth=1.5)
plt.plot(t_xy,U_xy[:,0],c=line_cols[3],linewidth=1.5)
plt.plot(t_z,U_z[:,0],c=line_cols[1],linewidth=1.5)
plt.plot(t_u,U_u[:,0],c=line_cols[2],linewidth=1.5)
plt.ylabel(R'U (m s$^\mathrm{-1}$)') 
plt.text(0.95,0.85,'(a)',transform=plt.gca().transAxes)
plt.xlim(datetime.datetime(2013,11,8,20,0,0,0),datetime.datetime(2013,11,8,22,0,0,0))

plt.subplot(2,1,2)
plt.plot(t_t,U_t[:,1],'k',linewidth=1.5)
plt.plot(t_xy,U_xy[:,1],c=line_cols[3],linewidth=1.5)
plt.plot(t_z,U_z[:,1],c=line_cols[1],linewidth=1.5)
plt.plot(t_u,U_u[:,1],c=line_cols[2],linewidth=1.5)
plt.ylabel('U (m s$^\mathrm{-1}$)')
plt.text(0.95,0.85,'(b)',transform=plt.gca().transAxes)
plt.xlabel('Time (HH:MM UTC)')

plt.text(0.3,0.9,R'F$_\mathrm{20000xy}$',color=line_cols[3],transform=plt.gca().transAxes)
plt.text(0.4,0.9,R'F$_\mathrm{20000z}$',color=line_cols[1],transform=plt.gca().transAxes)
plt.text(0.5,0.9,R'F$_\mathrm{NP}$',color=line_cols[2],transform=plt.gca().transAxes)
plt.text(0.6,0.9,R'TTUT',color='black',transform=plt.gca().transAxes)

plt.xlim(datetime.datetime(2013,11,8,20,0,0,0),datetime.datetime(2013,11,8,22,0,0,0))
majorFormatter = mpl.dates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(majorFormatter)

plt.gcf().autofmt_xdate()
plt.tight_layout()

plt.savefig('c_u.png',dpi=600)
plt.show()

#np.savez('tower_means.npz',t=t,u=u,v=v,d=d,z=z,T=T,T_ave=T_ave,u_ave=u_ave,v_ave=v_ave,d_ave=d_ave)
