import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

test_area_int = [5, 78.54]
test_area_float = [5.5, 95.03]

test_perimeter_int = [5, 31.42]
test_perimeter_float = [5.5, 34.56]

r = Rectangle(2, 3)
s = Square(5)
t = Triangle(2, 3, 4)
test_add_area_1 = [5, r, 84.54]
test_add_area_2 = [5, s, 103.54]
test_add_area_3 = [5, t, 81.44]

test_radius_type_1 = "test"
test_radius_type_2 = [1, 2, 3]


@pytest.mark.circle
@pytest.mark.parametrize(
    "circle_test", [test_area_int, test_area_float], ids=["Test_integer", "Test_float"]
)
def test_circle_area_positive(start_end, circle_test):
    radius, area = circle_test
    print(f"Reference data - radius:{radius} area:{area}")
    c = Circle(radius)
    assert round(c.area, 2) == area


@pytest.mark.circle
@pytest.mark.parametrize(
    "circle_test",
    [test_perimeter_int, test_perimeter_float],
    ids=["Test_integer", "Test_float"],
)
def test_circle_perimeter_positive(start_end, circle_test):
    radius, perimeter = circle_test
    print(f"Reference data - radius: {radius} perimeter: {perimeter}")
    c = Circle(radius)
    assert round(c.perimeter, 2) == perimeter


@pytest.mark.circle
@pytest.mark.parametrize(
    "add_area_test",
    [test_add_area_1, test_add_area_2, test_add_area_3],
    ids=[
        "Area's circle + Area's rectangle",
        "Area's circle + Area's square",
        "Area's circle + Area's triangle",
    ],
)
def test_circle_add_area_positive(start_end, add_area_test):
    radius, new_figure, result = add_area_test
    c = Circle(radius)
    print(
        f"circle's area {c.area}, new_figure.area {new_figure.area}, reference result: {result}"
    )
    assert round(c.add_area(new_figure), 2) == result


@pytest.mark.circle
@pytest.mark.parametrize(
    "radius", [-1, 0], ids=["Negative value of radius", "Zero value of radius"]
)
def test_rectangle_sizes_negative(start_end, radius):
    print(f"Incorrect radius's value: {radius}")
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.circle
@pytest.mark.parametrize(
    "radius",
    [test_radius_type_1, test_radius_type_2],
    ids=["Incorrect type str", "incorrect type list"],
)
def test_rectangle_types_negative(start_end, radius):
    print(f"Incorrect radius's value:  {radius} with type {type(radius)}")
    with pytest.raises(TypeError):
        Circle(radius)
