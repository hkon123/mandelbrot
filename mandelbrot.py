import math
import Mathplotlib.pyplot as plt
import numpy as np
import complex
import decimal

def mandel(c):
    z = complex(0,0)
    zn = complex(0,0)
    count = 0
    while zn.length**2 <=4 and count <255:
         zn = z*z+c
         z = zn
         count = count + 1
    if count < 255:
        return count
    else:
        return 0

class mandelbrot(object):

    def __init__(self,step):
        self.x = np.arange(-2.025,0.6,step)
        self.y = np.arange(-1.125,1.125,step)
        self.comped = np.zeros((len(self.x),len(self.y)))

    def compute(self):
        for i in range(0,len(self.x)):
            for j in range(0,len(self.y)):
                self.comped[j,i]=mandel(complex(self.x[i],self.y[j]))

    def mPrint(self):
        left = self.x.min()
        right = len(self.x)
        bottom = len(self.y)
        top = self.y.min()
        plt.imshow(self.comped, extent=(left,right,bottom, top), interpolation = 'none', cmap='hot')
        plt.colorbar()
        plt.show()

def main():
    sett = mandelbrot(0.1)
    sett.compute()
    sett.mPrint()
