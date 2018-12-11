import numpy as np
import matplotlib.pyplot as plt

def find_spectra(dat,dt):

   #find number of points from input data:
   npts = int(len(dat))

   # Make it odd:
   npts = npts-(1-npts%2)

   # ----------- dat processing ------------
   # Crop data to uneven number of points
   dat = dat[:npts]
   # Remove mean from data:
   dat = dat - np.nanmean(dat)
   # Apply hamming window to data:
   dat = dat * np.hamming(npts)
   # Find fft from data
   dat_fft = np.fft.fftshift(np.fft.fft(dat))
   # Find the maximum possible frequency:
   max_freq = 1/dt
   # Find the frequency increment:
   df = max_freq/npts
   # Find Energy Spectrum!!!
   Ef = (1/(npts**2.))*(dat_fft*np.conj(dat_fft))
   # Crop the spectrym (since it's symmet.)
   Ef = Ef[len(Ef)/2:]
   # Create frequency vector:
   fs = 2*df*np.arange(np.floor(npts/2)+1)
   # ---------------------------------------

   return Ef,fs
