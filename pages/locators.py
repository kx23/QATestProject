from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

    REGISTRATION_EMAIL_INPUT = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.NAME, "registration-password1")
    REGISTRATION_PASSWORD_REPEAT_INPUT = (By.NAME, "registration-password2")

    LOGIN_EMAIL_INPUT = (By.NAME, "login-username")
    LOGIN_PASSWORD_INPUT = (By.NAME, "login-password")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRODUCT_NAME_IN_SUCCESFUL_ADDING_NOTIFICATION = (
        By.CSS_SELECTOR,
        ".alert-success:nth-of-type(1) strong",
    )
    PRODUCT_PRICE_IN_SUCCESFUL_ADDING_NOTIFICATION = (
        By.CSS_SELECTOR,
        ".alert-info strong",
    )
