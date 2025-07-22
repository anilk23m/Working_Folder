import pytest

#here fixtures when applied to a function, that function will be running first before the test functions to which this fixture function pass the value to use
#fixture function defined inside a test file has a scope within the test file only.
#to mark a fixture available to multiple files, we have to define the fixture function in a file called conftest.py
@pytest.fixture()
def input_value():
    value = 90
    return value

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

