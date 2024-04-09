from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: float or int) -> None:
        self.__radius = radius

    def calculate_area(self) -> int or float:
        return pi * self.__radius ** 2

    def calculate_perimeter(self) -> int or float:
        return 2 * (pi * self.__radius)


class Rectangle(Shape):
    def __init__(self, height: int or float, width: int or float) -> None:
        self.__width = width
        self.__height = height

    def calculate_area(self) -> int or float:
        return self.__height * self.__width

    def calculate_perimeter(self) -> int or float:
        return 2 * (self.__height + self.__width)
