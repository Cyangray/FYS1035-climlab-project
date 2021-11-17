# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:54:36 2021

@author: thedi

A modification of make_datasets, where the co2 emission decrease with 4ppm per 
year after the icecaps melt. Let's see how long does it take for the ice to come back
"""

import numpy as np
import climlab
from climlib import *

#Some data to be used in making the prediction models
filepaths = ['data/RCP3PD_MIDYR_CONC.DAT', 'data/RCP45_MIDYR_CONC.DAT', 'data/RCP6_MIDYR_CONC.DAT', 'data/RCP85_MIDYR_CONC.DAT']
labels = ['RCP-2.6', 'RCP-4.5', 'RCP-6.0', 'RCP-8.5']
param = {'D':0.55, 'A':210, 'B':2, 'a0':0.3, 'a2':0.078, 'ai':0.62, 'Tf':-10.}

#Year interval where the models will be evaluated
years_lims = [2021, 2150]

#initiate today model, and make it as a starting point for all other simulations
climlab_today = make_model(param)

#year_list = [2036, 2038, 2040, 2042, 2043, 2044, 2046, 2048, 2050, 2052, 2054]
year_list = [2036, 2043, 2044, 2050]

#Make datasets when emissions stop in year year_thresh
for year_thresh in year_list:
    
    #make list of the four models
    predictions = [prediction(label, filepath=filepath, year_lims=years_lims) for label, filepath in zip(labels,filepaths)]

    #initiate models
    for pred in predictions: pred.initiate_model(param, starting_climlab_model = climlab_today)
    
    #run the models
    for pred in predictions: pred.run_model(year_decrease = year_thresh, static = False) #ice_lat_decrease = 80)
    
    #save the dataset models for plotting in other scripts
    np.save('predicts_vippepunkt_%s.npy'%year_thresh,predictions)

#Make datasets when emissions reverse in year year_thresh
for year_thresh in year_list:
    
    #make list of the four models
    predictions = [prediction(label, filepath=filepath, year_lims=years_lims) for label, filepath in zip(labels,filepaths)]

    #initiate models
    for pred in predictions: pred.initiate_model(param, starting_climlab_model = climlab_today)
    
    #run the models
    for pred in predictions: pred.run_model(year_decrease = year_thresh, static = True) #ice_lat_decrease = 80)
    
    #save the dataset models for plotting in other scripts
    np.save('predicts_vippepunkt_s_%s.npy'%year_thresh,predictions)