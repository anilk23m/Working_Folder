from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service)
driver.get("https://rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()