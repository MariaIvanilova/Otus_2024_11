from src.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, a: int | float):
        if not (isinstance(a, int) or isinstance(a, float)):
            raise TypeError("Square side should be int or float")
        if a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(a, a)
