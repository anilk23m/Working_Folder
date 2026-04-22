from pages.base_page import BasePage
from utils.config import BASE_URL

class LoginPage(BasePage):

    def load(self):
        self.open(BASE_URL)

    def login(self, username, password):
        self.type("#user-name", username)
        self.type("#password", password)
        self.click("#login-button")