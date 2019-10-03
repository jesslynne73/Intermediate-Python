# Quiz 2 - Coding Part
# March 28th, 2019
# Author: Jessica Strait
# This code was completed independently with guidance from the following sources:
# Review of Lab9
#######################


# QUESTION 1
def power(x, n):
    # Write your code here
    # First I will check to see if both inputs are integers. If they are not, I'll return error.
    if type(x) is not int:
        return 'error'
    elif type(n) is not int:
        return 'error'
    else:
        # If n is negative, we will also return error.
        if n < 0:
            return 'error'
        # If n is exactly zero, we will return one.
        if n == 0:
            return 1
        # If n is exactly one, we return x.
        if n == 1:
            return x
        # Otherwise, we will use a recursive call to multiply x times the power function of x to the next smaller power.
        else:
            return x * power(x, n-1)


# QUESTION 2
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        current=self.head
        out=[]
        while current:
            out.append(str(current.value))
            current=current.next
        out=' '.join(out)
        return 'Head:{}, Tail:{}\nList:{}'.format(self.head, self.tail,out)

    __repr__=__str__

    def __len__(self):
        return self.count

    def append(self, value):
        # My code begins here. If the type of value is not linked list, we can append as given in the starter code.
        if type(value) is not LinkedList:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.count += 1
        # If the type of value is a linked list, things get more interesting.
        else:
            # I will fix a variable at the head of the linked list.
            start = value.head
            # While the list is not empty...
            while start is not None:
                # We will instantiate class Node at the integer value of the "index" we are using with start.
                new_node = Node(start.value)
                # If the existing list is empty, our new node is the head and the tail.
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    self.count += 1
                else:
                    # Otherwise, we'll append our new node to the end of the linked list and call it self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                    # We'll redefine start so that our while loop can continue.
                    start = start.next
                    # We must add one to the count to ensure that our length function will still return correctly.
                    self.count += 1
