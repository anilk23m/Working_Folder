import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
#dropdown selecting specific value using xpath
driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']/option[3]").click()
driver.implicitly_wait(10)
#click on button
driver.find_element(By.XPATH, "//input[@type='radio' and @value='radio1']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='option1']").click()
driver.implicitly_wait(10)
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
options_list = [option.text for option in dropdown.options]
print(options_list)
assert 'Select' in options_list
assert 'Option1' in options_list
assert  'Option2' in options_list
assert  'Option3' in options_list
#alert handling
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert text", alert.text)
alert.accept()

driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert text", alert.text)
alert.accept() #this will click on pop up ok button
#if want to click on cancel button
# alert.dismiss()

#scroll the page 
driver.execute_script("window.scrollTo(0, 0);")  # Scroll to top
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to bottom
