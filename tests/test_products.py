import shutil
import time

from pages.check_out_complete_page import CheckOutCompletePage
from pages.check_out_page import CheckOutPage
from pages.log_out_page import LogOutPage
from pages.login_page import LoginPage
from pages.product_page import ProductSort
from pages.shopping_cart_page import ShoppingCartPage
from resources.constants import First_Name, Last_Name, Postal_Code, TEST_SITE_URL
from tests.conftest import username_password, driver
from tests.test_user_login import TestLogin


class TestPriceSort(TestLogin):

    def test_sort_price(self,driver,username_password,expected_result,expected_title):
        price_sort=self.test_login(driver,username_password,expected_result,expected_title)
        price_sort.drop_down_action()
        price= price_sort.get_product_price__sorted()
        assert price == expected_result["price"], "list is not sorted"
        return ProductSort(driver)


    def test_add_to_cart(self,driver,username_password,expected_result,expected_title):
        add_to_cart=self.test_sort_price(driver,username_password,expected_result,expected_title)
        add_to_cart.get_product_name()#click on the selected product
        assert expected_result["select_product_url"] in driver.current_url,"item not displayed in the separate page"

        add_to_cart.click_add_to_cart()
        cart_number_text=add_to_cart.get_cart_number()
        assert cart_number_text in expected_result["expected cart_number"],"The total item count displayed in the shopping cart does not match the expected value"
        return ShoppingCartPage(driver)

    def test_shopping_cart(self,driver,username_password,expected_result,expected_title):
        shopping_cart=self.test_add_to_cart(driver,username_password,expected_result,expected_title)
        shopping_cart.explicit_wait_cart()

        shopping_cart.click_shopping_cart()
        #time.sleep(10)
        cart_items=shopping_cart.get_cart_items()
        assert cart_items in expected_result["item_name"],"selected items are not displayed in the shopping cart"
        item_price=shopping_cart.get_cart_item_price()
        assert  item_price in expected_result["item_price"],"The actual product price displayed in the shopping cart does not match with expected price"
        shopping_cart.click_check_out_button()
        return CheckOutPage(driver)

    def test_check_out_page(self,driver,username_password,expected_result,expected_title):
        test_check_out_page=self.test_shopping_cart(driver,username_password,expected_result,expected_title)
        test_check_out_page.fill_firstname(First_Name)
        test_check_out_page.fill_lastname(Last_Name)
        test_check_out_page.postal_code(Postal_Code)
        test_check_out_page.continue_button()
        current_url=driver.current_url
        assert current_url in expected_result["check_out_url"],"Actual URL is not matching with expected URL"
        return  CheckOutCompletePage(driver)

    def test_check_out_complete(self,driver,username_password,expected_result,expected_title):
        test_check_out_complete=self.test_check_out_page(driver,username_password,expected_result, expected_title)
        total_summary=test_check_out_complete.get_total_summary_label()
        assert total_summary in expected_result["Price Total"]
        test_check_out_complete.clock_on_finish_button()
        order_complete_message=test_check_out_complete.get_complete_order_text()
        assert order_complete_message in expected_result["order complete message"]












