from pages.base_page import BasePage

class InventoryPage(BasePage):

    def add_first_product_to_cart(self):
        self.click("(//button[contains(text(),'Add to cart')])[1]")

    def go_to_cart(self):
        self.click(".shopping_cart_link")