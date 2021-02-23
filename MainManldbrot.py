# -*- coding: utf-8 -*-
"""
Main file for Mandelbrot set
@author: Pablo Morandé
"""
from MandelbrotSet import Mandelbrot
import numpy as np
def main ():
    mySet = Mandelbrot(500, 500)
    mySet.printMandlebrot()

main()


