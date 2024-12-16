from src.triangle import Triangle
import pytest

test_area_int = [2, 3, 4, 2.9]
test_area_float = [2.2, 3.3, 4.4, 3.51]

test_perimeter_int = [2, 3, 4, 9]
test_perimeter_float = [2.1, 3.3, 4.4, 9.8]


@pytest.mark.triangle
@pytest.mark.parametrize(
    "numbers",
    [test_area_int, test_area_float],
    ids=["Test_integer", "Test_float"],
)
def test_triangle_area_positive(start_end, numbers):
    a, b, c, area = numbers
    print(a, b, c, area)
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
    print(a, b, c, perimeter)
    t = Triangle(a, b, c)
    assert round(t.perimeter, 2) == perimeter


@pytest.mark.triangle
def test_triangle_is_not_triangle_negative(start_end):
    a, b, c = 1, 2, 3
    print(a, b, c)
    with pytest.raises(ValueError):
        Triangle(a, b, c)
