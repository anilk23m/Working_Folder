#class name - pascal Case - LoginPage, CostSheet, BrowserManager
#object - snake case - login_page, cost_sheet, browser_manager
#Methods - Functions inside class - snake case - open_browser(), click_login()
#attributes - snake case - self.browser_type, self.base_url,

class LoginPage:
    def __init__(self,username,password, url):
        self.username = username #object reference self we used to set the data/attributes for the object
        self.password = password
        self.url = url
    def open(self): #methods are the functions inside class
        print(f"Opening {self.url}")
    def enter_username(self):
        print(f"Entering username {self.username}")
    def enter_password(self):
        print(f"Entering password {self.password}")
    def click_login(self):
        print(f"Clicking login button")
login1 = LoginPage("anilk", "testing1234", "https://www.google.com")
login1.open()
login1.enter_username()
login1.open()
login1.enter_username()
login1.enter_password()

#Constructor - Special method that runs automatically when object is created
#__init__ - dunder (double under square) - Constructor name in python
#self - Refers to current object itself
#self.attribute - data belongs to this object
#python passes self automatically. you never pass self manually.

