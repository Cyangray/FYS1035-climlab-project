# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:16:10 2021

@author: thedi
"""
import numpy as np
import matplotlib.pyplot as plt

wikidata = np.loadtxt('wikidata.txt')

model26 = np.loadtxt('RCP3PD_MIDYR_CONC.DAT', skiprows = 40)
model45 = np.loadtxt('RCP45_MIDYR_CONC.DAT', skiprows = 40)
model60 = np.loadtxt('RCP6_MIDYR_CONC.DAT', skiprows = 40)
model85 = np.loadtxt('RCP85_MIDYR_CONC.DAT', skiprows = 40)

models = [model26, model45, model60, model85]
labels = ['ssp2.6', 'ssp4.5', 'ssp6.0', 'ssp8.5']

def co2_to_deltaA(co2eppm):
    return 3.71/np.log(2)*np.log(co2eppm/278)

'''
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time')
ax1.set_ylabel('RF', color=color)
plt.plot(wikidata[:,0], wikidata[:,7], color = color, label='RF')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('co2e', color=color)  # we already handled the x-label with ax1
plt.plot(wikidata[:,0], wikidata[:,8], color = color, label='RF')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()




co2lvls = np.linspace(300,1000, 500)

fig, ax2 = plt.subplots()
ax2.plot(co2lvls, co2_to_deltaA(co2lvls), label = 'dataset')
ax2.plot(wikidata[:,8], wikidata[:,7], label = 'wiki')
plt.legend()
plt.grid()
fig.show()



fig, ax3 = plt.subplots()
for model, label in zip(models,labels):
    ax3.plot(model[:,0],co2_to_deltaA(model[:,1]), label = label)
plt.legend()
plt.grid()
fig.show()
'''

