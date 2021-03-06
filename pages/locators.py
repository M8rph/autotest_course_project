from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "h1:nth-child(1)")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, "span a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
