import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from resources.constants import MAX_WAIT_INTERVAL
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):

    def type_username(self,usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.username_textbox).clear()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginPageLocators.username_textbox).send_keys(usr_and_pw[0])

    def type_password(self,usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.password_textbox).clear()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginPageLocators.password_textbox).send_keys(usr_and_pw[1])
    def click_login_button(self):
        self.find_element(LoginPageLocators.login_button).click()



    def get_error_message(self):
           """Wait for the error message and return its text"""
           try:
               error_element = WebDriverWait(self.driver, 10).until(
                   ec.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
               )
               return error_element.text
           except:
               return None