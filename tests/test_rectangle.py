from src.rectangle import Rectangle
import pytest

test_area_int = [3, 5, 15]
test_area_float = [3.5, 5.5, 19.25]

test_perimetr_int = [3, 5, 16]
test_perimetr_float = [3.5, 5.5, 18]

test_size_negative = [-1, 5]
test_size_zero = [0, 5]

test_size_type_1 = ["test", 5]
test_size_type_2 = [5, [1, 2, 3]]


@pytest.mark.rectangle
@pytest.mark.parametrize(
    "numbers",
    [test_area_int, test_area_float],
    ids=["Test_integer", "Test_float"]
)
def test_rectangle_area_positive(start_end, numbers):
    a, b, area = numbers
    print(a, b, area)
    r = Rectangle(a, b)
    assert r.area == area


@pytest.mark.rectangle
@pytest.mark.parametrize(
    "numbers",
    [test_perimetr_int, test_perimetr_float],
    ids=["Test_integer", "Test_float"]
)
def test_rectangle_perimetr_positive(start_end, numbers):
    a, b, perimetr = numbers
    print(a, b, perimetr)
    r = Rectangle(a, b)
    assert r.perimeter == perimetr


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("a", "b"),
    [test_size_negative, test_size_zero],
    ids=["Negative value of size", "Zero value of size"],
)
def test_rectangle_sizes_negative(start_end, a, b):
    print(a, b)
    with pytest.raises(ValueError):
        Rectangle(a, b)


@pytest.mark.rectangle
@pytest.mark.parametrize(
    ("a", "b"),
    [test_size_type_1, test_size_type_2],
    ids=["Incorrect format str", "incorrect format list"]
)
def test_rectangle_types_negative(start_end, a, b):
    print(a, b)
    with pytest.raises(TypeError):
        Rectangle(a, b)
