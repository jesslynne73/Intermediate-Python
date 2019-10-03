# Author: Jessica Strait
# This project supports basic vector operations: addition, subtraction, multiplication, and dot products.
class Vector:

    def __init__(self, vector_list):
        self.vector = vector_list

    # Let's start by writing our add function. We're good at adding! We will take self and other as parameters.
    def __add__(self, other):
        # First, let's make sure the data types are vectors. If they are not, we will check for another elif condition.
        if type(self) == Vector and type(other) == Vector:
            # Now, the lengths must be the same. If they are not, we return the invalid dimensions.
            if len(self.vector) == len(other.vector):
                # Let's make a list that we can easily convert into a vector once we are done adding.
                solution_list = []
                # With a simple for loop, we can run through every item in the vectors and sum them by matching index.
                for value in range(len(self.vector)):
                    sum = self.vector[value] + other.vector[value]
                    # We will append our solutions to the solution list and continue running the loop.
                    solution_list.append(sum)
                    value += 1
                # To create output in the correct format, we need to make the solution list into a vector.
                output_vector = Vector(solution_list)
                # Finally, we return that vector we just created under our variable name.
                return output_vector
            else:
                return 'Error - Invalid dimensions'
        # If one item is a vector and one is an integer, we return invalid operation rather than dimension.
        elif type(self) == Vector and type(other) == int:
            return 'Error - Invalid operation'
        # In any other condition, we can return invalid dimensions.
        else:
            return 'Error - Invalid dimensions'

    # Our substraction function will be very similar to the addition function in terms of parameters.
    def __sub__(self, other):
        # Again, we check for data types. We want both types to be vectors.
        if type(self) == Vector and type(other) == Vector:
            # The vectors must be equal in length.
            if len(self.vector) == len(other.vector):
                # We'll make a similar solution list to turn into a vector.
                solution_list = []
                # We'll use the same type of for loop to subtract values by checking the index.
                for value in range(len(self.vector)):
                    difference = self.vector[value] - other.vector[value]
                    # We will append our differences to the solution list and continue the for loop.
                    solution_list.append(difference)
                    value += 1
                # Once more, we convert our solution list to a vector and return it.
                output_vector = Vector(solution_list)
                return output_vector
            else:
                return 'Error - Invalid dimensions'
        # If one is a vector and one is an integer, we return invalid operation.
        elif type(self) == Vector and type(other) == int:
            return 'Error - Invalid operation'
        # Otherwise, we just return invalid dimensions.
        else:
            return 'Error - Invalid dimensions'

    # The multiplication function will be a bit more challenging, but it will start the same.
    def __mul__(self, other):
        # Again, let's check our data types. Things are easiest if they are both vectors.
        if type(self) == Vector and type(other) == Vector:
            # I'll set a total variable that I can use to sum my products.
            total = 0
            # We'll make a for loop to again multiply our values based on index.
            for value in range(len(self.vector)):
                product = self.vector[value] * other.vector[value]
                # This time, we will sum our products inside our total variable and continue the for loop.
                total += product
                value += 1
            # Then, we can return our total as a simple integer.
            return total
        # If the expression is a vector times an integer, we will be completing scalar multiplication.
        elif type(self) == Vector and type(other) == int:
            # I'll set the integer to a "multiple" variable for simplicity.
            multiple = other
            # We'll make another list that we can convert to a vector later.
            product_list = []
            # With this for loop, we will multiply each term in the vector by our multiple variable.
            for value in range(len(self.vector)):
                product = self.vector[value] * multiple
                # Then, we append the product to the product list and continue the for loop.
                product_list.append(product)
                value += 1
                # As with addition and subtraction, we convert our output to a vector and return it.
            output_vector = Vector(product_list)
            return output_vector

    def __rmul__(self, other):
        # Now, if the expression is an integer times a vector, we use rmul to complete our multiplcation.
        if type(self) == Vector and type(other) == int:
            # Once the parameters are set, I'll conduct everything in the same way as with the other scalar function.
            multiple = other
            product_list = []
            for value in range(len(self.vector)):
                product = self.vector[value] * multiple
                product_list.append(product)
                value += 1
            output_vector = Vector(product_list)
            return output_vector

    def __eq__(self, other):
        # The lengths of the vectors must be equal for them to be equivalent.
        if len(self.vector) == len(other.vector):
            # We'll use a simple for loop to verify that every term is the same.
            for value in range(len(self.vector)):
                if self.vector[value] == other.vector[value]:
                    pass
                else:
                    return False
            return True
        else:
            return False

    # With this string function, we are returning all those output_vector statements as a string.
    def __str__(self):
        return "Vector("+str(self.vector)+")"

    # This statement allows us to represent our objects as strings.
    __repr__ = __str__



