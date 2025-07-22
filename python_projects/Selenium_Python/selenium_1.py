from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

driver.find_element(By.ID, "small-searchterms").send_keys("Laptop")

# driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME, "Password").clear()
# driver.find_element(By.NAME, "Password").send_keys("admin")
# driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
