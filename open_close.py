# 2.Open/Closed
# Be able to add new functionality to existing code easily without modifying existing code.
# e.g. Use abstract classes.

from abc import ABC, abstractmethod


class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_prices(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class Payment(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class PayDebitProcessor(Payment):
    def pay(self, order, security_code):
        print(f'Processing debit payment')
        print(f'Verifying security code {security_code}')
        self.status = 'paid'


class PayCreditProcessor(Payment):
    def pay(self, order, security_code):
        print(f'Processing credit payment')
        print(f'Verifying security code {security_code}')
        self.status = 'paid'


security_code = '123123'
order = Order()
order.add_item('Brown Bread', 2, 20)
order.add_item('Peanut Butter', 1, 50)
order.add_item('Oregano', 10, 10)

print(order.total_prices())

payment_processor = PayCreditProcessor()
payment_processor.pay(order, security_code)
