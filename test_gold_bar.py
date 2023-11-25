import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from page_objects import GoldBarPage

def find_fake_bar(driver, gold_bar_page):
    bars = list(range(9))

    while len(bars) > 1:
        third_length = len(bars) // 3
        group1 = bars[:third_length]
        group2 = bars[third_length:2 * third_length]
        group3 = bars[2 * third_length:]

        # Weigh the first two groups
        gold_bar_page.weigh_bars(group1, group2)
        result = gold_bar_page.get_weighing_result()

        if '<' in result:
            bars = group1  # Fake bar is in the first group
        elif '>' in result:
            bars = group2  # Fake bar is in the second group
        else:
            bars = group3  # Fake bar is in the third group

        gold_bar_page.reset_scale()

    return bars[0]

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--enable-javascript")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_gold_bar_alert_message(driver):
    gold_bar_page = GoldBarPage(driver)

    # Navigate to the website
    driver.get('http://sdetchallenge.fetch.com/')

    # Find the fake bar using the recursive algorithm
    fake_bar = find_fake_bar(driver, gold_bar_page)

    # Click on the gold bar and check for the alert
    gold_bar_page.click_gold_bar(fake_bar)
    time.sleep(2)  # Wait for 2 seconds to observe the alert

    try:
        # Wait for the alert to be present
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = Alert(driver).text
        # Check the alert message
        assert 'Yay! You find it!' in alert_text
        if 'Oops! Try Again!' in alert_text:
            assert False, "Found the wrong fake gold bar."
    except Exception as e:
        print(f"An error occurred: {e}")
        assert False, "No alert present"
