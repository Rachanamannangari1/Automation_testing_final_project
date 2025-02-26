from selenium.webdriver.common.by import By


class ShoppingCartLocators:
  shopping_cart = (By.CLASS_NAME, "shopping_cart_badge")
  cart_items=(By.XPATH,"//div[@class='cart_item']//a/div")
  item_price=(By.XPATH,"//div[@class='cart_item']//div[2]/div[2]/div")
  check_out_button=(By.XPATH,"//div[@class='cart_footer']//button[2]")
  shopping_cart_link=(By.XPATH, "//a[@class='shopping_cart_link']")