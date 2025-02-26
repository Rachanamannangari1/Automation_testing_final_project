from selenium.webdriver.common.by import By


class CheckOutLocators:
    first_name=(By.ID,"first-name")
    last_name=(By.ID,"last-name")
    postal_code=(By.ID,"postal-code")
    continue_button=(By.ID,"continue")
    total_amount=(By.CLASS_NAME,"summary_subtotal_label")
    total_label= (By.XPATH,"//div[@class='summary_total_label']")