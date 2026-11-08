from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
add_element.click()
add_element.click()
delete_elements = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

assert len(delete_elements) == 2, "There should be 2 elements deleted"
assert add_element.is_displayed(), "There should be 1 element added"

driver.quit()