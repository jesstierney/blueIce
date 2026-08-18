# function to do time averaging
import numpy as np
# currently assuming provided age error on Ar is a 2-sigma error.
def iceTimeAvg(age, abserr, timeavg, simAge, simValue, N):
    ValSim = np.empty((len(age),N))
    for i in range(len(age)):
        # select age right now
        AgeN = age[i]
        # select absolute age error
        AgeEA = abserr[i]
        # first select an Age mean value using abs error
        ageMSamps = np.random.normal(AgeN,AgeEA/2,N)
        # using these find average CO2 values within +/- the relative error
        # here the relative error is effectively treated as a uniform distribution
        for j, samp in enumerate(ageMSamps):
            mask = (simAge >= samp - timeavg/2) & (simAge <= samp + timeavg/2)
            ValSim[i, j] = simValue[mask].mean()
    return ValSim