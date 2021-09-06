'''
Calculate the volume of the n-dimensional spehere a function of the dimension using a simple hit-or-miss Monte Carlo.
'''

from __future__ import print_function, division
import numpy as np
import scipy.special
import pylab as plt
import time

Dmax = 30 # Largest dimension
N = int(1e7) # Monte Carlo samples

data = []

for D in np.arange(2,Dmax+1): # Loop
    t0=time.time()

    all = np.random.uniform(-1,1, D*N).reshape(N,D) # Generate points in cube

    distance = np.sum(all**2,axis=1)**0.5 # Distance from cube center

    Ninside = np.sum(distance<=1) # Number of points within sphere
    fractioninside = Ninside/N # Fraction of points within sphere
    cube = 2**D # Volume of the cube (from -1 to 1)
    sphere = fractioninside * cube # Volume of the sphere

    solution = np.pi**(D/2) / scipy.special.gamma( D/2 + 1) # True value
    diff= np.abs(sphere-solution)/solution # Error

    t=time.time()-t0
    print("D=%i\tN=%i\tN_in=%06d\tV=%.5f\t\tSol=%.5f\t\tdiff=%.5f\tt=%.2fs" %(D,N,Ninside,sphere,solution,diff,t))

    data.append([D,sphere,solution,diff]) # Store data


# Plots...
dims, my,true,errors = np.array(data).T
fig, axs= plt.subplots(2, 1,figsize=(5,10))
axs[0].plot(dims,my,label='my',ls='-',marker='x')
axs[0].plot(dims,true,label='true',ls='-')
axs[1].plot(dims,errors,label='errors')
[ax.legend() for ax in axs]
plt.show()