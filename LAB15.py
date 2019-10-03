#LAB 15
#Due Date: 04/05/2019, 11:59PM
########################################
#
# Name: Jessica Strait
# Collaboration Statement:             
# This code was completed independently with guidance from the following resources:
# The video lectures on sorting algorithms
########################################


def merge(list1, list2):
    #write your code here
    # First, I will create an empty list that I can append to later.
    merged_list = []
    # I will create two index checking variables that begin at zero.
    first_index = 0
    second_index = 0
    # This while loop will check that my indexes are within the length of the lists.
    while first_index < len(list1) and second_index < len(list2):
        # If the the first element in list1 is smaller than the first element in list 2...
        if list1[first_index] <= list2[second_index]:
            # I append that element to my final list.
            merged_list.append(list1[first_index])
            # I've taken care of the value at that index, so I need to increase my index checker by one.
            first_index += 1
        # If the opposite is true, I simply append the first element of the second list to my list.
        else:
            merged_list.append(list2[second_index])
            # In that case, I will be increasing my second index checker variable by one.
            second_index += 1
    # This for loop will be called if list 1 has remaining values when list 2 is empty. It will run through the indexes
    # that were not checked, and will append those values to my list.
    for index in range(first_index, len(list1)):
        merged_list.append(list1[index])
    # This for loop will work if the above statement is true of list 2.
    for index in range(second_index, len(list2)):
        merged_list.append(list2[index])
    # Then, I return my merged list.
    return merged_list


def mergeSort(numList):
    #write your code here
    if type(numList) is not list:
        return 'error'
    # Firstly, if the length of the list is zero, I should raise an error.
    if len(numList) <= 0:
        return 'error'
    # If the list is exactly one element, I can just return that element. It will be my base case for a recursive call.
    if len(numList) == 1:
        return numList
    # I'll find the middle by integer division (no remainder allowed) on the length of the list.
    middle = len(numList)//2
    # I will call mergeSort recursively on the left and right sides that I've created. Remember that the right side
    # won't actually be called until the left side has been totally sorted.
    left_side = mergeSort(numList[:middle])
    right_side = mergeSort(numList[middle:])
    # Then, we must merge the two sides of the list that we've created.
    return merge(left_side, right_side)
