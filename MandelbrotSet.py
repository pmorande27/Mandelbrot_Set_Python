# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:52:38 2020

@author: Pablo Morandé
"""
import numpy as np
import matplotlib.pyplot as plt
class mandlebrot(object):
    def __init__(self, resolution):
        self.resolution = resolution
    def isMandlebrot(self,realN, complexN):
        z0 = complex(0,0) 
        C = complex (realN,complexN)
        result = 0
        for i in range(255):
            if (np.abs(z0)<2):
                z0 =z0*z0 + C
            else:
                result = i
                break
        return (result)
    def printMandlebrot(self,):
        lineSpaceX = np.linspace(-2.025,0.6,self.resolution)
        lineSpaceY = np.linspace(-1.125,1.125,self.resolution)
        resultArray = np.zeros((self.resolution,self.resolution))
        for i in range(self.resolution):
            for j in range(self.resolution):
                resultArray[i][j] = self.isMandlebrot(lineSpaceX[i],lineSpaceY[j])
        return (plt.imshow(resultArray.T,extent = [-2.025,0.6,-1.125,1.125]))
       
            
                        