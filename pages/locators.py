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
