import pytest

@pytest.fixture(scope="function")
def left_list():
    return [3, 4, 2, 1, 3, 3]

@pytest.fixture(scope="function")
def second_list():
    return [4, 3, 5, 3, 9, 3]