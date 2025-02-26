import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    user_name = "standard_user"
    password = "secret_sauce"
    return [user_name,password]


@pytest.fixture(scope="function")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()

    
@pytest.fixture(scope="session")
def expected_result():
    return {"login_success_url":"https://www.saucedemo.com/inventory.html",
            "price":[7.99, 9.99, 15.99, 15.99, 29.99, 49.99],
            "select_product_url":"https://www.saucedemo.com/inventory-item.html?id=0",
            "expected cart_number":"1",
            "item_name":"Sauce Labs Bike Light",
            "item_price":"$9.99",
            "check_out_url":"https://www.saucedemo.com/checkout-step-two.html",
            "Price Total":"Total: $10.79",
             "order complete message":"Thank you for your order!",
            "log_out_successful":"https://www.saucedemo.com/"
    }


@pytest.fixture(scope="session")
def expected_title():
    return "Swag Labs"