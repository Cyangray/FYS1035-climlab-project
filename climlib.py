# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 17:55:56 2021

@author: thedi
"""


import numpy as np
import matplotlib.pyplot as plt
import climlab
from climlab import constants as const



def co2_to_deltaA(co2eppm):
    '''
    function translating the CO2e concentration levels in the atmosphere, to the
    to the change in OLR (delta A).
    '''
    return 3.71/np.log(2)*np.log(co2eppm/278)

def make_model(params):
    climlab_model = climlab.EBM_annual(name='EBM with interactive ice line',
                                num_lat=360,
                                **params)
    climlab_model.integrate_years(10, verbose=False)
    return climlab_model

class prediction:
    '''
    Class to make it easier to structure between the models
    '''
    def __init__(self, label, filepath=None, year_lims=None):
        if filepath:
            raw_dataset = np.loadtxt(filepath, skiprows = 40)
            if year_lims:
                 raw_dataset = raw_dataset[(raw_dataset[:,0]>=year_lims[0]) & (raw_dataset[:,0]<=year_lims[1])]
                 self.raw_dataset = raw_dataset
            else:
                 self.raw_dataset = raw_dataset
            
            self.years = self.raw_dataset[:,0]
            self.co2e_array = self.raw_dataset[:,1]
            self.DA_array = co2_to_deltaA(self.co2e_array)
            self.label = label
        
    def initiate_model(self, params, starting_climlab_model=None):
        if starting_climlab_model:
            self.climlab_model = climlab.process_like(starting_climlab_model)
        else:    
            self.climlab_model = make_model(params)
        self.params = params
        
    def run_model(self,stab_years=1, ice_lat_decrease = None, year_decrease = None, static = False):
        self.icelat = np.empty_like(self.DA_array)
        if ice_lat_decrease or year_decrease:
            
            if ice_lat_decrease:
                if np.max(self.climlab_model.icelat) >= ice_lat_decrease:
                    print('ice_lat_decrease must be bigger than initial icelat!')
            elif year_decrease:
                if year_decrease < self.years[0]:
                    print('year_decrease must be bigger than initial year!')
                
            decrease = False
            maxco2e_ind = 0
                
            for i in range(len(self.DA_array)):
                if decrease:
                    if static:
                        new_co2e = self.co2e_array[maxco2e_ind]
                    else:    
                        new_co2e = self.co2e_array[maxco2e_ind] - 4*(i - maxco2e_ind)
                    if new_co2e < self.co2e_array[0]:
                        new_co2e = self.co2e_array[0]
                    self.co2e_array[i] = new_co2e
                    self.DA_array[i] = co2_to_deltaA(self.co2e_array[i])
                DA = self.DA_array[i]
                self.climlab_model.subprocess['LW'].A = self.params['A'] + self.DA_array[0] - DA
                self.climlab_model.integrate_years(stab_years, verbose=False)
                self.icelat[i] = np.max(self.climlab_model.icelat)
                try:
                    if self.icelat[i] >= ice_lat_decrease:
                        decrease = True
                        maxco2e_ind = i
                except:
                    pass
                try:
                    if self.years[i] >= year_decrease:
                        decrease = True
                        maxco2e_ind = i
                except:
                    pass
                print(i)
        else:
            for i, DA in enumerate(self.DA_array):
                self.climlab_model.subprocess['LW'].A = self.params['A'] + self.DA_array[0] - DA
                self.climlab_model.integrate_years(stab_years, verbose=False)
                self.icelat[i] = np.max(self.climlab_model.icelat)
                print(i)
            
            
            
            
            
            
            
            
            
            
            
        