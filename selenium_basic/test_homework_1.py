import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_homework_1(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser.find_element(By.XPATH, '//button[text()="Add Element"]')
    add_element.click()
    add_element.click()
    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')

    assert add_element.is_displayed(), "There should be 1 element added"
    assert len(delete_elements) == 2, "There should be 2 elements deleted"