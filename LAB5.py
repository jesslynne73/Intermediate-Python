# Author: Jessica Strait
# This project introduces elementary class methods through a soda machine simulation.
class SodaMachine:

    def __init__(self, product, price):
        # First, I'll assign some variables to make life a little easier. We should also set our balance and
        # stock to zero initially.
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0

    def purchase(self):
        # We'll start with an if statement to ensure that at least one soda is in stock for our customer to buy.
        if self.stock < 1:
            return 'Product out of stock'
        else:
            # Now, if the balance is less than the price, the customer needs to deposit the remaining difference.
            if self.balance < self.price:
                return 'Please deposit ${}'.format(int(self.price-self.balance))
            # If the balance is exactly that of the price, there is no change. Remember to decrease the stock though!
            elif self.balance == self.price:
                self.balance = 0
                self.stock -= 1
                return '{} dispensed'.format(self.product)
            # In this case, we can use simple subtraction to determine the change for the customer. Again, remember to
            # decrease the stock by one. This time, we need to reset the balance to zero manually, because we "told the
            # user to take their change, which would set the balance to zero.
            elif self.balance > self.price:
                self.stock -= 1
                change = self.balance - self.price
                self.balance = 0
                return '{} dispensed, take your ${}'.format(self.product, int(change))

    def deposit(self, amount):
        # Let's start by checking if there is any soda to be sold. If not, the balance does not change.
        if self.stock <= 0:
            return 'Sorry, out of stock. Take your ${} back'.format(amount)
        else:
            # We should increase the balance by the amount deposited.
            self.balance += amount
            return 'Balance: ${}'.format(self.balance)

    def restock(self, amount):
        # We should increase the stock by the amount restocked by our customer.
        self.stock += amount
        return 'Current soda stock: {}'.format(self.stock)
