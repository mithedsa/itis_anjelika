import math
from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    def __init__(self, lenght: int, heigth = int):
        '''
        Constructor for abstract GeometricFigure class. Inits class properties
        :param lenght: lenght or side a of gigure
        :param heigth: height or side b of gigure
        '''
        self.length = lenght
        self.heigth = heigth

    @abstractmethod
    def square(self):
        return self.length * self.heigth

    @abstractmethod
    def perimetr(self):
        return 2 * (self.length + self.heigth)


class Circle(GeometricFigure):
        def square(self, diametr):
            self.square = math.pi * (diametr / 2)**2
            print('площадь круга', square())

class Quadrangle(GeometricFigure):
    def __init__(self, a, b):
        self.length = a
        self.heigth = b

class Rectangle(Quadrangle):
    def square(self, a, b):
            return a * b

class Trapezoid(Quadrangle):
    def square(self, a, b, h):
        return (a + b) / 2 * h

class Parallelogram(Quadrangle):
    def square(self, a, h):
        return a * h
