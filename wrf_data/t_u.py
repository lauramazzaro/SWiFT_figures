# Add new colorbars which aren't available in my version of python (i.e. viridis)
execfile('../new_cmaps.py')

# Modify plotting parameters!
execfile('../new_params.py')

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
import glob

plt.figure(figsize=(15,10))

dh_xy = np.load('c_xy_20000_2000_2200.npz')
dh_z = np.load('c_z_20000_2000_2300.npz')
dh_u = np.load('unp_2000_2300.npz')
dh_t = np.load('../experimental_data/tower_all.npz')



print 'Approximate heights plotted: '+ str(np.mean(dh_u['z'][:,4]-dh_u['z'][:,0])) + 'm and '+str(np.mean(dh_u['z'][:,10]-dh_u['z'][:,0]))+'m'

# Format datetime: 
t_xy = dh_xy['t']
t_xy = [datetime.datetime(2013,11,8,int(t_xy[i])+12,int((t_xy[i]*60)%60),int((t_xy[i]*60*60)%60),int((t_xy[i]*60*60*10)%10)) for i in np.arange(len(t_xy)) ]
t_z = dh_z['t']
t_z = [datetime.datetime(2013,11,8,int(t_z[i])+12,int((t_z[i]*60)%60),int((t_z[i]*60*60)%60),int((t_z[i]*60*60*10)%10)) for i in np.arange(len(t_z)) ]
t_u = dh_u['t']
t_u = [datetime.datetime(2013,11,8,int(t_u[i])+12,int((t_u[i]*60)%60),int((t_u[i]*60*60)%60),int((t_u[i]*60*60*10)%10)) for i in np.arange(len(t_u)) ]
#print "Loading t is soooo slow...."
#t_t = dh_t['t']
#print 'There we go!'

# Extract U:
u_xy = dh_xy['u'][:,[4,10]]
v_xy = dh_xy['v'][:,[4,10]]
U_xy = ((u_xy)**2+(v_xy)**2)**(1/2.)
u_z = dh_z['u'][:,[4,10]]
v_z = dh_z['v'][:,[4,10]]
U_z = ((u_z)**2+(v_z)**2)**(1/2.)
u_u = dh_u['u'][:,[4,10]]
v_u = dh_u['v'][:,[4,10]]
U_u = ((u_u)**2+(v_u)**2)**(1/2.)
u_t = dh_t['u'][:,[5,8]]
v_t = dh_t['v'][:,[5,8]]
U_t = ((u_t)**2+(v_t)**2)**(1/2.)


for i in np.arange(len(glob.glob('002*npz'))):
   dh = np.load(glob.glob('002*npz')[i])
   U = ((dh['u'][:,[5,8]])**2+(dh['v'][:,[5,8]])**2)**(1/2.)
   t = dh['t']
   t = [datetime.datetime(2013,11,8,int(t[i])+12,int((t[i]*60)%60),int((t[i]*60*60)%60),int((t[i]*60*60*10)%10)) for i in np.arange(len(t)) ]
   plt.subplot(2,1,1)
   plt.plot(t,U[:,0],c=line_cols[4],linewidth=1.5)
   plt.subplot(2,1,2)
   plt.plot(t,U[:,1],c=line_cols[4],linewidth=1.5)



plt.subplot(2,1,1)
plt.xticks([])
plt.plot(t_t,U_t[:,0],'k',linewidth=1.5)
#plt.plot(t_xy,U_xy[:,0],c=line_cols[3],linewidth=1.5)
plt.plot(t_z[:48000],U_z[:48000,0],c=line_cols[4],linewidth=1.5)
plt.plot(t_u,U_u[:,0],c=line_cols[2],linewidth=1.5)


plt.ylabel(R'U (m s$^\mathrm{-1}$)') 
plt.text(0.95,0.85,'(a)',transform=plt.gca().transAxes)
plt.xlim(datetime.datetime(2013,11,8,20,0,0,0),datetime.datetime(2013,11,8,22,0,0,0))

plt.subplot(2,1,2)
plt.plot(t_t,U_t[:,1],'k',linewidth=1.5)
#plt.plot(t_xy,U_xy[:,1],c=line_cols[3],linewidth=1.5)
plt.plot(t_z[:48000],U_z[:48000,1],c=line_cols[4],linewidth=1.5)
plt.plot(t_u,U_u[:,1],c=line_cols[2],linewidth=1.5)
plt.ylabel('U (m s$^\mathrm{-1}$)')
plt.text(0.95,0.85,'(b)',transform=plt.gca().transAxes)
plt.xlabel('Time (HH:MM UTC)')

plt.text(0.4,0.9,R'F$_\mathrm{xy+z}$',color=line_cols[4],transform=plt.gca().transAxes)
plt.text(0.5,0.9,R'F$_\mathrm{NP}$',color=line_cols[2],transform=plt.gca().transAxes)
plt.text(0.6,0.9,R'TTUT',color='black',transform=plt.gca().transAxes)

plt.xlim(datetime.datetime(2013,11,8,20,0,0,0),datetime.datetime(2013,11,8,22,0,0,0))
majorFormatter = mpl.dates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(majorFormatter)

plt.gcf().autofmt_xdate()
plt.tight_layout()

plt.savefig('t_u.png',dpi=600)
plt.show()

#np.savez('tower_means.npz',t=t,u=u,v=v,d=d,z=z,T=T,T_ave=T_ave,u_ave=u_ave,v_ave=v_ave,d_ave=d_ave)
