from src.circle import Circle
from src.rectangle import Rectangle
import pytest

from src.square import Square
from src.triangle import Triangle

test_area_int = [3, 5, 15]
test_area_float = [3.5, 5.5, 19.25]

test_perimetr_int = [3, 5, 16]
test_perimetr_float = [3.5, 5.5, 18]

c = Circle(5.5)
s = Square(5.5)
t = Triangle(2.2, 3.3, 4.4)
test_add_area_1 = [5, 10, c, 145.03]
test_add_area_2 = [5.3, 10.5, s, 85.9]
test_add_area_3 = [5.5, 5.5, t, 33.76]


test_size_negative = [-1, 5]
test_size_zero = [0, 5]

test_size_type_1 = ["test", 5]
test_size_type_2 = [5, [1, 2, 3]]


@pytest.mark.rectangle
@pytest.mark.parametrize(
    "numbers", [test_area_int, test_area_float], ids=["Test_integer", "Test_float"]
)
def test_rectangle_area_positive(start_end, numbers):
    a, b, area = numbers
    print(f"Reference data - a_size: {a}, b_size: {b}, area: {area}")
    r = Rectangle(a, b)
    assert r.area == area


@pytest.mark.rectangle
@pytest.mark.parametrize(
    "numbers",
    [test_perimetr_int, test_perimetr_float],
    ids=["Test_integer", "Test_float"],
)
def test_rectangle_perimetr_positive(start_end, numbers):
    a, b, perimetr = numbers
    print(f"Reference data - a_size: {a}, b_size: {b}, perimeter: {perimetr}")
    r = Rectangle(a, b)
    assert r.perimeter == perimetr


@pytest.mark.rectangle
@pytest.mark.parametrize(
    "add_area_test",
    [test_add_area_1, test_add_area_2, test_add_area_3],
    ids=[
        "Area's rectangle + Area's circle",
        "Area's rectangle + Area's square",
        "Area's rectangle + Area's triangle",
    ],
)
def test_rectangle_add_area_positive(start_end, add_area_test):
    a, b, new_figure, result = add_area_test
    r = Rectangle(a, b)
    print(
        f"rectangle's area {r.area}, new_figure.area {new_figure.area}, reference result: {result}"
    )
    assert round(r.add_area(new_figure), 2) == result


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("a", "b"),
    [test_size_negative, test_size_zero],
    ids=["Negative value of size", "Zero value of size"],
)
def test_rectangle_sizes_negative(start_end, a, b):
    print(f"Incorrect sizes value - a_size: {a}, b_size: {b}")
    with pytest.raises(ValueError):
        Rectangle(a, b)


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("a", "b"),
    [test_size_type_1, test_size_type_2],
    ids=["Incorrect format str", "incorrect format list"],
)
def test_rectangle_types_negative(start_end, a, b):
    print(f"Incorrect type - a_size: {a} {type(a)}, b_size: {b} {type(b)}")
    with pytest.raises(TypeError):
        Rectangle(a, b)
