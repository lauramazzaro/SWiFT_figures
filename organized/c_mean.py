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

dh = np.load('convective_data.npz')

# Load datetime:
print('Loading datetime...')
print('xy')
t_xy = dh['t_xy']
print('z')
t_z = dh['t_z']
print('unp')
t_u = dh['t_u']
print "t"
t_t = dh['t_t']
print 'There we go!'

# Extract U:
u_xy = dh['u_xy']
v_xy = dh['v_xy']
U_xy = ((u_xy)**2+(v_xy)**2)**(1/2.)
u_z = dh['u_z']
v_z = dh['v_z']
U_z = ((u_z)**2+(v_z)**2)**(1/2.)
u_u = dh['u_u']
v_u = dh['v_u']
U_u = ((u_u)**2+(v_u)**2)**(1/2.)
u_t = dh['u_t']
v_t = dh['v_t']
U_t = ((u_t)**2+(v_t)**2)**(1/2.)

# Do the averaging!! 
dt = 0.1
dt_t = 0.02
t_ave = 10

ave_ind = np.arange(0,len(t_xy)+10*60/dt,10*60/dt)
ave_ind = ave_ind.tolist()
ave_ind_t = np.arange(0,len(t_t)+10*60/dt_t-1,10*60/dt_t)
ave_ind_t = ave_ind_t.tolist()

xmin = datetime.datetime(2013,11,8,20,5,0,0)
xmax = datetime.datetime(2013,11,8,21,55,0,0)

U_xy_ave = np.zeros([len(ave_ind)-1,2])
U_z_ave = np.zeros([len(ave_ind)-1,2])
U_u_ave = np.zeros([len(ave_ind)-1,2])
U_t_ave = np.zeros([len(ave_ind_t)-1,2])

U_xy_std_1 = np.zeros([len(ave_ind)-1,2])
U_z_std_1 = np.zeros([len(ave_ind)-1,2])
U_u_std_1 = np.zeros([len(ave_ind)-1,2])
U_t_std_1 = np.zeros([len(ave_ind_t)-1,2])

U_xy_std_2 = np.zeros([len(ave_ind)-1,2])
U_z_std_2 = np.zeros([len(ave_ind)-1,2])
U_u_std_2 = np.zeros([len(ave_ind)-1,2])
U_t_std_2 = np.zeros([len(ave_ind_t)-1,2])

for i in np.arange(len(ave_ind)-1):

   i1 = ave_ind[i]
   i2 = ave_ind[i+1]

   U_xy_ave[i,:] = np.squeeze(np.nanmean(U_xy[i1:i2,:],0))
   U_z_ave[i,:]  = np.squeeze(np.nanmean(U_z[i1:i2,:],0))
   U_u_ave[i,:]  = np.squeeze(np.nanmean(U_u[i1:i2,:],0))

   U_xy_std = (np.nanmean((U_xy[i1:i2,:]-U_xy_ave[i,:])**2,0))**(.5)
   U_z_std  = (np.nanmean((U_z[i1:i2,:]-U_z_ave[i,:])**2,0))**(.5)
   U_u_std  = (np.nanmean((U_u[i1:i2,:]-U_u_ave[i,:])**2,0))**(.5)

   U_xy_std_1[i,:] = U_xy_ave[i,:] - U_xy_std
   U_xy_std_2[i,:] = U_xy_ave[i,:] + U_xy_std
   U_z_std_1[i,:] = U_z_ave[i,:] - U_z_std
   U_z_std_2[i,:] = U_z_ave[i,:] + U_z_std
   U_u_std_1[i,:] = U_u_ave[i,:] - U_u_std
   U_u_std_2[i,:] = U_u_ave[i,:] + U_u_std

for i in np.arange(len(ave_ind_t)-1):

   i1 = ave_ind_t[i]
   i2 = ave_ind_t[i+1]

   U_t_ave[i,:] = np.squeeze(np.nanmean(U_t[i1:i2,:],0))

   U_t_std  = (np.nanmean((U_t[i1:i2,:]-U_t_ave[i,:])**2))**(.5)

   U_t_std_1[i,:] = U_t_ave[i,:] - U_t_std
   U_t_std_2[i,:] = U_t_ave[i,:] + U_t_std

t_xy = t_xy[ave_ind[:-1]]
t_xy = [t_xy[i]+datetime.timedelta(minutes = 5) for i in np.arange(len(ave_ind)-1)]
t_z = t_z[ave_ind[:-1]]
t_z = [t_z[i]+datetime.timedelta(minutes = 5) for i in np.arange(len(ave_ind)-1)]
t_u = t_u[ave_ind[:-1]]
t_u = [t_u[i]+datetime.timedelta(minutes = 5) for i in np.arange(len(ave_ind)-1)]
t_t = t_t[ave_ind_t[:-1]]
t_t = [t_t[i]+datetime.timedelta(minutes = 5) for i in np.arange(len(ave_ind_t)-1)]

plt.subplot(2,1,1)

plt.plot(t_xy,U_xy_ave[:,1],c=line_cols[0],linewidth=2)
plt.plot(t_z,U_z_ave[:,1],c=line_cols[1],linewidth=2)
plt.plot(t_u,U_u_ave[:,1],c=line_cols[2],linewidth=2)
plt.plot(t_t,U_t_ave[:,1],'k',linewidth=2)

plt.fill_between(t_xy,U_xy_std_1[:,1],U_xy_std_2[:,1],alpha=0.3,color=line_cols[0])
plt.fill_between(t_z,U_z_std_1[:,1],U_z_std_2[:,1],alpha=0.3,color=line_cols[1])
plt.fill_between(t_u,U_u_std_1[:,1],U_u_std_2[:,1],alpha=0.3,color=line_cols[2])
plt.fill_between(t_t,U_t_std_1[:,1],U_t_std_2[:,1],alpha=0.3,color=line_cols[-1])

plt.ylabel(R'U (m s$^\mathrm{-1}$)')
plt.yticks([4,8,12,16])

plt.text(0.95,0.85,'(a)',transform=plt.gca().transAxes)

plt.ylim(4,18)
plt.yticks([4,8,12,16])
plt.xlim(xmin,xmax)
plt.xticks([])

# new axis:
ax2 = plt.gca().twiny()
mn, mx = [xmin-datetime.timedelta(hours=-18),xmax-datetime.timedelta(hours=-18)]
ax2.set_xlim(mn,mx)
ax2.set_xlabel('Time (HH:MM CST)')
majorFormatter = mpl.dates.DateFormatter('%H:%M')
ax2.xaxis.set_major_formatter(majorFormatter)
ax2.xaxis.grid()


plt.subplot(2,1,2)

plt.plot(t_xy,U_xy_ave[:,0],c=line_cols[0],linewidth=2)
plt.fill_between(t_xy,U_xy_std_1[:,0],U_xy_std_2[:,0],alpha=0.3,color=line_cols[0])
plt.plot(t_z,U_z_ave[:,0],c=line_cols[1],linewidth=2)
plt.fill_between(t_z,U_z_std_1[:,0],U_z_std_2[:,0],alpha=0.3,color=line_cols[1])
plt.plot(t_u,U_u_ave[:,0],c=line_cols[2],linewidth=2)
plt.fill_between(t_u,U_u_std_1[:,0],U_u_std_2[:,0],alpha=0.3,color=line_cols[2])
plt.plot(t_t,U_t_ave[:,0],'k',linewidth=2)
plt.fill_between(t_t,U_t_std_1[:,0],U_t_std_2[:,0],alpha=0.3,color=line_cols[-1])

plt.ylabel('U (m s$^\mathrm{-1}$)')

plt.text(0.95,0.85,'(b)',transform=plt.gca().transAxes)

plt.xlabel('Time (HH:MM UTC)')

plt.text(0.3,0.9,R'F$_\mathrm{20000xy}$',color=line_cols[0],transform=plt.gca().transAxes)
plt.text(0.4,0.9,R'F$_\mathrm{20000z}$',color=line_cols[1],transform=plt.gca().transAxes)
plt.text(0.5,0.9,R'F$_\mathrm{NP}$',color=line_cols[2],transform=plt.gca().transAxes)
plt.text(0.6,0.9,R'TTUT',color='black',transform=plt.gca().transAxes)

plt.xlim(xmin,xmax)
majorFormatter = mpl.dates.DateFormatter('%H:%M')
plt.ylim(4,18)
plt.yticks([4,8,12,16])

plt.gca().xaxis.grid()
plt.gca().xaxis.set_major_formatter(majorFormatter)

#plt.gcf().autofmt_xdate()
plt.tight_layout()

plt.savefig('c_mean.png',dpi=600)
plt.show()
