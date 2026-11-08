import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_homework_2(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    assert not checkboxes[0].is_selected(), "Первый чекбокс должен быть в статусе uncheck"
    checkboxes[0].click()
    assert checkboxes[0].is_selected(), "Первый чекбокс должен быть в статусе check"

    assert checkboxes[1].is_selected(), "Второй чекбокс должен быть в статусе check"
    checkboxes[1].click()
    assert not checkboxes[1].is_selected(), "Второй чекбокс должен быть в статусе uncheck"