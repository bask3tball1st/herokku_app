import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.basic
def test_homework_4(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")

    input_field.send_keys(3)
    assert int(input_field.get_attribute("value")) == 3, "Поле не приняло цифровое значение"

    input_field.send_keys(Keys.ARROW_UP)
    assert int(input_field.get_attribute("value")) == 4, "Поле не принимает ввод стрелочкой вверх"

    input_field.send_keys(Keys.ARROW_DOWN)
    input_field.send_keys(Keys.ARROW_DOWN)
    assert int(input_field.get_attribute("value")) == 2, "Поле не принимает ввод стрелочкой вниз"

    input_field.clear()
    input_field.send_keys("a")
    assert input_field.get_attribute("value") != "a", "Поле принимает буквенные значения"