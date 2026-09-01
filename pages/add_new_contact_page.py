import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ContactPage(BasePage):
    ADD_NAV_LINK = (By.CSS_SELECTOR, "[href = '/add']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BTN = (By.XPATH, "//button[b[text()='Save']]")
    CONTACT_NAV_LINK = (By.CSS_SELECTOR, "[href='/contacts']")


    def open_contact_form(self):
        # self.driver.find_element(*self.ADD_NAV_LINK).click()
        self.click(self.ADD_NAV_LINK)

    def fill_name(self, name):
        # self.driver.find_element(*self.NAME_INPUT).clear()
        # self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.fill(self.NAME_INPUT,name)

    def fill_last_name(self, last_name):
        self.fill(self.LAST_NAME_INPUT,last_name)

    def fill_phone(self, phone):
        self.fill(self.PHONE_INPUT,phone)

    def fill_email(self, email):
        self.fill(self.EMAIL_INPUT,email)

    def fill_address(self, address):
        self.fill(self.ADDRESS_INPUT,address)

    def fill_description(self, description):
        self.fill(self.DESCRIPTION_INPUT, description)

    def fill_contact_form(self, contact):
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    def submit_contact(self):
        self.click(self.SAVE_BTN)


    def is_add_button_active(self):
        add_link = self.find(self.ADD_NAV_LINK)
        return "active" in add_link.get_attribute("class")



