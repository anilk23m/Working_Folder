from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//i[@class='hm-icon nav-sprite']").click()
driver.find_element(By.XPATH, "//a[@role='button']//div[contains(text(),'Electronics')]").click()


