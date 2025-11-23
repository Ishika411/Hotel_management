from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} in cash.")

class CardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid ₹{amount} using card ending {self.card_number[-4:]}.")