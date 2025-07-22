import pytest
#pytest command will execute all the files of format test_* or _test* in the current directory and subdirectories.

import math

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def test_square():
    num = 7
    assert 7*7 == 49

# This case will not execute as Pytest module will not consider this function as test case as it's name is not the format of test*.
@pytest.mark.other
def tesequality():
    assert 10 == 11

@pytest.mark.other
def testequality():
    assert 100 == 100



