from src.figure import Figure
import math


class Circle(Figure):
    """Class Circle"""

    def __init__(self, r: int | float):
        if not (isinstance(r, int) or isinstance(r, float)):
            raise TypeError("Radius should be int or float")
        if r <= 0:
            raise ValueError("Radius can't be less than 0")
        self.r = r

    @property
    def perimeter(self) -> int | float:
        return 2 * math.pi * self.r

    @property
    def area(self) -> int | float:
        return math.pi * (pow(self.r, 2))
