# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:54:36 2021

@author: thedi

Prepare datasets for plotting from the four prediction models
"""

import numpy as np
import climlab
from climlib import *

#Some data to be used in making the prediction models
filepaths = ['RCP3PD_MIDYR_CONC.DAT', 'RCP45_MIDYR_CONC.DAT', 'RCP6_MIDYR_CONC.DAT', 'RCP85_MIDYR_CONC.DAT']
labels = ['RCP-2.6', 'RCP-4.5', 'RCP-6.0', 'RCP-8.5']
param = {'D':0.55, 'A':210, 'B':2, 'a0':0.3, 'a2':0.078, 'ai':0.62, 'Tf':-10.}

#Year interval where the models will be evaluated
years_lims = [2021,2150]

#make list of the four models
predictions = [prediction(label, filepath=filepath, year_lims=years_lims) for label, filepath in zip(labels,filepaths)]

#initiate today model, and make it as a starting point for all other simulations
climlab_today = make_model(param)
for pred in predictions: pred.initiate_model(param, starting_climlab_model=climlab_today)

#run the models
for pred in predictions: pred.run_model()

#save the dataset models for plotting in other scripts
np.save('predicts_vanilla.npy',predictions)