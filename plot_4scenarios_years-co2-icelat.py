# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 18:48:18 2021

@author: thedi
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from climlib import *


#Do you want to plot the vanilla results, or the ones showing the vippepunkt?

#name = 'predicts.npy'

year_list = [2040, 2042, 2044, 2046, 2048, 2050, 2052, 2054]
for year_thresh in year_list:
    name = 'predicts_vippepunkt_%s.npy'%year_thresh
    
    
    #load prediction models
    predictions = np.load(name, allow_pickle = True)
    
    '''
    #Plot 2x2 grid
    colors = ['b', 'r']
    fig1, axs1 = plt.subplots(nrows = 2, ncols = 2, figsize=(10,6))
    for predmodel, ax1 in zip(predictions, axs1.reshape(-1)):
        ax1.plot(predmodel.years, predmodel.icelat, colors[0]+'-', label = predmodel.label)
        ax2 = ax1.twinx()
        ax2.plot(predmodel.years, predmodel.co2e_array, colors[1]+'-', alpha = 0.5)
        ax2.set_ylim(400,1250)
        ax1.set_ylim(65,95)
        ax1.set_ylabel('iceline latitude')
        ax2.set_ylabel('CO2e levels [ppm]')
        ax1.legend()
    fig1.tight_layout()
    fig1.show()
    '''
    
    #plot icelats and co2e levels
    cmap = matplotlib.cm.get_cmap('rainbow')
    fig2, axs2 = plt.subplots(nrows = 1, ncols = 2, figsize=(10,6))
    for i,predmodel in enumerate(predictions):
        axs2[0].plot(predmodel.years, predmodel.icelat, color = cmap(i/4), linestyle = '-', label = predmodel.label)
        axs2[1].plot(predmodel.years, predmodel.co2e_array, color = cmap(i/4), linestyle = '-', label = predmodel.label)
    axs2[0].set_title('Cut year %s'%year_thresh)
    axs2[0].set_ylim(70,91)
    axs2[1].set_ylim(370,610)
    axs2[0].set_ylabel('iceline latitude')
    axs2[1].set_ylabel('CO2e levels [ppm]')
    axs2[0].legend()
    axs2[1].legend()
    axs2[0].grid()
    axs2[1].grid()
    #fig2.tight_layout()
    fig2.show()