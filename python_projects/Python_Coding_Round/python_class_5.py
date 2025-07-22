class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print(self.is_checked_out)

    def return_book(self):
        self.is_checked_out = False
        print(self.is_checked_out)

    def status(self):
        print("current status is", self.is_checked_out)
        return self.is_checked_out

book1 = Book("Gayatri Mantra", "Om Swami")
book1.check_out()
book1.return_book()
book1.status()
