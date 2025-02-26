from pages.base_page import BasePage
from pages.check_out_complete_locators import CheckOutCompleteLocators
from resources.constants import MAX_WAIT_INTERVAL


class CheckOutCompletePage(BasePage):
    def get_total_summary_label(self):
        total_summary_label=self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckOutCompleteLocators.summary_total_label).text
        return total_summary_label
    def clock_on_finish_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckOutCompleteLocators.button_finish).click()
    def get_complete_order_text(self):
        complete_order_text= self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CheckOutCompleteLocators.complete_order_text).text
        return complete_order_text
