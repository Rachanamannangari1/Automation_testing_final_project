from select import select
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.product_page_locators import ProductPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class ProductSort(BasePage):
    def drop_down_action(self):
      sort_dropdown=Select(self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ProductPageLocators.select_drop_down))
      sort_dropdown.select_by_visible_text("Price (low to high)")

    def get_product_price__sorted(self):
      inventory_list=self.find_elements(ProductPageLocators.inventory_list)
      price_list = []
      price = []
      for element in inventory_list:
          price_list.append(element.text)
      print(price_list)
      for p in price_list:
          price.append(float(p[1:]))

      return price
    def get_product_name(self):
        product_names_list=self.find_elements(ProductPageLocators.product_name_list)


        for product in product_names_list:
          if product.text.__contains__("Sauce Labs Bike Light"):
            product.click()
            break


    def click_add_to_cart(self):
         self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ProductPageLocators.add_to_cart).click()

    def get_cart_number(self):
        cart_number_text=self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,ProductPageLocators.cart_number).text
        return cart_number_text
