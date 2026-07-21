from config import BASE_URL
from config import STANDARD_USER
from config import PASSWORD
from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login_01(page):
    login = LoginPage(page)
    login.open(BASE_URL)
    login.login(STANDARD_USER, PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
