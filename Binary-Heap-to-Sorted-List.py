# Author: Jessica Strait
# This project implements my own binary heap code to create a maximum priority heap. Then, it sorts the heap into a list.


# This is all code copied and pasted from Binary-Heap.
class MaxHeapPriorityQueue:

    def __init__(self):
        self.heap = []
        self.size = 0

    # I'm going to make the __len__ attribute a property method to ensure a proper return value.
    @property
    def __len__(self):
        # If the size of the heap is empty, we can just return zero.
        if self.size == 0:
            return '0'
        else:
            # Otherwise, we can measure the length as we would a list and return that value.
            length = len(self.heap)
            return length

    def parent(self, index):
        # If the index calls up the root or exceeds the heap, we should return None.
        if index <= 1 or index > self.size:
            return None
        # We'll use the index function taught in the video lecture to determine the index of the parent in the tree.
        parent_tree_index = (index//2)
        # However, in the list, this index value will be one less. We'll use that number to find the value at that
        # special list index.
        parent_value = self.heap[parent_tree_index-1]
        # We'll return the value of the parent that we determined through its index.
        return parent_value

    def leftChild(self, index):
        # If the index is smaller than one or there is no left child (exceeds the size of the heap), we return none.
        if index < 1 or (2*index) > self.size:
            return None
        # Otherwise, we use the function taught in the lecture to find the index of the left child within the tree.
        else:
            return self.heap[2*index - 1]


    def rightChild(self, index):
        # If the index is smaller than one or there is no right child (exceeds the size of the heap), we return none.
        if index < 1 or (2*index + 1) > self.size:
            return None
        # Otherwise, we use the function taught in the lecture to find the index of the right child within the tree.
        else:
            return self.heap[2*index]

    def swap(self, index1, index2):
        # This was provided with the starter code.
        self.heap[index1-1], self.heap[index2-1] = self.heap[index2-1], self.heap[index1-1]

    def insert(self, x):
        # If the heap is empty, we can just append our new x value to the "list" and increase the size by one.
        if self.size == 0:
            self.heap.append(x)
            self.size += 1
        else:
            # Otherwise, we still begin by appending our new x value.
            self.heap.append(x)
            # I'll save the LIST index value for that new x.
            item_list_index = self.heap.index(x)
            # If the value is exactly one, then the parent tree index must be one (list index 0).
            if item_list_index == 1:
                parent_tree_index = 1
                parent = self.heap[parent_tree_index - 1]
            else:
                # Otherwise, we'll use our special parent index calculation again.
                parent_tree_index = ((item_list_index + 1) // 2)
                parent = self.heap[parent_tree_index - 1]
            while parent < x:
                # While the parent is greater than x, we must swap the tree index and our list index altered to match
                # the tree index conventions.
                self.swap(parent_tree_index, item_list_index + 1)
                # We'll set our item list index variable to the updated index.
                item_list_index = self.heap.index(x)
                # If that index is exactly zero, then the item is the root and we should stop.
                if item_list_index == 0:
                    break
                # Otherwise, we calculate the new parent and run the while loop until the parent is not larger than x.
                parent_tree_index = ((item_list_index + 1) // 2)
                parent = self.heap[parent_tree_index - 1]
            # Don't forget to increase the size by 1 with each insertion!
            self.size += 1

    def deleteMax(self):
        # Firstly, if there is only one element in the list, we need to only delete that single element.
        if self.size == 1:
            deleted = self.heap[0]
            del self.heap[0]
            return deleted
        # Otherwise, we initialize the element to be deleted at index 0, and set a current variable to 1.
        deleted = self.heap[0]
        current = 1
        # We'll swap our to-be-deleted element and the last element in the list (at index equal to self.size)
        self.swap(self.heap.index(deleted)+1, self.size)
        # We remove that last element, but remember to subtract one to adjust for list indexing rules.
        del self.heap[self.size-1]
        # Don't forget to decrease the size of the heap by one!
        self.size -= 1
        # The value that we moved is now at the root of the heap, index zero in the list.
        moved_value = self.heap[0]
        # While there exists a left child...
        while self.leftChild(current) is not None:
            # If there exists a right child exceeding the left child...
            if self.rightChild(current) is not None and self.rightChild(current) > self.leftChild(current):
                # If the right child is less than the moved value, we should break the loop. The moved value is correct.
                if self.rightChild(current) <= moved_value:
                    break
                # Otherwise, we will swap the right child and our current variable.
                # We also reassign current to be the right child, since we just swapped it.
                else:
                    self.swap(current, current*2 + 1)
                    current = current*2 + 1
            # If there is no right child, there may still be a left child requiring swapping.
            else:
                # If the moved value is greater than the left child, its position is correct.
                if self.leftChild(current) <= moved_value:
                    break
                # Otherwise, we swap the left child and our current variable, and reassign current.
                else:
                    self.swap(current, current*2)
                    current = current*2
        # We'll return the "deleted" variable that we set earlier.
        return deleted

# Here is where the new code to produce a sort list begins.

def heapSort(numList):
    sort_heap = MaxHeapPriorityQueue()
    # First, I'll use a quick for loop to insert each value in the list into a heap.
    for value in numList:
        sort_heap.insert(value)
    # I'll create an empty list to insert sorted values into in a moment.
    sorted_list = []
    # This length variable will help run our while loop. The while loop will run until this length value equals zero,
    # meaning that each value from the list has been sorted.
    length = len(numList)
    while length > 0:
        # The new value will be the returned "deleted" element from the deleteMax function.
        new_value = sort_heap.deleteMax()
        # Remember that deleteMax returns the largest number, but we want our list in ascending order.
        # So, we need to insert each increasingly small number at the BEGINNING of the list, not appending to the end.
        sorted_list = [new_value] + sorted_list
        # With each iteration, I'll subtract one from our length variable so the while loop will end at the right time.
        length -= 1
    # Then, we return the sorted list.
    return sorted_list
