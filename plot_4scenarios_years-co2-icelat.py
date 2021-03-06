# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 18:48:18 2021

@author: thedi
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#load prediction models
name = 'predicts_vanilla.npy'
predictions = np.load(name, allow_pickle = True)

#plot icelats and co2e levels
cmap = matplotlib.cm.get_cmap('Accent')
fig2, axs = plt.subplots(nrows = 1, ncols = 3, figsize=(15,7))
alpha = 1
plt.suptitle('Co2e-nivåer og iskanten frem til 2150 for fire utslippsmodeller')
for i,predmodel in enumerate(predictions):
    axs[0].plot(predmodel.years, predmodel.co2e_array, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = alpha)
    axs[1].plot(predmodel.co2e_array, predmodel.icelat, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = alpha)
    axs[2].plot(predmodel.years, predmodel.icelat, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = alpha)
    axs[0].scatter(predmodel.years[-1], predmodel.co2e_array[-1], color = cmap(i/4), linestyle = 'dotted')
    axs[1].scatter(predmodel.co2e_array[-1], predmodel.icelat[-1], color = cmap(i/4), linestyle = 'dotted')
    axs[2].scatter(predmodel.years[-1], predmodel.icelat[-1], color = cmap(i/4), linestyle = 'dotted')

axs[0].plot(predmodel.years[0], predmodel.co2e_array[0], 'ko')
axs[1].plot(predmodel.co2e_array[0], predmodel.icelat[0], 'ko')
axs[2].plot(predmodel.years[0], predmodel.icelat[0], 'ko')
axs[0].annotate(text = 'Dagens nivå', xy=(predmodel.years[0], predmodel.co2e_array[0]), xytext=(predmodel.years[0]+4, predmodel.co2e_array[0]-40))
axs[1].annotate(text = 'Dagens nivå', xy=(predmodel.co2e_array[0], predmodel.icelat[0]), xytext=(predmodel.co2e_array[0]+50, predmodel.icelat[0]-0.2))
axs[2].annotate(text = 'Dagens nivå', xy=(predmodel.years[0], predmodel.icelat[0]), xytext=(predmodel.years[0]+4, predmodel.icelat[0]-0.2))



axs[1].set_ylim(70,91)
#axs[0].set_ylim(420,630)
axs[0].set_xlabel('År')
axs[0].set_ylabel('CO2e-nivåer [ppm]')
axs[1].set_xlabel('CO2e-nivåer [ppm]')
axs[1].set_ylabel('Iskant [breddegrad]')
axs[2].set_xlabel('År')
axs[2].set_ylabel('Iskant [breddegrad]')
axs[0].legend(loc = 'right')
axs[1].legend(loc = 'right')
axs[2].legend(loc = 'right')
axs[0].grid()
axs[1].grid()
axs[2].grid()

fig2.tight_layout()
fig2.show()


fig1, axs1 = plt.subplots()
for i,predmodel in enumerate(predictions):
    dT = [predmodel.mean_temp[i] - predmodel.mean_temp[0] + 1 for i in range(len(predmodel.mean_temp))] 
    axs1.plot(predmodel.years, dT, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = 1)

plt.title('Global gjennomsnittlig temperaturendring i forhold til 1850-1900')
axs1.plot([2015,2165], [1.5, 1.5], 'r--', label = '1,5 grader')
axs1.set_xlim(2015,2100)
axs1.set_ylim(-0.5,5.5)
axs1.set_xlabel('År')
axs1.set_ylabel('Global gjennomsnittlig temperaturendring [°C]')
axs1.legend()
axs1.grid()
fig1.show()