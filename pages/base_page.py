from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))


    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    def find_elements(self, locator_type_and_locator_tuple):
        return self.driver.find_elements(*locator_type_and_locator_tuple)


    def explicitly_wait_for_expected_title(self,interval,expected_title):
        WebDriverWait(self.driver,interval).until(ec.title_contains(expected_title))

    def explicitly_wait_for_element_clickable(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.element_to_be_clickable(locator_type_and_locator_tuple))

    def get_text(self,interval,locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.element_to_be_clickable(locator_type_and_locator_tuple)).text

