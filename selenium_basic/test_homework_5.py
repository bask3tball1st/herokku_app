import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_homework_5(browser):
    browser.get("https://the-internet.herokuapp.com/typos")
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    assert len(paragraphs) > 0, "На странице нет параграфов"

    correct_text = "Sometimes you'll see a typo, other times you won't."
    text = paragraphs[-1].text.strip()
    assert text in correct_text, "Текст не соответсвует правильному написанию"