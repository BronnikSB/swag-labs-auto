from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_button = "#login-button"
    user_name = "#user-name"
    password = "#password"

    def login(self, username, password):
        self.page.locator(self.user_name).fill(username)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.login_button).click()
