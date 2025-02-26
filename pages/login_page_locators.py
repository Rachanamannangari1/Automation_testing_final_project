from selenium.webdriver.common.by import By


class LoginPageLocators:
    error_message=(By.XPATH,"//button[@class='error-button']")
    username_textbox=(By.ID,"user-name")
    password_textbox=(By.ID,"password")
    login_button=(By.ID,"login-button")