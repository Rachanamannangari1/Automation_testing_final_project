import time

from pages.base_page import BasePage
from pages.log_out_page_locators import LogOutLocators
from resources.constants import MAX_WAIT_INTERVAL
from tests.conftest import expected_title


class LogOutPage(BasePage):
    def click_on_menu(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LogOutLocators.menu_icon).click()
    def explicit_wait(self):
        self.explicitly_wait_for_element_clickable(MAX_WAIT_INTERVAL,LogOutLocators.LOg_out_link)

    def click_on_log_out(self):
        #self.explicitly_wait_for_expected_title(MAX_WAIT_INTERVAL,expected_title)
        #time.sleep(10)

        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LogOutLocators.LOg_out_link).click()
