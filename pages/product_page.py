from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_name_in_notification(self):
        assert (
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            == self.browser.find_element(
                *ProductPageLocators.PRODUCT_NAME_IN_SUCCESFUL_ADDING_NOTIFICATION
            ).text
        ), "Product name in notification is incorrect"

    def should_be_correct_price_in_notification(self):
        assert (
            self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
            == self.browser.find_element(
                *ProductPageLocators.PRODUCT_PRICE_IN_SUCCESFUL_ADDING_NOTIFICATION
            ).text
        ), "Basket price in notification is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is not disappeared, but should be"
