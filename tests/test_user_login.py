import time

from selenium.webdriver.common.by import By

from pages import product_page
from pages.log_out_page import LogOutPage
from pages.login_page import LoginPage
from pages.login_page_locators import LoginPageLocators
from pages.product_page import ProductSort
from resources.constants import TEST_SITE_URL, MAX_WAIT_INTERVAL
from tests.conftest import expected_title


class TestLogin:
    def test_login(self,driver,username_password,expected_result,expected_title):
        test_login_user=LoginPage(driver)
        test_login_user.navigate_to(TEST_SITE_URL)

       # driver.find_element(By.XPATH,"//h3[@data-test='error']/button").click()
        test_login_user.type_username(username_password)
        test_login_user.type_password(username_password)
        test_login_user.click_login_button()

        login_url=driver.current_url
        #test_login_user.explicitly_wait_for_expected_title(MAX_WAIT_INTERVAL,expected_result["login_success_url"])
        assert login_url == expected_result["login_success_url"],"Test user login is failed"
        test_login_user.explicitly_wait_for_expected_title(MAX_WAIT_INTERVAL, expected_title)
        return ProductSort(driver)


    def test_log_out(self,driver,username_password,expected_result,expected_title):

        product_sort = self.test_login(driver, username_password, expected_result, expected_title)
        log_out_page = LogOutPage(product_sort.driver)  # Pass driver to LogOut class
        log_out_page.click_on_menu()
        log_out_page.explicit_wait()
        log_out_page.click_on_log_out()
        current_url=driver.current_url
        assert  current_url==expected_result["log_out_successful"]




