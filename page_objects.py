import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoldBarPage:
    def __init__(self, driver):
        self.driver = driver

    def weigh_bars(self, left_bars, right_bars):
        for bar in left_bars:
            self.driver.find_element(By.ID, f'left_{bar}').send_keys(str(bar))
        for bar in right_bars:
            self.driver.find_element(By.ID, f'right_{bar}').send_keys(str(bar))
        self.driver.find_element(By.ID, 'weigh').click()
        time.sleep(2)  # Wait for 2 seconds after weighing

    def get_weighing_result(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".game-info > ol > li"))
        )
        result = self.driver.execute_script(
            "return document.querySelector('.game-info > ol > li:last-child').textContent;"
        )
        time.sleep(1)
        return result.strip()

    def reset_scale(self):
        reset_button_xpath = "/html/body/div[1]/div/div[1]/div[4]/button[1]"
        self.driver.find_element(By.XPATH, reset_button_xpath).click()

    def click_gold_bar(self, bar_number):
        self.driver.find_element(By.ID, f'coin_{bar_number}').click()
