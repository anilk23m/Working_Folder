from pages.base_page import BasePage

class CartPage(BasePage):

    def verify_product_in_cart(self):
        return self.page.locator(".inventory_item_name").is_visible()

    def click_checkout(self):
        self.click("#checkout")