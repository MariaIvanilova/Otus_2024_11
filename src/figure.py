from abc import ABC, abstractmethod


class Figure(ABC):
    """Base class for geometric figure"""

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure: object) -> int | float:
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.area + other_figure.area
