class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("total balance= ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, "SBI01224")
print(acc1.account_no, "is having balance", acc1.balance)
acc1.debit(1000)
acc1.credit(35000)
