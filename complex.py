import math


class complex(object):

    def __init__(self,real,comp):
        self.real = real
        self.comp = comp

    def __add__(self,other):
        a = complex(0,0)
        a.real = self.real + other.real
        a.comp = self.comp + other.comp
        return a

    def __sub__(self,other):
        a = complex(0,0)
        a.real = self.real - other.real
        a.comp = self.comp - other.comp
        return a

    def __mul__(self,other):
        a = complex(0,0)
        a.real = self.real*other.real - self.comp*other.comp
        a.comp = self.real*other.comp + self.comp*other.real
        return a

    def length(self):
        s = math.sqrt(self.real**2 + self.comp**2)
        return s
