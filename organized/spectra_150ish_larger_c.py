execfile('../new_cmaps.py')
execfile('../new_params.py')
execfile('../new_spectra.py')


# Temporal resolution:
dt = 0.1
dt_t = 0.02
 
plt.figure(figsize=(22,6))
t_ave = 10 # in minutes


# ------------- CONVECTIVE -------------


#  REFERENCE -------------
x_ref = np.array([9*10**(-2),9*10**(-1)])
y_0 = 1E-3*x_ref**(-1)
plt.subplot(1,3,1)
plt.loglog(x_ref,y_0,c=line_cols[-1])
plt.subplot(1,3,2)
plt.loglog(x_ref,y_0,c=line_cols[-1])
plt.subplot(1,3,3)
plt.loglog(x_ref,y_0,c=line_cols[-1])
x_ref = np.array([10**(0),10**(1)])
y_0 = 1E-3*x_ref**(-5/3.)
plt.subplot(1,3,1)
plt.loglog(x_ref,y_0,c=line_cols[-1])
plt.subplot(1,3,2)
plt.loglog(x_ref,y_0,c=line_cols[-1])
plt.subplot(1,3,3)
plt.loglog(x_ref,y_0,c=line_cols[-1])
plt.text(0.48,0.77,'-1',color=line_cols[-1],transform=plt.gca().transAxes)
plt.text(0.67,0.65,'-5/3',color=line_cols[-1],transform=plt.gca().transAxes)
# ------------------------


plt.subplot(1,3,1)

dh = np.load('convective_data.npz')

u_xy = dh['u_xy']
u_z  = dh['u_z']
u_u  = dh['u_u']
u_t  = dh['u_t']

v_xy = dh['v_xy']
v_z  = dh['v_z']
v_u  = dh['v_u']
v_t  = dh['v_t']

dh = np.load('u_larger_c.npz')
u_u_2 = dh['u']
v_u_2 = dh['v']

dh = np.load('xy_larger_c.npz')
u_xy_2 = dh['u']
v_xy_2 = dh['v']

dh = np.load('z_larger_c.npz')
u_z_2 = dh['u']
v_z_2 = dh['v']

u_xy = (u_xy**2 + u_xy**2)**(0.5)
u_xy_2 = (u_xy_2**2 + u_xy_2**2)**(0.5)
u_z  = (u_z**2  + u_z**2)**(0.5)
u_z_2  = (u_z_2**2  + u_z_2**2)**(0.5)
u_u  = (u_u**2  + u_u**2)**(0.5)
u_u_2  = (u_u_2**2  + u_u_2**2)**(0.5)
u_t  = (u_t**2  + u_t**2)**(0.5)

# data intervals:
split = np.arange(0,u_xy.shape[0],t_ave*60/dt)
split_t = np.arange(0,u_t.shape[0],t_ave*60/dt_t)

Ef_xy = [None]*(len(split)-1)
Ef_z = [None]*(len(split)-1)
Ef_u = [None]*(len(split)-1)
Ef_xy_2 = [None]*(len(split)-1)
Ef_z_2 = [None]*(len(split)-1)
Ef_u_2 = [None]*(len(split)-1)
Ef_t = [None]*(len(split_t)-1)

for i in np.arange(len(split)-1):

   dat_xy = u_xy[split[i]:split[i+1],1]
   dat_z = u_z[split[i]:split[i+1],1]
   dat_u = u_u[split[i]:split[i+1],1]
   dat_xy_2 = u_xy_2[split[i]:split[i+1],10]
   dat_z_2 = u_z_2[split[i]:split[i+1],10]
   dat_u_2 = u_u_2[split[i]:split[i+1],10]

   Ef_xy[i],fs_xy = find_spectra(dat_xy,dt)
   Ef_z[i],fs_z = find_spectra(dat_z,dt)
   Ef_u[i],fs_u = find_spectra(dat_u,dt)
   Ef_xy_2[i],fs_xy_2 = find_spectra(dat_xy_2,dt)
   Ef_z_2[i],fs_z_2 = find_spectra(dat_z_2,dt)
   Ef_u_2[i],fs_u_2 = find_spectra(dat_u_2,dt)

for i in np.arange(len(split_t)-1):

   dat = u_t[split_t[i]:split_t[i+1],1]
   for j in np.arange(len(dat)):
      if np.isnan(dat[j]):
         dj = 1
         while np.isnan(dat[j+dj]):
            dj += 1
         for n in np.arange(dj):
            dat[j+n] = dat[j+n-1] +(n+1)*(dat[j+dj]-dat[j-1])/(dj+1)
   Ef_t[i],fs_t = find_spectra(dat,dt_t)


plt.loglog(fs_xy,np.mean(Ef_xy[:],axis=0),c = line_cols[0],label=R'$\mathrm{C_{xy20000}}$')
#plt.loglog(fs_z,np.mean(Ef_z[:],axis=0),c = line_cols[1],label=R'$\mathrm{C_{z20000}}$')
#plt.loglog(fs_u,np.mean(Ef_u[:],axis=0),c = line_cols[2],label=R'$\mathrm{C_{NP}}$')
plt.loglog(fs_xy_2,np.mean(Ef_xy_2[:],axis=0),'--',c = line_cols[0],label=R'$\mathrm{C_{xy20000L}}$')
#plt.loglog(fs_z_2,np.mean(Ef_z_2[:],axis=0),'--',c = line_cols[1],label=R'$\mathrm{C_{z20000L}}$')
#plt.loglog(fs_u_2,np.mean(Ef_u_2[:],axis=0),'--',c = line_cols[2],label=R'$\mathrm{C_{NPL}}$')
plt.loglog(fs_t,np.mean(Ef_t[:],axis=0),c = 'k',label='TTUT')
plt.text(0.9,0.9,'(a)',transform=plt.gca().transAxes)
plt.ylabel(R'$\mathrm{F_{ut}}$ (m$^\mathrm{3}s^\mathrm{-2}$)')
plt.xlabel(R'$f$ (s$^\mathrm{-1}$)')

plt.yticks([1e-10,1e-8,1e-6,1e-4,1e-2,1e0])
plt.text(0.1,0.4,R'F$_\mathrm{2000xy}$',color=line_cols[0],transform=plt.gca().transAxes)
plt.text(0.1,0.3,R'F$_\mathrm{2000z}$',color=line_cols[1],transform=plt.gca().transAxes)
plt.text(0.1,0.2,'F$_\mathrm{NP}$',color=line_cols[2],transform=plt.gca().transAxes)
plt.text(0.1,0.1,'TTUT',color='k',transform=plt.gca().transAxes)

# ------------- NEUTRAL -------------

plt.subplot(1,3,2)


plt.loglog(fs_z,np.mean(Ef_z[:],axis=0),c = line_cols[1],label=R'$\mathrm{C_{z20000}}$')
plt.loglog(fs_z_2,np.mean(Ef_z_2[:],axis=0),'--',c = line_cols[1],label=R'$\mathrm{C_{z20000L}}$')
plt.loglog(fs_t,np.mean(Ef_t[:],axis=0),c = 'k',label='TTUT')

plt.text(0.9,0.9,'(b)',transform=plt.gca().transAxes)
#plt.ylabel(R'$\mathrm{F_{ux}}$ (m$^\mathrm{3}s^\mathrm{-2}$)')
plt.xlabel(R'$f$ (s$^\mathrm{-1}$)')
plt.yticks([])
#plt.yticks([1e-10,1e-8,1e-6,1e-4,1e-2,1e0])
plt.ylim(1e-10,1e0)

# ------------- STABLE -------------

plt.subplot(1,3,3)

plt.loglog(fs_u,np.mean(Ef_u[:],axis=0),c = line_cols[2],label=R'$\mathrm{C_{NP}}$')
plt.loglog(fs_u_2,np.mean(Ef_u_2[:],axis=0),'--',c = line_cols[2],label=R'$\mathrm{C_{NPL}}$')
plt.loglog(fs_t,np.mean(Ef_t[:],axis=0),c = 'k',label='TTUT')

plt.text(0.9,0.9,'(c)',transform=plt.gca().transAxes)
#plt.ylabel(R'$\mathrm{F_{ux}}$ (m$^\mathrm{3}s^\mathrm{-2}$)')
plt.xlabel(R'$f$ (s$^\mathrm{-1}$)')
plt.yticks([])
#plt.yticks([1e-10,1e-8,1e-6,1e-4,1e-2,1e0])
plt.ylim(1e-10,1e0)

plt.tight_layout()

plt.savefig('spectra_150ish_larger_c.png',dpi=600)
plt.show()
