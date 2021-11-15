# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:11:01 2021

@author: thedi
"""

import numpy as np
import matplotlib.pyplot as plt
import climlab
from climlab import constants as const

predmodel26 = np.loadtxt('RCP3PD_MIDYR_CONC.DAT', skiprows = 40)
predmodel45 = np.loadtxt('RCP45_MIDYR_CONC.DAT', skiprows = 40)
predmodel60 = np.loadtxt('RCP6_MIDYR_CONC.DAT', skiprows = 40)
predmodel85 = np.loadtxt('RCP85_MIDYR_CONC.DAT', skiprows = 40)

predmodels = [predmodel26, predmodel45, predmodel60, predmodel85]
labels = ['ssp2.6', 'ssp4.5', 'ssp6.0', 'ssp8.5']



#  for convenience, set up a dictionary with our reference parameters
param = {'D':0.55, 'A':210, 'B':2, 'a0':0.3, 'a2':0.078, 'ai':0.62, 'Tf':-10.}

#This EBM has already been balanced to today's levels
model1 = climlab.EBM_annual(name='EBM with interactive ice line',
                            num_lat=360,
                            **param)

# Integrate out to equilibrium.
model1.integrate_years(10)

#check for equilibrium is reached (=ASR - OLR)
print(climlab.global_mean(model1.net_radiation))

#  There is a diagnostic that tells us the current location of the ice edge:
print(model1.icelat)


def co2_to_deltaA(co2eppm):
    '''
    function translating the CO2e concentration levels in the atmosphere, to the
    to the change in OLR (delta A).
    '''
    return 3.71/np.log(2)*np.log(co2eppm/278)

colors = ['b', 'r']

climlabmodels = [climlab.process_like(model1) for i in range(len(predmodels))]
fig1, axs1 = plt.subplots(nrows = 2, ncols = 2)
yearslim = [2021,2100]


for climlabmodel, predmodel, ax1, label in zip(climlabmodels, predmodels, axs1.reshape(-1), labels):
    predmodelcut = predmodel[(predmodel[:,0]>=yearslim[0]) & (predmodel[:,0]<=yearslim[1])]
    years = predmodelcut[:,0]
    co2e_concs = predmodelcut[:,1]
    DA_array = co2_to_deltaA(co2e_concs)
    icelat = np.empty_like(DA_array)
    #icelat_cooling = np.empty_like(DA_array)
    for i, DA in enumerate(DA_array):
        climlabmodel.subprocess['LW'].A = param['A'] + DA_array[0] - DA
        climlabmodel.integrate_years(1, verbose=False)
        icelat[i] = np.max(climlabmodel.icelat)
        print(i)
        print(icelat[i])
    
    ax1.plot(years, icelat, colors[0]+'-', label = label)
    ax2 = ax1.twinx()
    ax2.plot(years, co2e_concs, colors[1]+'-', alpha = 0.5)
    ax2.set_ylim(400,1250)
    ax1.set_ylim(65,95)
    ax1.set_ylabel('ice_latitude')
    ax2.set_ylabel('CO2e levels [ppm]')
    ax1.legend()
    '''
    # First warm....
    for n in range(DA_array.size):
        model1.subprocess['LW'].A = param['A'] - DA_array[n]
        model1.integrate_years(1, verbose=False)
        icelat_warming[n] = np.max(model1.icelat)
        print(n)
    # Then cool...
    for n in reversed(range(DA_array.size)):
        model1.subprocess['LW'].A = param['A'] - DA_array[n]
        model1.integrate_years(1, verbose=False)
        icelat_cooling[n] = np.max(model1.icelat)
        print(n)
    '''
fig1.tight_layout()
fig1.show()



'''
fig = plt.figure( figsize=(10,6) )
ax = fig.add_subplot(111)
ax.plot(DA_array, icelat_warming, 'b-', label='warming' )
ax.plot(DA_array, icelat_cooling, 'r-', label='cooling' )
ax.set_ylim(65,100)
#ax.set_yticks((0,15,30,45,60,75,90))
ax.grid()
ax.set_ylabel('Ice edge latitude', fontsize=16)
ax.set_xlabel('Radiative Forcing (W m$^{-2}$)', fontsize=16)
ax.plot( [co2_factor_to_deltaA(1), co2_factor_to_deltaA(1)], [65, 100], 'k--', label='present-day' )
ax.legend(loc='upper left')
ax.set_title('Solar constant versus ice edge latitude in the EBM with albedo feedback', fontsize=16);
fig.show()

'''
