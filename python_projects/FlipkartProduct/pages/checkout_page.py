from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def fill_details(self, first, last, zip_code):
        self.type("#first-name", first)
        self.type("#last-name", last)
        self.type("#postal-code", zip_code)

    def continue_checkout(self):
        self.click("#continue")

    def finish_order(self):
        self.click("#finish")

    def get_success_message(self):
        return self.get_text(".complete-header")