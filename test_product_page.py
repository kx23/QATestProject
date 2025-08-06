from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.add_to_basket()
    page.should_be_correct_price_in_notification()
    page.should_be_correct_product_name_in_notification()
