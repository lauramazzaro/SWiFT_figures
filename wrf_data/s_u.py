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

dh_xy = np.load('n_xy_20000_2120_2300.npz')
dh_z = np.load('s_z_20000_0400_0500.npz')
dh_u = np.load('unp_0400_0500.npz')
dh_t = np.load('../experimental_data/tower_all.npz')

z1 = 4
z2 = 10


print 'Approximate heights plotted: '+ str(np.mean(dh_u['z'][:,z1]-dh_u['z'][:,0]-5)) + 'm and '+str(np.mean(dh_u['z'][:,z2]-dh_u['z'][:,0]-5))+'m'

# Format datetime: 
#t_xy = dh_xy['t']
#t_xy = [datetime.datetime(2013,11,8,int(t_xy[i])-12,int((t_xy[i]*60)%60),int((t_xy[i]*60*60)%60),int((t_xy[i]*60*60*10)%10)) for i in np.arange(len(t_xy)) ]
t_z = dh_z['t']
t_z = np.array([datetime.datetime(2013,11,9,int(t_z[i])-12,int((t_z[i]*60)%60),int((t_z[i]*60*60)%60),int((t_z[i]*60*60*10)%10)) for i in np.arange(len(t_z))])
t_u = dh_u['t']
t_u = np.array([datetime.datetime(2013,11,9,int(t_u[i])-12,int((t_u[i]*60)%60),int((t_u[i]*60*60)%60),int((t_u[i]*60*60*10)%10)) for i in np.arange(len(t_u))])
print "Loading t is soooo slow...."
t_t = dh_t['t']
print 'There we go!'

# Extract U:
u_xy = dh_xy['u'][:,[z1,z2]]
v_xy = dh_xy['v'][:,[z1,z2]]
U_xy = ((u_xy)**2+(v_xy)**2)**(1/2.)
u_z = dh_z['u'][:,[z1,z2]]
v_z = dh_z['v'][:,[z1,z2]]
U_z = ((u_z)**2+(v_z)**2)**(1/2.)
u_u = dh_u['u'][:,[z1,z2]]
v_u = dh_u['v'][:,[z1,z2]]
U_u = ((u_u)**2+(v_u)**2)**(1/2.)
u_t = dh_t['u'][:,[5,8]]
v_t = dh_t['v'][:,[5,8]]
U_t = ((u_t)**2+(v_t)**2)**(1/2.)

xmin = datetime.datetime(2013,11,9,4,0,0,0)
xmax = datetime.datetime(2013,11,9,5,0,0,0)

plt.subplot(2,1,1)
pt_gap = 100
plt.plot(t_t[np.arange(0,len(t_t)-1,pt_gap)],U_t[np.arange(0,len(t_t)-1,pt_gap),1],'k.',linewidth=1.5)
pt_gap = 20
#plt.plot(t_xy,U_xy[:,0],c=line_cols[3],linewidth=1.5)
plt.plot(t_z[np.arange(0,len(t_z)-1,pt_gap)],U_z[np.arange(0,len(t_z)-1,pt_gap),1],'.',c=line_cols[1],linewidth=1.5)
plt.plot(t_u[np.arange(0,len(t_u)-1,pt_gap)],U_u[np.arange(0,len(t_u)-1,pt_gap),1],'.',c=line_cols[2],linewidth=1.5)

plt.ylabel(R'U (m s$^\mathrm{-1}$)') 
plt.text(0.95,0.85,'(a)',transform=plt.gca().transAxes)

plt.xlim(xmin,xmax)
plt.xticks([])
plt.yticks([4,8,12,16])

ax2 = plt.gca().twiny()
mn, mx = [xmin-datetime.timedelta(hours=-18),xmax-datetime.timedelta(hours=-18)]
ax2.set_xlim(mn,mx)
ax2.set_xlabel('Time (HH:MM CST)')
majorFormatter = mpl.dates.DateFormatter('%H:%M')
ax2.xaxis.set_major_formatter(majorFormatter)
ax2.xaxis.grid()


plt.subplot(2,1,2)
pt_gap = 100
plt.plot(t_t[np.arange(0,len(t_t)-1,pt_gap)],U_t[np.arange(0,len(t_t)-1,pt_gap),0],'.k',linewidth=1.5)
pt_gap = 20
#plt.plot(t_xy,U_xy[:,1],c=line_cols[3],linewidth=1.5)
plt.plot(t_z[np.arange(0,len(t_z)-1,pt_gap)],U_z[np.arange(0,len(t_z)-1,pt_gap),0],'.',c=line_cols[1],linewidth=1.5)
plt.plot(t_u[np.arange(0,len(t_u)-1,pt_gap)],U_u[np.arange(0,len(t_u)-1,pt_gap),0],'.',c=line_cols[2],linewidth=1.5)
plt.ylabel('U (m s$^\mathrm{-1}$)')
plt.text(0.95,0.85,'(b)',transform=plt.gca().transAxes)
plt.xlabel('Time (HH:MM UTC)')

#plt.text(0.3,0.9,R'F$_\mathrm{20000xy}$',color=line_cols[3],transform=plt.gca().transAxes)
plt.text(0.4,0.9,R'F$_\mathrm{20000z}$',color=line_cols[1],transform=plt.gca().transAxes)
plt.text(0.5,0.9,R'F$_\mathrm{NP}$',color=line_cols[2],transform=plt.gca().transAxes)
plt.text(0.6,0.9,R'TTUT',color='black',transform=plt.gca().transAxes)

plt.xlim(xmin,xmax)
plt.yticks([10,15,20])
plt.ylim([5,20])
plt.gca().xaxis.grid()
majorFormatter = mpl.dates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(majorFormatter)

plt.tight_layout()

plt.savefig('s_u.png',dpi=600)
plt.show()

# Data is cropped to right time period and saved manually
#np.savez('stable_data.npz',t_t=t_t,t_z=t_z,t_u=t_u,u_t=u_t,u_z=u_z,u_u=u_u,v_t=v_t,v_z=v_z,v_u=v_u)
