# This class looks clean but this is not. This is simply a mess.
# Let's try to add SOLID principles
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

    def pay(self, payment_type, security_code):
        if payment_type == 'debit':
            print(f'Processing {payment_type} payment')
            print(f'Verifying security code {security_code}')
            self.status = 'paid'
        elif payment_type == 'credit':
            print(f'Processing {payment_type} payment')
            print(f'Verifying security code {security_code}')
            self.status = 'paid'
        else:
            raise Exception(f"Unknown Payment Type {payment_type}")


order = Order()
order.add_item('Brown Bread', 2, 20)
order.add_item('Peanut Butter', 1, 50)
order.add_item('Oregano', 10, 10)

print(order.total_prices())

order.pay('debit', '123123')
