import pytest
from src.circle import Circle

test_area_int = (5, 78.54)
test_area_float = (5.5, 95.03)

test_perimeter_int = (5, 31.42)
test_perimeter_float = (5.5, 34.56)

test_radius_type_1 = "test"
test_radius_type_2 = [1, 2, 3]


@pytest.mark.circle
@pytest.mark.parametrize(
    "circle_test", [test_area_int, test_area_float], ids=["Test_integer", "Test_float"]
)
def test_circle_area_positive(start_end, circle_test):
    r, area = circle_test
    print(r, area)
    r = Circle(r)
    assert round(r.area, 2) == area


@pytest.mark.circle
@pytest.mark.parametrize(
    "circle_test",
    [test_perimeter_int, test_perimeter_float],
    ids=["Test_integer", "Test_float"]
)
def test_circle_perimeter_positive(start_end, circle_test):
    r, perimeter = circle_test
    print(r, perimeter)
    r = Circle(r)
    assert round(r.perimeter, 2) == perimeter


@pytest.mark.circle
@pytest.mark.parametrize(
    "radius", [-1, 0], ids=["Negative value of radius", "Zero value of radius"]
)
def test_rectangle_sizes_negative(start_end, radius):
    print(radius)
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.circle
@pytest.mark.parametrize(
    "radius",
    [test_radius_type_1, test_radius_type_2],
    ids=["Incorrect format str", "incorrect format list"]
)
def test_rectangle_types_negative(start_end, radius):
    print(radius)
    with pytest.raises(TypeError):
        Circle(radius)
