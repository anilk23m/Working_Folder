from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()
