import requests
class IRCTC:
    def __init__(self):

        user_input = input("""How would you like to proceed?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule""")

        if user_input == 1:
            print("Live train status")
        elif user_input == 2:
            print("PNR")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("Enter the train number: ")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        url = f"https://petstore.swagger.io/v2/pet/findByStatus?status={train_no}"
        data = requests.get(url=url)
        print(data.status_code)
        data = data.json()
        print(data)

obj = IRCTC()
