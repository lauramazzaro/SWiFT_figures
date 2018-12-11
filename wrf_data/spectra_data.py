execfile('../new_cmaps.py')
execfile('../new_params.py')
execfile('../new_spectra.py')


# Temporal resolution:
dt = 0.1

plt.figure(figsize=(12,8))
t_ave = 10 # in minutes

dh = np.load('c_xy_20000_2000_2200.npz')
u = dh['u'][:,[4,10]]

# data intervals: 
split = np.arange(0,u.shape[0],t_ave*60/dt)

Ef = [None]*(len(split)-1)
for i in np.arange(len(split)-1):

   dat = u[split[i]:split[i+1],0]
   Ef[i],fs = find_spectra(dat,dt)

plt.loglog(fs,np.mean(Ef[:],axis=0),c = line_cols[1],label=R'$\mathrm{C_{xy20000}}$') 


dh = np.load('c_z_20000_2000_2300.npz')
u = dh['u'][:,[4,10]]

Ef = [None]*(len(split)-1)
# data intervals: 
for i in np.arange(len(split)-1):

   dat = u[split[i]:split[i+1],0]
   Ef[i],fs = find_spectra(dat,dt)

plt.loglog(fs,np.mean(Ef[:],axis=0),c = line_cols[2],label=R'$\mathrm{C_{z20000}}$') 

 
dh = np.load('unp_2000_2300.npz')
u = dh['u'][:,[4,10]]

Ef = [None]*(len(split)-1)
# data intervals: 
for i in np.arange(len(split)-1):

   dat = u[split[i]:split[i+1],0]
   Ef[i],fs = find_spectra(dat,dt)

plt.loglog(fs,np.mean(Ef[:],axis=0),c = line_cols[3],label=R'$\mathrm{C_{NP}}$')


dh = np.load('../experimental_data/tower_all.npz')
u = dh['u'][1440000:1800000,[5,8]]
dt = 0.02

# data intervals: 
split = np.arange(0,u.shape[0],t_ave*60/dt)

Ef = [None]*(len(split)-1)
# data intervals: 
for i in np.arange(len(split)-1):

   dat = u[split[i]:split[i+1],0]

   for j in np.arange(len(dat)):
      if np.isnan(dat[j]):
         dj = 1
         while np.isnan(dat[j+dj]):
            dj += 1
         for n in np.arange(dj):
            dat[j+n] = dat[j+n-1] +(n+1)*(dat[j+dj]-dat[j-1])/(dj+1)

   Ef[i],fs = find_spectra(dat,dt)

plt.loglog(fs,np.mean(Ef[:],axis=0),'k',label=R'TTUT')

plt.legend()
plt.show()

