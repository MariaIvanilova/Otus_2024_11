from src.square import Square
import pytest

test_area_int = [3, 9]
test_area_float = [3.3, 10.89]

test_perimetr_int = [3, 12]
test_perimetr_float = [3.3, 13.2]

test_size_type_1 = "test"
test_size_type_2 = [1, 2, 3]


@pytest.mark.square
@pytest.mark.parametrize(
    "numbers",
    [test_area_int, test_area_float],
    ids=["Test_integer", "Test_float"]
)
def test_square_area_positive(start_end, numbers):
    a, area = numbers
    print(a, area)
    s = Square(a)
    assert round(s.area, 2) == area


@pytest.mark.square
@pytest.mark.parametrize(
    "numbers",
    [test_perimetr_int, test_perimetr_float],
    ids=["Test_integer", "Test_float"]
)
def test_square_perimetr_positive(start_end, numbers):
    a, perimeter = numbers
    print(a, perimeter)
    s = Square(a)
    assert s.perimeter == perimeter


@pytest.mark.square
@pytest.mark.parametrize(
    "a", [-1, 0], ids=["Negative value of size", "Zero value of size"]
)
def test_rectangle_sizes_negative(start_end, a):
    print(a)
    with pytest.raises(ValueError):
        Square(a)


@pytest.mark.square
@pytest.mark.parametrize(
    "a",
    [test_size_type_1, test_size_type_2],
    ids=["Incorrect format str", "incorrect format list"],
)
def test_rectangle_types_negative(start_end, a):
    print(a)
    with pytest.raises(TypeError):
        Square(a)
