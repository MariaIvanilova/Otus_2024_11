from src.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, a: int | float):
        if a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(a, a)
