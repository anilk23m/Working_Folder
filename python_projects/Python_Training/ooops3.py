class LoginPage:
    def set_value(self, username, password):
        self.username = username
        self.password = password
        self.url = "https://gmail.com"
    def open_login_page(self):
        print(f"Opening Login Page {self.url}")
    def enter_username(self):
        print(f"Entering username {self.username}")
    def enter_password(self):
        print(f"Entering password {self.password}")
    def click_login(self):
        print("Clicking login button")
login = LoginPage()
login.set_value("admin", "testing123")
login.open_login_page()
login.enter_username()
login.enter_password()
login.click_login()
