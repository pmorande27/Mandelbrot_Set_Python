# -*- coding: utf-8 -*-
"""
File for creating the class Mandelbrot
@author: Pablo Morandé
"""
import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot(object):
    def __init__(self,x_dimension,y_dimension):
        """
        Constructor of the Class to build the mandelbrot, 
        it will take as parameters the number of points to be analysed
        """
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension

    def isMandelbrot(self, c):
        iterations = 0
        z = 0
        magnitude = 0
        while magnitude <= 2 and iterations < 255:
            nextZ = z*z + c
            magnitude = abs(nextZ)
            z = nextZ
            iterations += 1
        return iterations

    def printMandlebrot(self, ):
        """
        Method used to construct and display the Mandelbrot.
        """
        "Create Space of imaginary and real terms"
        lineSpaceX = np.linspace(-2.025, 0.6, self.x_dimension)
        lineSpaceY = np.linspace(-1.125, 1.125, self.y_dimension)
        XX, YY = np.meshgrid(lineSpaceX,lineSpaceY )
        "Initialize result array"
        resultArray = np.zeros((self.x_dimension, self.y_dimension))
        "Calculate Mandelbrot set"
        for i in range( self.x_dimension):
            for j in range( self.y_dimension):
                resultArray[i][j] = self.isMandelbrot(complex(XX[i][j],YY[i][j]))
        "Plot"
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.axis('on')
        plt.imshow(resultArray,extent=[-2.025, 0.6,-1.125, 1.125])
        plt.colorbar()
        plt.title('MandelBrot Set')
        plt.show()
