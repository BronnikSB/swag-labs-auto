from pages.base_page import BasePage


class MainPage(BasePage):
    product = ".inventory_list > div"
    product_name = '[data-test="inventory-item-name"]'

    def get_count_product_list(self):
        list_product = self.page.locator(self.product)
        count = list_product.count()
        return count

    def get_name_product_list(self):
        product_names = self.page.locator(self.product_name).all()
        list_names = [i.text_content() for i in product_names]
        return list_names

