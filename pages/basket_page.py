from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_summary(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_SUMMARY
        ), "Basket summary is presented, but should not be"

    def should_be_empty_basket_label(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_LABEL
        ), "Empty basket label should be presented, it is not"
