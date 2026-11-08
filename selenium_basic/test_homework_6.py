import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_homework_6(browser):
    browser.get("https://the-internet.herokuapp.com/tables")
    element1 = browser.find_element(By.XPATH, "//table[1]//tbody/tr[4]/td[2]")
    assert element1.text == "Tim", f"Ожидалось имя Tim, получено {element1.text}"

    element2 = browser.find_element(By.XPATH, "//table[1]//tbody/tr[3]/td[1]")
    assert element2.text != "Bach", f"Ожидалось любая фамилия кроме Bach"

    table = browser.find_element(By.XPATH, "//table[1]")
    rows = table.find_elements(By.XPATH, ".//tbody/tr")
    assert len(rows) > 0, "Таблица пустая"

    for row in rows:
        values = row.find_elements(By.XPATH, ".//td")
        assert len(values) > 0, "В строке нет значений"

        assert ".com" in values[4].text, "В ячейке нет домена .com"