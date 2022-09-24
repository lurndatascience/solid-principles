# 1.Single Responsibility
# Make things (classes, functions, etc.) responsible for fulfilling one type of role.
# e.g. Refactor code responsibilities into separate classes.


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


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print(f'Processing debit payment')
        print(f'Verifying security code {security_code}')
        self.status = 'paid'

    def pay_credit(self, order, security_code):
        print(f'Processing credit payment')
        print(f'Verifying security code {security_code}')
        self.status = 'paid'


security_code = '123123'
order = Order()
order.add_item('Brown Bread', 2, 20)
order.add_item('Peanut Butter', 1, 50)
order.add_item('Oregano', 10, 10)

print(order.total_prices())

payment_processor = PaymentProcessor()
payment_processor.pay_credit(order, security_code)
