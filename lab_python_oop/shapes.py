from abc import ABC, abstractmethod
from .color import Color
import math


class Shape(ABC):
    def __init__(self, color: Color):
        self._color = color

    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def get_data(self) -> str:
        pass

    def __str__(self) -> str:
        return '{} {} ({})'.format(self._color, self.name, self.get_data())


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        self._width = width
        self._height = height
        Shape.__init__(self, color)

    def area(self) -> float:
        return self._width * self._height

    @property
    def name(self) -> str:
        return 'Прямоугольник'

    def get_data(self) -> str:
        return '{}x{}={}'.format(self._width, self._height, self.area())


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        Rectangle.__init__(self, side, side, color)

    @property
    def name(self) -> str:
        return 'Квадрат'


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        self._radius = radius
        self._color = color
        Shape.__init__(self, color)

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @property
    def name(self) -> str:
        return 'Круг'

    def get_data(self) -> str:
        return f'pi*{self._radius}^2={self.area()}'
