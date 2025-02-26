from selenium.webdriver.common.by import By


class CheckOutCompleteLocators:

   complete_order_text=(By.CLASS_NAME,"complete-header")
   summary_total_label=(By.XPATH,"// div[ @class ='summary_total_label']")
   button_finish=(By.ID,"finish")
