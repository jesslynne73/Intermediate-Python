#Lab #10
#Due Date: 03/15/2019, 11:59PM
########################################
#                                      
# Name: Jessica Strait
# Collaboration Statement:             
# This code was completed independently with guidance from the following sources:
# The video lecture "Stack and Queue"
# Several supplemental doctests created independently
# Review of Lab 9 methods and relevant recitation notes
########################################

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
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

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
