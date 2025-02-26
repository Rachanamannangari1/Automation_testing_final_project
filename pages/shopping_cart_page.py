from pages.base_page import BasePage
from pages.product_page_locators import ProductPageLocators
from pages.shopping_cart_locators import ShoppingCartLocators
from resources.constants import MAX_WAIT_INTERVAL


class ShoppingCartPage(BasePage):
    def explicit_wait_cart(self):
        self.explicitly_wait_for_element_clickable(MAX_WAIT_INTERVAL,ShoppingCartLocators.shopping_cart_link)
    def click_shopping_cart(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ShoppingCartLocators.shopping_cart_link).click()
    def get_cart_items(self):
        cart_items=self.find_elements(ShoppingCartLocators.cart_items)

        for cart_item in cart_items:
          cart_item.text.__contains__("Sauce Labs Bike Light")

          return cart_item.text

    def get_cart_item_price(self):
        price = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ShoppingCartLocators.item_price).text
        return price
    def explict_wait_check_out_button(self):
        self.explicitly_wait_for_element_clickable(MAX_WAIT_INTERVAL,ShoppingCartLocators.check_out_button)
    def click_check_out_button(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ShoppingCartLocators.check_out_button).click()