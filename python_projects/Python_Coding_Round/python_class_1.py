class BankAccount:

    def __init__(self, account_holder_name:str, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <=0:
            print("Withdraw amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"{amount} withdrawn successfully.")

    def get_balance(self):
        return self.balance

account1 = BankAccount("Alice", 1000)
account1.deposit(500)
account1.withdraw(400)
final_balance = account1.get_balance()
print(final_balance)


