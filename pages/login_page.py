from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_NAV_LINK = (By.CSS_SELECTOR,"[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR,"[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='password']")
    LOGIN_BTN = (By.XPATH,"//button[text()='Login']")
    SIGN_OUT_BTN = (By.XPATH,"//*[text()='Sign Out']")


    def open_login_form(self):
        self.click(self.LOGIN_NAV_LINK)


    def fill_email(self,email):
        self.fill(self.EMAIL_INPUT,email)

    def fill_password(self,password):
        self.fill(self.PASSWORD_INPUT,password)

    def submit_login(self):
        self.click(self.LOGIN_BTN)


    def is_logged(self):
        try:
            WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located(self.SIGN_OUT_BTN)
            )
            return True
        except TimeoutException:
            return False





