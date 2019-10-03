#HW 6
#Due Date: 04/26/2019, 11:59PM
########################################
#
# Name: Jessica Strait
# Collaboration Statement:
# This code was completed independently with guidance from the following sources:
# Code from Labs 10 & 11
# Review of the video lectures about BFS, DFs, and Dijkstra's algorithm
# Review of Piazza page (particularly questions about sorting methods)
# https://www.programiz.com/python-programming/methods/list/sort for information on the sort method
# https://www.programiz.com/python-programming/methods/built-in/sorted for information on the reverse aspect of sorting
# Assistance from TA Lawrence Lee
# https://realpython.com/python-lists-tuples/ for a review on tuples and how they work
# Use of the community-created Dijkstra doctests shared on Piazza
########################################

# ---Copy your code from labs 10 and 11 here (you can remove their comments)


class StackNode:
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
        new_node = StackNode(value)
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


class QueueNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        temp = self.head
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = ' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head, self.tail, out))

    __repr__ = __str__

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
            new_node = QueueNode(value)
            # I'll set a temp value to the existing tail of the queue.
            temp = self.tail
            # I'll let the value after the temp variable equal our new node.
            temp.next = new_node
            # Then, I'll reassign self.tail as the new_node.
            self.tail = new_node
        else:
            # If the queue is empty, we still instantiate class Node at our value.
            new_node = QueueNode(value)
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

#----- HW6 Graph code

class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        # Your code starts here
        # First, I want to check and make sure that the start variable is in the graph representation.
        if start not in self.vertList:
            return 'error'
        # I'll create a new instance of class queue.
        q = Queue()
        # I'll enqueue my "start" value.
        q.enqueue(start)
        # This empty list will hold each visited node, and will be what I return.
        visited_nodes = []
        # I can go ahead and append my "start" value to that list.
        visited_nodes.append(start)
        # I can use my isEmpty() function to check that the queue still has values in it.
        while not q.isEmpty():
            # This variable stores that values that I'm removing from the queue.
            dequeued_node = q.dequeue()
            # This for loop traverses a sorted list of all the neighbors to each dequeued item. Remember, we need to use
            # alphabetical order, so this sorting is important.
            for new_node in sorted(self.vertList[dequeued_node]):
                # If the type is a tuple, then the graph is weighted and I can take the value at index 0 as my value to
                # be appended in the output list.
                if type(new_node) == tuple:
                    new_node = new_node[0]
                # Regardless, I need to check if my "new_node" variable is already in the visited nodes list.
                if new_node not in visited_nodes:
                    # If it is not, I need to enqueue that value and append it to my output list. I need to enqueue it
                    # so we can visit its neighbors with the next iteration. I must append it so it will be returned.
                    q.enqueue(new_node)
                    visited_nodes.append(new_node)
                # If the value is already in the visited_nodes list, I can just pass and continue with the loop.
                else:
                    pass
        # The return value is the visited_nodes list that we created.
        return visited_nodes

    def dfs(self, start):
        # Your code starts here
        # As with BFS, I need to check that the start variable is in the graph representation.
        if start not in self.vertList:
            return 'error'
        # I'll instantiate class stack to help me out.
        s = Stack()
        # I can go ahead and push my start variable into the stack.
        s.push(start)
        # I'll create another empty visited_nodes list that I'll use as my output.
        visited_nodes = []
        # I can use my isEmpty() function to ensure that the stack is not empty.
        while not s.isEmpty():
            # I want to pop the top node on my stack.
            popped_node = s.pop()
            # If it a tuple, then we need to consider the value at index 0.
            if type(popped_node) == tuple:
                popped_node = popped_node[0]
            # Similar to BFS, we need to check that the popped node is not yet in the list.
            if popped_node not in visited_nodes:
                # If it isn't, we need to append the popped node.
                visited_nodes.append(popped_node)
                # We need to complete a DESCENDING sort on our list to make sure the order of our stack is correct as
                # the iterations continue. Remember, alphabetical order is important to us, and we are checking the
                # longest possible paths, so we will need to backtrack.
                for new_node in sorted(self.vertList[popped_node], reverse=True):
                    # If the new node isn't in the visited_nodes list, we need to push it to the stack so we can deal
                    # with it later.
                    if new_node not in visited_nodes:
                        s.push(new_node)
            # If the popped node is already in the list, we can just pass and continue the loop.
            else:
                pass
        # Again, we will return our value list as output.
        return visited_nodes

    # EXTRA CREDIT, uncomment method definition if submitting extra credit

    def dijkstra(self, start):
        # Your code starts here
        # As with BFS and DFS, I'll run the same check on the input to make sure the start value is correct.
        if start not in self.vertList:
            return 'error'
        # My output will be a dictionary, so I'll start with an empty one.
        output = {}
        # The visited nodes list we've been using will be helpful even if I'm not returning it.
        visited_nodes = []
        # I'm going to instantiate a queue.
        q = Queue()
        # For every node in the graph, I want to define its key in my dictionary as infinity for now.
        for node_value in self.vertList:
            output[node_value] = float('inf')
        # However, the key for my start value must be zero (because that will always be the shortest path to itself).
        output[start] = 0
        # Now, I'll enqueue my start variable.
        q.enqueue(start)
        # I'll use my isEmpty() function to check for values in the queue.
        while not q.isEmpty():
            # The vertex points are all in the queue, and we're going to go through them.
            vertex = str(q.dequeue())
            # For each neighbor of the vertex in the graph representation...
            for value in self.vertList[vertex]:
                # Let's make sure the edge we're traveling on isn't weighted. We may have to do some different things.
                if type(value) != tuple:
                    # If the value has not yet been visited...
                    if value not in visited_nodes:
                        # I need to "visit" the node by adding it to the queue and making a note of it by appending it
                        # to my list for future reference.
                        visited_nodes.append(value)
                        q.enqueue(value)
                    # If the dictionary key of the neighbor is greater than the key of the vertex plus one, then I need
                    # to reassign the key of my current neighbor.
                    if output[value] > output[vertex] + 1:
                        output[value] = output[vertex] + 1
                    # Everything below here is for tuples, so I should continue if the value is not a tuple.
                    continue
                # Now, if the value is a tuple, we need to check if the tuple at index zero has been visited.
                elif value[0] not in visited_nodes:
                    # If it has not, we need to enqueue it and make a note just like we did for unweighted graphs.
                    visited_nodes.append(value[0])
                    q.enqueue(value[0])
                # Even though it looks more complicated because of the brackets, this is the same comparison that we did
                # earlier, but for a weighted graph. This means that our new path is shorter (and for this algorithm,
                # better), so we want to reassign its key to this new shorter path.
                if output[value[0]] > output[vertex] + value[1]:
                    output[value[0]] = output[vertex] + value[1]
        # We are returning our dictionary with the shortest path possibilities saved as keys.
        return output
