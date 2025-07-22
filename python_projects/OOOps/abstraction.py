from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_amount(self):
        pass


class CreditCardPayment(Payment):
    def process_amount(self):
        return f'amount processed for credit card {self.amount}'


class UPIPayment(Payment):
    def process_amount(self):
        return f'amount processed for UPI Payment {self.amount}'


payment1 = CreditCardPayment(15000)
payment2 = UPIPayment(20000)

print(payment1.process_amount())
print(payment2.process_amount())