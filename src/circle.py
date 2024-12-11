from src.figure import Figure
import math


class Circle(Figure):
    """Class Circle"""

    def __init__(self, r: int | float):
        self.r = r

    def perimeter(self) -> int | float:
        return 2 * math.pi * self.r

    @property
    def area(self) -> int | float:
        return math.pi * (pow(self.r, 2))
