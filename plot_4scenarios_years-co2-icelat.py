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
cmap = matplotlib.cm.get_cmap('magma')
fig2, axs2 = plt.subplots(nrows = 1, ncols = 2, figsize=(10,6))
plt.suptitle('Co2e-nivåer og islinja frem til 2150 for fire utslippsmodeller')
for i,predmodel in enumerate(predictions):
    axs2[1].plot(predmodel.years, predmodel.icelat, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = 0.7)
    axs2[0].plot(predmodel.years, predmodel.co2e_array, color = cmap(i/4), linestyle = '-', label = predmodel.label, alpha = 0.7)
axs2[1].set_ylim(70,91)
axs2[1].set_ylabel('iceline latitude')
axs2[0].set_ylabel('CO2e levels [ppm]')
axs2[1].legend()
axs2[0].legend()
axs2[1].grid()
axs2[0].grid()
#fig2.tight_layout()
fig2.show()