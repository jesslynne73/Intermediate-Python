# Author: Jessica Strait
# This project implements the concept of a maximum priority binary heap through a linked list.

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
        # We'll use the index function taught in the video lecture to determine the index of the parent in the tree.
        parent_tree_index = (index//2)
        # However, in the list, this index value will be one less. We'll use that number to find the value at that
        # special list index.
        parent_value = self.heap[parent_tree_index-1]
        # If the index calls up the root or exceeds the heap, we should return None.
        if index <= 1 or index > self.size:
            return None
        # Otherwise, we'll return the value of the parent that we determined through its index.
        else:
            return parent_value

    def leftChild(self, index):
        # Again, we'll use the function taught in the video lecture to find the index of the left child within the tree.
        left_child_tree_index = 2*index
        # We need to subtract one to account for the index difference within the list.
        if self.heap[left_child_tree_index-1] is not None:
            # If the value is not none, we return the value at the list index.
            return self.heap[left_child_tree_index-1]
        else:
            return None

    def rightChild(self, index):
        # We'll use the function taught in the video lecture to find the index of the right child within the tree.
        right_child_tree_index = (2*index)+1
        if self.heap[right_child_tree_index] is not None:
            # If the value is not none, we return the value at the special list index.
            return self.heap[right_child_tree_index-1]
        else:
            return None

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
                parent = self.heap[parent_tree_index-1]
                print(x, parent, item_list_index)
            else:
                # Otherwise, we'll use our special parent index calculation again.
                parent_tree_index = ((item_list_index+1)//2)
                parent = self.heap[parent_tree_index-1]
                print(x, parent)
            while parent < x:
                # While the parent is greater than x, we must swap the tree index and our list index altered to match
                # the tree index conventions.
                self.swap(parent_tree_index, item_list_index+1)
                # We'll set our item list index variable to the updated index.
                item_list_index = self.heap.index(x)
                # If that index is exactly zero, then the item is the root and we should stop.
                if item_list_index == 0:
                    break
                # Otherwise, we calculate the new parent and run the while loop until the parent is not larger than x.
                parent_tree_index = ((item_list_index+1)//2)
                parent = self.heap[parent_tree_index-1]
            # Don't forget to increase the size by 1 with each insertion!
            self.size += 1

    def deleteMax(self):
        # If the size of the list is empty, we should return None because there's no max value to delete.
        if self.size <= 0:
            return None
        # If the list has only one value, it must be the max. So we need to return that single value, the root, and make
        #  our heap completely empty.
        elif self.size == 1:
            self.size = 0
            max_value = self.heap[0]
            self.heap = []
            return max_value
        # If the heap is any other size, we have some work to do!
        else:
            # First, I want to know the length of the heap so I can figure out what the last value will be.
            length = len(self.heap)
            # We must remember to subtract one from the length because list indexes start at zero.
            swapped_value = self.heap[length-1]
            # I'll also go ahead and save the TREE index of the swapped value to help me with the swapping process.
            swapped_value_index = self.heap.index(swapped_value)+1
            # The max value will be the root of the heap.
            max_value = self.heap[0]
            # Now, we can swap using 1 (the tree index of the max value) and our saved index from earlier.
            self.swap(1, swapped_value_index)
            # We should delete the new last value, which we just swapped out to be the max.
            del self.heap[length-1]
            # So, the new tree index of our swapped value is 1.
            new_tree_index = 1
            # We'll use our left/right child equations to determine those indexes. We'll adjust to list conventions.
            n = (new_tree_index*2)-1
            m = new_tree_index*2
            # We have a lot of if statements to take care of. First, let's check if there are left and right children.
            if n and m in range(len(self.heap)):
                # If they are, I'll set some temp variables to save those values.
                temp1 = self.heap[n]
                temp2 = self.heap[m]
                # We need to determine which value is larger, the left or right child. We should only compare one at a
                # time to the root value.
                if temp1 > temp2:
                    max_temp = temp1
                else:
                    max_temp = temp2
            # Alternatively, if there is no right child, only the left child can be compared to the root.
            elif n in range(len(self.heap)) and m not in range(len(self.heap)):
                max_temp = self.heap[n]
            # Similarly, if there is no left child, only the right child can be compared to the root.
            elif m in range(len(self.heap)) and n not in range(len(self.heap)):
                max_temp = self.heap[m]
            # If there are no children, we have an empty heap now, and we can just return the max_value.
            else:
                self.size = 0
                self.heap = []
                return max_value
            # Let's save the list index of our max temp value.
            temp_index = self.heap.index(max_temp)
            # As long as max temp exceeds the swapped value, we need to run this while statement.
            while max_temp > swapped_value:
                # First, let's adjust our indexes to tree conventions and run the swap function.
                self.swap(temp_index+1, self.heap.index(swapped_value)+1)
                # Now, we have a new tree index: the old index from that temp value.
                new_tree_index = temp_index+1
                # We'll create new left and right child equations.
                n = (new_tree_index*2)-1
                m = new_tree_index*2
                # We need to check and see if the left child exists, or if it is None.
                if n in range(len(self.heap)):
                    temp1 = self.heap[n]
                else:
                    temp1 = None
                # We need to do the same for the right child.
                if m in range(len(self.heap)):
                    temp2 = self.heap[m]
                else:
                    temp2 = None
                # If neither value is none, we need to compare the children again to find the max temp value.
                if temp1 is not None and temp2 is not None:
                    if temp1 > temp2:
                        max_temp = temp1
                    else:
                        max_temp = temp2
                # If one of the values is none, the other one defaults to our new max temp value.
                elif temp1 is None and temp2 is not None:
                    max_temp = temp2
                elif temp1 is not None and temp2 is None:
                    max_temp = temp1
                # If both values are none (the swapped value is now a leaf), we should break our loop.
                elif temp1 is None and temp2 is None:
                    break
                # We'll get a new temp index to do our swap again as we continue running the while loop.
                temp_index = self.heap.index(max_temp)
            # We need to decrease the size of our heap by one.
            self.size -= 1
            # Finally, we return the original max value that we removed.
            return max_value

    def betterInsert(self, x):
        if self.size == 0:
            self.heap.append(x)
            self.size += 1
        else:
            self.heap.append(x)
            self.size += 1
            current_index = self.size
            print(current_index, self.heap[current_index-1], self.parent(current_index))
            while current_index > 1 and self.parent(current_index) < self.heap[current_index - 1]:
                parent_of_x = current_index//2
                self.swap(current_index, parent_of_x)
                current_index = parent_of_x


h = MaxHeapPriorityQueue()
h.insert(5)
h.insert(6)
h.insert(17)
h.insert(7)
h.insert(50)
print(h.insert(60))
print(h.heap)
