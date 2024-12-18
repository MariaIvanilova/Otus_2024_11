from src.circle import Circle
from src.square import Square
from src.triangle import Triangle
from src.rectangle import Rectangle
import pytest

test_area_int = [2, 3, 4, 2.9]
test_area_float = [2.2, 3.3, 4.4, 3.51]

test_perimeter_int = [2, 3, 4, 9]
test_perimeter_float = [2.1, 3.3, 4.4, 9.8]

c = Circle(5.5)
r = Rectangle(5, 4.4)
s = Square(5.5)
test_add_area_1 = [2, 3, 4, c, 97.94]
test_add_area_2 = [2, 3, 4, r, 24.9]
test_add_area_3 = [2, 3, 4, s, 33.15]


@pytest.mark.triangle
@pytest.mark.parametrize(
    "numbers",
    [test_area_int, test_area_float],
    ids=["Test_integer", "Test_float"],
)
def test_triangle_area_positive(start_end, numbers):
    a, b, c, area = numbers
    print(f"Reference data - a_size: {a}, b_size: {b}, с_size: {c}, area: {area}")
    t = Triangle(a, b, c)
    assert round(t.area, 2) == area


@pytest.mark.triangle
@pytest.mark.parametrize(
    "numbers",
    [test_perimeter_int, test_perimeter_float],
    ids=["Test_integer", "Test_float"],
)
def test_triangle_perimeter_positive(start_end, numbers):
    a, b, c, perimeter = numbers
    print(
        f"Reference data - a_size: {a}, b_size: {b}, с_size: {c}, perimeter: {perimeter}"
    )
    t = Triangle(a, b, c)
    assert round(t.perimeter, 2) == perimeter


@pytest.mark.triangle
@pytest.mark.parametrize(
    "add_area_test",
    [test_add_area_1, test_add_area_2, test_add_area_3],
    ids=[
        "Area's triangle + Area's circle",
        "Area's triangle + Area's rectangle",
        "Area's rectangle + Area's square",
    ],
)
def test_rectangle_add_area_positive(start_end, add_area_test):
    a, b, c, new_figure, result = add_area_test
    t = Triangle(a, b, c)
    print(
        f"triangle's area {t.area}, new_figure.area {new_figure.area}, reference result: {result}"
    )
    assert round(t.add_area(new_figure), 2) == result


@pytest.mark.triangle
def test_triangle_is_not_triangle_negative(start_end):
    a, b, c = 1, 2, 3
    print(f"a_size: {a}, b_size: {b}, c_size: {c} is not a triangle.")
    with pytest.raises(ValueError):
        Triangle(a, b, c)
