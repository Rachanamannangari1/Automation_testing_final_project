from selenium.webdriver.common.by import By
class ProductPageLocators:

  select_drop_down=(By.XPATH,"//select[@class='product_sort_container']")
  inventory_list=(By.XPATH,"//div[@class='inventory_list']/div/div[2]/div[2]/div")
  product_name_list=(By.XPATH,"//div[@class='inventory_list']/div//div[2]/div//div")
  add_to_cart=(By.ID, "add-to-cart")
  cart_number=(By.CLASS_NAME,"shopping_cart_badge")

