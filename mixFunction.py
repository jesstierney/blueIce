import numpy as np
import scipy as sp
# Function for the convolution (simulated permeation/mixing)
def mixIce(depth, dstep,SimVal,sigma):
    # first we need the time series to be at an even depth interval
    # first get total depth of core relative to starting middle depth
    # zmid = ice[['TopDepth', 'BottomDepth']].mean(axis=1)
    z = depth - depth[0]
    # target depth for interpolation using dstep average sample length
    zp = np.arange(0,np.max(z),dstep)
    # interpolate the simulated value array
    f = sp.interpolate.interp1d(z,SimVal,axis=0,bounds_error=False,fill_value="extrapolate")
    co2int = f(zp)
    # set the bounds of the kernel, has to be less than 0.5 the length of timeseries.
    bound=0.30*len(zp)*dstep
    zp2 = np.arange(-bound,bound,dstep)
    # sigma is the length scale of smoothing in m.
    part1=1./(sigma*np.sqrt(2.*np.pi))
    part2=np.exp(-zp2**2/(2*sigma**2))
    G=part1*part2
    # normalize
    G = G/np.sum(G)
    ### convolve
    ### vectorized
    co2c = co2int - np.mean(co2int,0)
    co2mix = sp.signal.fftconvolve(co2c,G[np.newaxis, :].T,axes=0,mode='same') + np.mean(co2int,0)
    # interpolate simulated points back to sample locations
    f = sp.interpolate.interp1d(zp,co2mix,axis=0,bounds_error=False,fill_value="extrapolate")
    co2mixInt = f(z)
    return z, zp, co2mix, co2mixInt