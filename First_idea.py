# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 13:25:47 2021

@author: thedi
"""
import numpy as np
import matplotlib.pyplot as plt
import climlab
from climlab import constants as const

model26 = np.loadtxt('RCP3PD_MIDYR_CONC.DAT', skiprows = 40)
model45 = np.loadtxt('RCP45_MIDYR_CONC.DAT', skiprows = 40)
model60 = np.loadtxt('RCP6_MIDYR_CONC.DAT', skiprows = 40)
model85 = np.loadtxt('RCP85_MIDYR_CONC.DAT', skiprows = 40)

models = [model26, model45, model60, model85]
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



yearslim = [2021,2100]
predmodel = model26


predmodelcut = predmodel[(predmodel[:,0]>=yearslim[0]) & (predmodel[:,0]<=yearslim[1])]

co2e_conc_array = predmodelcut[:,1]
DA_array = co2_to_deltaA(co2e_conc_array)
#DAfactor_array = np.linspace(3.14, 2., 30)
#model2.integrate_years(5)
icelat_cooling = np.empty_like(DA_array)
icelat_warming = np.empty_like(DA_array)
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






fig = plt.figure( figsize=(10,6) )
ax = fig.add_subplot(111)
ax.plot(co2e_conc_array, icelat_warming, 'r-', label='warming' )
ax.plot(co2e_conc_array, icelat_cooling, 'b-', label='cooling' )
ax.set_ylim(65,100)
#ax.set_yticks((0,15,30,45,60,75,90))
ax.grid()
ax.set_ylabel('Ice edge latitude', fontsize=16)
ax.set_xlabel('Radiative Forcing (W m$^{-2}$)', fontsize=16)
#ax.plot( [co2_factor_to_deltaA(1), co2_factor_to_deltaA(1)], [65, 100], 'k--', label='present-day' )
ax.legend(loc='upper left')
ax.set_title('Solar constant versus ice edge latitude in the EBM with albedo feedback', fontsize=16);
fig.show()






