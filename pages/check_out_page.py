from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.check_out_page_locators import CheckOutLocators
from resources.constants import MAX_WAIT_INTERVAL


class CheckOutPage(BasePage):
    def fill_firstname(self,first_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckOutLocators.first_name).send_keys(first_name)
    def fill_lastname(self,last_name):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckOutLocators.last_name).send_keys(last_name)
    def postal_code(self,postal_code):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, CheckOutLocators.postal_code).send_keys(postal_code)
    def continue_button(self):
        self.find_element(CheckOutLocators.continue_button).click()
    def explicit_wait(self):
        self.explicitly_wait_for_element_selected(MAX_WAIT_INTERVAL,CheckOutLocators.continue_button)

