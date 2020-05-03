# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:21:51 2020

@author: Pablo Morandé
"""
import numpy as np
import matplotlib.pyplot as plt
from MandelbrotSet import mandlebrot
def main():
    mymandlebrot =mandlebrot(10000)
    plt.show(mymandlebrot.printMandlebrot())
    
    
main()