import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_homework_3(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = browser.find_element(By.ID, "dropdown")
    options = dropdown.find_elements(By.CSS_SELECTOR, "option")
    assert len(options) > 0, "В дропдауне нет ни одной опции"

    available_options = []
    for option in options:
        assert option.is_displayed(), f"Опция {option.text} не активна"
        if option.is_enabled():
            available_options.append(option)

    assert len(available_options) >= 2, "Доступных опций меньше двух"

    available_options[0].click()
    assert available_options[0].is_selected(), "Первая опция не выбрана"

    available_options[1].click()
    assert available_options[1].is_selected(), "Вторая опция не выбрана"