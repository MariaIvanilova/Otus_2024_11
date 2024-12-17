from src.circle import Circle
from src.square import Square
from src.triangle import Triangle
from src.rectangle import Rectangle
import pytest


test_area_int = [3, 9]
test_area_float = [3.3, 10.89]

test_perimetr_int = [3, 12]
test_perimetr_float = [3.3, 13.2]

c = Circle(5.5)
r = Rectangle(5.5, 10)
t = Triangle(2.2, 3.3, 4.4)
test_add_area_1 = [5, c, 120.03]
test_add_area_2 = [5.3, r, 83.09]
test_add_area_3 = [5.5, t, 33.76]

test_size_type_1 = "test"
test_size_type_2 = [1, 2, 3]


@pytest.mark.square
@pytest.mark.parametrize(
    "numbers", [test_area_int, test_area_float], ids=["Test_integer", "Test_float"]
)
def test_square_area_positive(start_end, numbers):
    a, area = numbers
    print(f"Reference data - a_size:{a} area:{area}")
    s = Square(a)
    assert round(s.area, 2) == area


@pytest.mark.square
@pytest.mark.parametrize(
    "numbers",
    [test_perimetr_int, test_perimetr_float],
    ids=["Test_integer", "Test_float"],
)
def test_square_perimetr_positive(start_end, numbers):
    a, perimeter = numbers
    print(f"Reference data - a_size:{a} area:{perimeter}")
    s = Square(a)
    assert s.perimeter == perimeter


@pytest.mark.square
@pytest.mark.parametrize(
    "add_area_test",
    [test_add_area_1, test_add_area_2, test_add_area_3],
    ids=[
        "Area's square + Area's circle",
        "Area's square + Area's rectangle",
        "Area's square + Area's triangle",
    ],
)
def test_rectangle_add_area_positive(start_end, add_area_test):
    a, new_figure, result = add_area_test
    s = Square(a)
    print(
        f"square's area {s.area}, new_figure.area {new_figure.area}, reference result: {result}"
    )
    assert round(s.add_area(new_figure), 2) == result


@pytest.mark.square
@pytest.mark.parametrize(
    "a", [-1, 0], ids=["Negative value of size", "Zero value of size"]
)
def test_rectangle_sizes_negative(start_end, a):
    print(f"Incorrect value a_size: {a}")
    with pytest.raises(ValueError):
        Square(a)


@pytest.mark.square
@pytest.mark.parametrize(
    "a",
    [test_size_type_1, test_size_type_2],
    ids=["Incorrect format str", "incorrect format list"],
)
def test_rectangle_types_negative(start_end, a):
    print(f"Incorrect type {type(a)} of a_size: {a}")
    with pytest.raises(TypeError):
        Square(a)
