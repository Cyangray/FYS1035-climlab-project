# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 21:29:18 2021

@author: thedi
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from climlib import *


#Do you want to plot the vanilla results, or the ones showing the vippepunkt?

#name = 'predicts.npy'

year_list = [2036, 2043, 2050]

cmap = matplotlib.cm.get_cmap('magma')
alpha = 0.7
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize=(15,7))
plt.suptitle('Hva skjer hvis vi bestemmer oss for å stoppe utslipp helt på et visst år?')
axs.flatten()
for i, year_thresh in enumerate(reversed(year_list)):
    name = 'predicts_vippepunkt_s_%s.npy'%year_thresh
    
    #load prediction models
    predictions = np.load(name, allow_pickle = True)
    
    #plot icelats and co2e levels
    predmodel = predictions[3]
    axs[0].plot(predmodel.years, predmodel.co2e_array, color = cmap(i/len(year_list)), linestyle = '-', label = 'Stopp i %s'%year_thresh, alpha = alpha)
    axs[1].plot(predmodel.co2e_array, predmodel.icelat, color = cmap(i/len(year_list)), linestyle = '-', label = 'Stopp i %s'%year_thresh, alpha = alpha)
    axs[2].plot(predmodel.years, predmodel.icelat, color = cmap(i/len(year_list)), linestyle = '-', label = 'Stopp i %s'%year_thresh, alpha = alpha)
    if year_thresh == 2044:
        axs[0].plot(predmodel.years, predmodel.co2e_array, color = cmap(i/len(year_list)), linestyle = '--', label = 'Stopp i %s'%year_thresh, alpha = alpha)
        axs[1].plot(predmodel.co2e_array, predmodel.icelat, color = cmap(i/len(year_list)), linestyle = '--', label = 'Stopp i %s'%year_thresh, alpha = alpha)
        axs[2].plot(predmodel.years, predmodel.icelat, color = cmap(i/len(year_list)), linestyle = '--', label = 'Stopp i %s'%year_thresh, alpha = alpha)
    
    max_co2_i = np.argmax(predmodel.co2e_array)
    axs[1].plot(predmodel.co2e_array[max_co2_i], predmodel.icelat[max_co2_i], 'ko')
    if year_thresh > 2044:
        axs[1].annotate(text = int(year_thresh), xy=(predmodel.co2e_array[max_co2_i], predmodel.icelat[max_co2_i]), xytext=(predmodel.co2e_array[max_co2_i]+1, predmodel.icelat[max_co2_i]-0.5*((year_thresh%4) - 0.5)))
    else:
        axs[1].annotate(text = int(year_thresh), xy=(predmodel.co2e_array[max_co2_i], predmodel.icelat[max_co2_i]), xytext=(predmodel.co2e_array[max_co2_i]+7, predmodel.icelat[max_co2_i]-0.2))
    axs[0].plot(predmodel.years[max_co2_i], predmodel.co2e_array[max_co2_i], 'ko')
    axs[0].annotate(text = int(year_thresh), xy=(predmodel.years[max_co2_i], predmodel.co2e_array[max_co2_i]), xytext=(predmodel.years[max_co2_i]+2, predmodel.co2e_array[max_co2_i]-7))
    axs[2].plot(predmodel.years[max_co2_i], predmodel.icelat[max_co2_i], 'ko')
    axs[2].annotate(text = int(year_thresh), xy=(predmodel.years[max_co2_i], predmodel.icelat[max_co2_i]), xytext=(predmodel.years[max_co2_i]+4, predmodel.icelat[max_co2_i]-0.2))
    
#axs[1].set_title('Cut year %s'%year_thresh)
axs[0].plot(predmodel.years[0], predmodel.co2e_array[0], 'ko')
axs[1].plot(predmodel.co2e_array[0], predmodel.icelat[0], 'ko')
axs[2].plot(predmodel.years[0], predmodel.icelat[0], 'ko')

axs[0].annotate(text = 'Dagens nivå', xy=(predmodel.years[0], predmodel.co2e_array[0]), xytext=(predmodel.years[0]+4, predmodel.co2e_array[0]-3))
axs[1].annotate(text = 'Dagens nivå', xy=(predmodel.co2e_array[0], predmodel.icelat[0]), xytext=(predmodel.co2e_array[0]+7, predmodel.icelat[0]-0.2))
axs[2].annotate(text = 'Dagens nivå', xy=(predmodel.years[0], predmodel.icelat[0]), xytext=(predmodel.years[0]+4, predmodel.icelat[0]-0.2))
axs[1].set_ylim(70,91)
#axs[0].set_ylim(420,630)
axs[0].set_xlabel('År')
axs[0].set_ylabel('CO2e-nivåer [ppm]')
axs[1].set_xlabel('CO2e-nivåer [ppm]')
axs[1].set_ylabel('Islinje (breddegrad)')
axs[2].set_xlabel('År')
axs[2].set_ylabel('Islinje (breddegrad)')
axs[0].legend()
axs[1].legend()
axs[2].legend()
axs[0].grid()
axs[1].grid()
axs[2].grid()
#fig2.tight_layout()
fig.show()