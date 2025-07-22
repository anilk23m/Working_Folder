import pytest

# to run a single file we will use pytest <filename> -v
# if we dont pass any file name, it will run all the test case files  as default
# if we want to run a specific function we will use two method - either by substring match of function name or by group
#substring match of function name - pytest -k <substring> -v - it will run functions having that substring
#group using marker decorator - @pytest.mark.<markername> - it will run those functions which are labeled with this markername decorator
#@pytest.mark.greater and @pytest.mark.less are the decorators used to group the test functions so that we can run them using pytest -m <markername>
#Here we need to have pytest.ini file where we will have to register those markers first else it will give PytestUnknownMarkWarning error

@pytest.mark.greater
def test_greater():
    num = 101
    assert num > 100

@pytest.mark.greater
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.less
def test_less():
    num = 100
    assert num > 100

