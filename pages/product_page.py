from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_same_name_book(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.ADD_BOOK_SUCCESS_ALERT).text
        assert name_book == name_book_in_basket, "Different name book"

    def should_be_same_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_book_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_IN_BASKET).text
        assert price_book == price_book_in_basket, "Different price book"
