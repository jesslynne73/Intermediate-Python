#HW 4
#Due Date: 04/01/2019, 11:59PM
########################################
#
# Name: Jessica Strait
# Collaboration Statement:
# This assignment was completed independently with guidance from the following sources:
# The HW 3 pseudocode solution on Canvas
# Previously created code for HW 3 and Lab 10
# Review of the class lectures about postfix notation
# https://www.tutorialspoint.com/python/python_tuples.htm for information on multiple values returned from a function
# https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/ for a dictionary review
########################################


# Here is my fixed code from HW 3.
def findNextOpr(txt):
    if not isinstance(txt,str) or len(txt) <= 0:
        return "error: findNextOpr"
    # --- YOUR CODE STARTS HERE
    # Let's begin by setting parameters what the input must be, a non-empty string.
    if type(txt) == str and txt is not None:
        # I will create a list of operators.
        operatorList = ['+', '=', '-', '*', '/', '^']
        # This for loop will check each character in the string and see if it's in the operator list.
        for character in txt:
            # If the operator is present, we should return that index as the first operator.
            if character in operatorList:
                return txt.index(character)
            else:
                pass
            # If the for loop goes through and finds no operators, we must return a -1.
        return -1
    else:
        return 'error'


def isNumber(txt):
    if not isinstance(txt, str) or len(txt) == 0:
        return "error: isNumber"
    # --- YOU CODE STARTS HERE
    # Again, let's stipulate what the input must be.
    if type(txt) == str and txt is not None:
        # If we can turn the string into a float, then it must be a number!
        try:
            float(txt)
            return True
        # If a ValueError occurs, then the string must not be a number.
        except ValueError:
            return False
    else:
        return 'error'


def getNextNumber(expr, pos):
    if not isinstance(expr, str) or not isinstance(pos, int) or len(expr) == 0 or pos < 0 or pos >= len(expr):
        return None, None, "error: getNextNumber"
    # --- YOU CODE STARTS HERE
    # One last time, let's make sure that the input it a non-empty string.
    if type(expr) == str and expr is not None:
        # This time, we also need to ensure that that the position is a non-negative integer.
        if type(pos) == int and pos >= 0:
            # I'll create a new expression, slicing the old one at the given position and stripping away the spaces.
            new_expr = expr[pos:]
            new_expr = new_expr.strip(" ")
            # If the new expression begins with a minus sign, we treat it as a negative sign rather than an operator.
            if new_expr[0] == '-':
                # We'll save the position of the negative sign in the original expression.
                minus_position = expr.find('-', pos)
                # We'll create a subexpression consisting of everything after the negative sign.
                subexpression = expr[(minus_position + 1):]
                # Now, we'll run findNextOpr on our subexpression, checking everything after the negative sign.
                operator_position = findNextOpr(subexpression)
                # This if statement will handle what to do if no operators are found.
                if operator_position == -1:
                    # We set the operator and its position value to None.
                    operator = None
                    operator_position = None
                    # I'll create a variable that runs isNumber at the subexpression.
                    number = isNumber(expr[pos:])
                    # If there is such a number, we'll save it as a float to be returned.
                    if number is True:
                        next_number = float(expr[pos:])
                    # Otherwise, no such number exists.
                    else:
                        next_number = None
                else:
                    # We'll reestablish operator_position as the position in the original expression.
                    operator_position = operator_position + minus_position + 1
                    # We'll run a similar check to determine if there is a number at our specific index.
                    if isNumber(expr[pos:operator_position]) is True:
                        next_number = float(expr[pos:operator_position])
                    else:
                        # Otherwise, no such number exists.
                        next_number = None
                    # If an operator is found, it exists at operator_position in the original expression.
                    operator = expr[operator_position]
            else:
                # If there is no negative sign to worry about, then we can find the operator_position right away
                # beginning at pos in the original expression.
                operator_position = findNextOpr(expr[pos:])
                # Again, if there is no operator, we set operator and operator_position to none.
                if operator_position == -1:
                    operator = None
                    operator_position = None
                    # Again, we'll run our isNumber check and return the number either as a float or
                    # None if it is not a number.
                    if isNumber(expr[pos:]) is True:
                        next_number = float(expr[pos:])
                    else:
                        next_number = None
                else:
                    # We'll reset operator position into the original expression position.
                    operator_position = operator_position + pos
                    # We'll check for isNumber and return either the number as a float or None.
                    if isNumber(expr[pos:operator_position]) is True:
                        next_number = float(expr[pos:operator_position])
                    else:
                        next_number = None
                    # The operator exists at the original expression in the operator position spot.
                    operator = expr[operator_position]
            # Then we return the next number value, the next operator, and the position of the operator.
            return next_number, operator, operator_position
        else:
            return 'error'
    else:
        return 'error'

# Now, I will put my code from Lab 10 to help us create the postfix expressions.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Stack:

    def __init__(self):
        self.top = None

    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top, out))

    __repr__ = __str__

    def isEmpty(self):
        # This is where my code begins. I will start by checking to see if self.top exists.
        if self.top is None:
            # If there is no self.top, then the stack must be empty and we return true.
            return True
        else:
            # Otherwise, the stack is not empty and we return false.
            return False

    def __len__(self):
        # I'll set a temp value equal to the top of the stack, and a count variable at 0.
        temp = self.top
        count = 0
        # We'll traverse the stack with a while loop, adding one as long as our temp value is not none.
        while temp is not None:
            count += 1
            temp = temp.next
        # Then we return our count value.
        return count

    def peek(self):
        # If there is no self.top, then the stack is empty and there is nothing for us to peek.
        if self.top is None:
            return 'Stack is empty'
        else:
            # Otherwise, we return self.top. Remember to use the value function so we don't get a node!
            return self.top.value

    def push(self, value):
        # First, we need to create an instance of class Node at our new value. We'll call that new_node
        new_node = Node(value)
        # I'll set a temp variable at self.top: this is the only end we can push to.
        temp = self.top
        # I'll place our new node so it is just in front of that temp variable (the top of the stack).
        new_node.next = temp
        # Then, I'll reassign self.top as our new node. We don't need to return anything
        self.top = new_node

    def pop(self):
        # If the stack is empty, we can't pop anything.
        if self.top is None:
            return 'Stack is empty'
        else:
            # I'll set a temp variable at the top of the stack: this is the only end we can pop from.
            temp = self.top
            # I'll check the value of the top of the stack and create a variable to save it for later.
            return_value = temp.value
            # I need to reassign self.top as the value after that temp variable.
            self.top = temp.next
            # I can delete my temp item entirely.
            del temp
            # Now, I return the variable that I saved for later.
            return return_value

# Now, we will write new code to actually complete HW 4.


def postfix(expr):
    # First, we'll instantiate class Stack from Lab 10.
    stack = Stack()
    # I want to strip the spaces so I can ensure that this expression does not end in an expression. That would not be
    # a valid mathematical expression.
    simple_expression = expr.strip(" ")
    if simple_expression[-1] in "+-*/^":
        return 'error, invalid expression'
    # I'll initialize pos (to be used in getNextNumber) to index zero of the expression string.
    pos = 0
    # Let's create an empty string to put the completed expression in over time.
    postfix_expression = ''
    # I'll also create a prioritized dictionary according to the order of operations to determine when to pop.
    operator_dictionary = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    # Now, we run getNextNumber and save those values under convenient variable names.
    next_number, operator, operator_position = getNextNumber(expr, pos)
    # If operator_position was negative one, then there are no operators and we return an error.
    if operator_position == -1:
        return 'error, invalid expression'
    # If next_number is none, we should also raise an error.
    if next_number is None:
        return 'error, invalid expression'
    # These counts will help me to determine if the expression has too many operators and is invalid.
    number_count = 0
    operator_count = 0
    # This while loop will run as long as there are more numbers in the expression to add to the postfix string.
    while next_number is not None:
        # We add one to our number count with each new next_number variable we come across.
        number_count += 1
        # Then, we add that number as a string in float format to the postfix string.
        postfix_expression += ' '+str(float(next_number))
        # If the operator is not none, we need to increase our operator count and do some other fun things.
        if operator is not None:
            operator_count += 1
            # If there is an operator in the stack already, we need to compare its priority to the new operator.
            if stack.top is not None:
                while operator_dictionary[operator] <= operator_dictionary[stack.top.value]:
                    # As long as the new operator is of lower priority than the top of the stack, we need to get the
                    # operator at the top of the stack, pop that node from the stack, and append the value to the
                    # postfix string.
                    new_operator = stack.top.value
                    stack.pop()
                    postfix_expression += " "+new_operator
                    # If the stack becomes empty, we break from this while loop because there is no top value.
                    if stack.top is None:
                        break
                # Once we have removed everything of higher or equal precedence to our operator, we push our operator.
                stack.push(operator)
            # If the stack was empty to begin with, we can just push our new operator.
            else:
                stack.push(operator)
        # If we have no operators left, we need to remove and append everything still in the stack.
        if operator_position is None:
            while stack.top is not None:
                new_operator = stack.pop()
                postfix_expression += " "+new_operator
            # We can then break from the large loop entirely, because we have all our numbers and no new operators.
            break
        # We now look only at the original expression from the index directly after that of the operator we just
        # examined during this loop.
        pos = operator_position+1
        # Then, we run getNextNumber again to find out our new variables from this updated position.
        next_number, operator, operator_position = getNextNumber(expr, pos)
    # The nature of my while loop starts out the expression with a space, so I'll remove that just for aesthetics.
    postfix_expression = postfix_expression.lstrip(" ")
    # Here is where our count values become important! If there are as many or more operators than there are numbers in
    # the expression, it was never a valid expression to begin with. We should just call up an error now that our
    # program knows that the postfix cannot possibly be correct.
    if operator_count >= number_count:
        return 'error, invalid expression'
    # Otherwise, the expression passed all our validity tests, and we can return the expression we created.
    else:
        return postfix_expression
