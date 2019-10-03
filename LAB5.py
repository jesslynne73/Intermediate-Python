class SodaMachine:

    def __init__(self, product, price):
    #-- start code here ---
        # First, I'll assign some variables to make life a little easier. We should also set our balance and
        # stock to zero initially.
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0

    def purchase(self):
    #-- start code here ---
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
    #-- start code here ---
        # Let's start by checking if there is any soda to be sold. If not, the balance does not change.
        if self.stock <= 0:
            return 'Sorry, out of stock. Take your ${} back'.format(amount)
        else:
            # We should increase the balance by the amount deposited.
            self.balance += amount
            return 'Balance: ${}'.format(self.balance)

    def restock(self, amount):
    #-- start code here ---
        # We should increase the stock by the amount restocked by our customer.
        self.stock += amount
        return 'Current soda stock: {}'.format(self.stock)


class Line:

    def __init__(self, coord1, coord2):
    # -- start code here ---
        # I'll start by setting some quick variables to help me out.
        self.coord1 = coord1
        self.coord2 = coord2

    # Remember, we need to use our property methods here! This helps our code behave flexibly for any user.
    @property
    def distance(self):
    # -- start code here ---
        # I'm going to set some variables here to ensure no math errors take place. It never hurts to be cautious, and
        # it's okay to do things in a few steps if it helps you!
        x_values = (self.coord2[0] - self.coord1[0])**2
        y_values = (self.coord2[1] - self.coord1[1])**2
        under_radical = x_values + y_values
        distance = under_radical**(1/2)
        # We must round our solution to three decimal places.
        return round(distance, 3)
    # -- ends here ---

    # Again, we need our property method.
    @property
    def slope(self):
    # -- start code here ---
        # I'll use a try and except block to calculate the slope in any case except when x_numbers = 0
        try:
            y_numbers = self.coord2[1] - self.coord1[1]
            x_numbers = self.coord2[0] - self.coord1[0]
            slope = y_numbers / x_numbers
            # We'll round our solution to three decimal places again.
            return round(slope, 3)
        # If there is a zero division error, meaning that the line is horizontal, we can return infinity.
        except ZeroDivisionError:
            return 'Infinity'
    # -- ends here ---
