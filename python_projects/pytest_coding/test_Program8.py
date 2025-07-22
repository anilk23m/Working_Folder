import pytest
from selenium import webdriver

driver = None
@pytest.fixture
def setup():
    print("start browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test_1(setup):
    driver.get("http://www.facebook.com")
    print("Test1 executed")

def test_2(setup):
    driver.get("https://www.google.com")
    print("Test2 executed")

def test_3(setup):
    driver.get("https://www.gmail.com")
    print("Test3 executed")