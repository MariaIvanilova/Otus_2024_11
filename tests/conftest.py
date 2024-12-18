import pytest


@pytest.fixture(scope="function", autouse=True)
def start_end():
    print("\nStart action")
    yield
    print("\nEnd action")
