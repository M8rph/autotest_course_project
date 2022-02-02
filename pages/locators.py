from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1)")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
