import math
import matplotlib.pyplot as plt
import numpy as np
import decimal


class complex1(object):

    def __init__(self,real,comp):
        self.real = real
        self.comp = comp

    def __add__(self,other):
        a = complex1(0,0)
        a.real = self.real + other.real
        a.comp = self.comp + other.comp
        return a

    def __sub__(self,other):
        a = complex1(0,0)
        a.real = self.real - other.real
        a.comp = self.comp - other.comp
        return a

    def __mul__(self,other):
        a = complex1(0,0)
        a.real = self.real*other.real - self.comp*other.comp
        a.comp = self.real*other.comp + self.comp*other.real
        return a

    def length(self):
        s = math.sqrt(self.real**2 + self.comp**2)
        return float(s)


def mandel(c):
    z = complex1(0,0)
    zn = complex1(0,0)
    count = 0
    while zn.length()**2 <=4 and count <255:
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
        self.comped = np.zeros((len(self.y),len(self.x)))

    def compute(self):
        for i in range(0,len(self.x)):
            for j in range(0,len(self.y)):
                self.comped[j,i]=mandel(complex1(self.x[i],self.y[j]))

    def mPrint(self):
        left = self.x[0]
        right = self.x[-1]
        bottom = self.y[-1]
        top = self.y[0]
        plt.imshow(self.comped, extent=(left,right,bottom, top), cmap='hot')
        plt.colorbar()
        plt.title("mandelbrot set for c{-2.025-1.125i-->0.6+1.125i}")
        plt.xlabel("real part")
        plt.ylabel("complex part")
        plt.show()

def main():
    while True:
        try:
            step = float(raw_input("how big a step between the points "))
            break
        except ValueError:
            print("use a small number, jeez")
    
    sett = mandelbrot(step)
    sett.compute()
    sett.mPrint()

main()
