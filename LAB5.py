# Author: Jessica Strait
# This project takes two points and uses property methods to calculate distance or slope between the points.
class Line:

    def __init__(self, coord1, coord2):
        # I'll start by setting some quick variables to help me out.
        self.coord1 = coord1
        self.coord2 = coord2

    # Remember, we need to use our property methods here! This helps our code behave flexibly for any user.
    @property
    def distance(self):
        # I'm going to set some variables here to ensure no math errors take place. It never hurts to be cautious, and
        # it's okay to do things in a few steps if it helps you!
        x_values = (self.coord2[0] - self.coord1[0])**2
        y_values = (self.coord2[1] - self.coord1[1])**2
        under_radical = x_values + y_values
        distance = under_radical**(1/2)
        # We must round our solution to three decimal places.
        return round(distance, 3)

    # Again, we need our property method.
    @property
    def slope(self):
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
