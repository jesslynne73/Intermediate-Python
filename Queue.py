# Author: Jessica Strait
# This project implements the queue data structure.

class Node:

    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:

    def __init__(self): 
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        # This is where my code begins. I will check to see if self.head is none: if it is, the queue must be empty.
        if self.head is None:
            return True
        else:
            # Otherwise, the queue is not empty and we return False.
            return False

    def __len__(self):
        # I'll create a temp value starting at self.head, the "front" of the queue. I'll also set a count variable to 0.
        temp = self.head
        count = 0
        # We'll traverse the list until the temp value is none, meaning we've reached the end of the queue. For each
        # item, we increase our count value by 1.
        while temp is not None:
            count += 1
            temp = temp.next
        # Then we return our count variable.
        return count

    def enqueue(self, value):
        # If the queue is not empty, we need to examine the tail of the queue.
        if self.head is not None:
            # We'll create an instance of class Node at our value and call it new_node.
            new_node = Node(value)
            # I'll set a temp value to the existing tail of the queue.
            temp = self.tail
            # I'll let the value after the temp variable equal our new node.
            temp.next = new_node
            # Then, I'll reassign self.tail as the new_node.
            self.tail = new_node
        else:
            # If the queue is empty, we still instantiate class Node at our value.
            new_node = Node(value)
            # Because the queue is empty, self.head and self.tail will both equal new_node until new items are enqueued.
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        # First, we must check if the queue is empty.
        if self.head is not None:
            # Then, we need to check if the queue has only one value.
            if self.head == self.tail:
                # I'll set a variable at self.head, chosen arbitrarily over self.tail since there is only one item.
                item = self.head
                # I'll save the value of my item for returning later.
                return_value = item.value
                # I'm setting both self.head and self.tail to "item.next," which is simply None. When we have dequeued
                # the item variable, these values should both be none.
                self.head = item.next
                self.tail = item.next
                # Then I delete my single item.
                del item
                # We return the value that we saved earlier.
                return return_value
            else:
                # If the queue has at least two values, we only examine self.head. I'll call it an item variable.
                item = self.head
                # I'll save the value of my item for returning later.
                return_value = item.value
                # I'll set the new self.head to the next item in the queue after my item.
                self.head = item.next
                # Then I delete my item.
                del item
                # We return the value that we saved earlier.
                return return_value
        else:
            # If the queue is empty, we cannot dequeue anything.
            return 'Queue is empty'
