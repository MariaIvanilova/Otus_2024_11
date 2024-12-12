from src.figure import Figure
import math


class Triangle(Figure):
    """Class Triangle"""

    def __init__(self, a: int | float, b: int | float, c: int | float):
        if (a + b <= c) or (b + c <= a) or (c + a <= b):
            raise ValueError("It is not a triangle")
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self) -> int | float:
        return self.a + self.b + self.c

    @property
    def area(self) -> int | float:
        _semi_perimeter = self.perimeter / 2
        return math.sqrt(
            _semi_perimeter
            * (_semi_perimeter - self.a)
            * (_semi_perimeter - self.b)
            * (_semi_perimeter - self.c)
        )
