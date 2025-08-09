from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL_INPUT
        ), "Login email input not found"
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_PASSWORD_INPUT
        ), "Login password input not found"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL_INPUT
        ), "Registration email input not found"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT
        ), "Registration password input not found"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_INPUT
        ), "Repeat password input not found"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL_INPUT
        )
        email_input.send_keys(email)

        pass1_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT
        )
        pass1_input.send_keys(password)

        pass2_input = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_INPUT
        )
        pass2_input.send_keys(password)

        registration_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON
        )
        registration_button.click()
