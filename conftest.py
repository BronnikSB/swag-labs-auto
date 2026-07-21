import pytest

from playwright.sync_api import Page

from config import STANDARD_USER, PASSWORD, BASE_URL
from pages.base_page import BasePage

user_name = "#user-name"
password = "#password"
login_button = "#login-button"


@pytest.fixture
def auth_page(page: Page) -> Page:
    page.goto(BASE_URL)
    page.locator(user_name).fill(STANDARD_USER)
    page.locator(password).fill(PASSWORD)
    page.locator(login_button).click()
    return page
