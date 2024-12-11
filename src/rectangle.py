from src.figure import Figure


class Rectangle(Figure):
    """Class Rectangle"""

    def __init__(self, a: int | float, b: int | float):
        if not isinstance(a, int) or isinstance(a, float):
            raise TypeError("The size 'a' of rectangle's sides should be int of float")
        if not isinstance(b, int) or isinstance(b, float):
            raise TypeError("The size 'b' of rectangle's sides should be int of float")
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")

        self.a = a
        self.b = b

    @property
    def perimeter(self) -> int | float:
        return (self.a * 2) + (self.b * 2)

    @property
    def area(self) -> int | float:
        return self.a * self.b
