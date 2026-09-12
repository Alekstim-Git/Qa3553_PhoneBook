from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        logger.debug(f"Click on {locator}")
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, value):
        logger.debug(f"Fill{locator}with{value}")
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver,timeout=5).until(
            EC.alert_is_present()
        )

        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()