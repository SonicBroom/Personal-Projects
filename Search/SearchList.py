__author__ = 'Ambrose'

import random

"""
These are my helper functions, you don't have to mess with them
"""
def generate_random_numbers_list(in_size):
    """ (int) -> List
    This function will take in an integer representing the number of random
    numbers to generate and will return a List of that many random numbers
    between 0 and 1000.
    """
    list_of_numbers = []

    for i in range (0, in_size):
        list_of_numbers.append(random.randrange(100000))

    return list_of_numbers

def insertion_sort(in_list_to_sort):
    """ (List) -> List
    This function will take a list of random integers and then apply the insertion
    sort algorithm on it.  It will return a sorted list of numbers.
    """
    i = 1
    sorted_list = []

    while (i < len(in_list_to_sort)):
        if (in_list_to_sort[i] < in_list_to_sort[i - 1]):
            j = i

            while (j >= 1 and in_list_to_sort[j] < in_list_to_sort[j - 1]):
                temp_num = in_list_to_sort[j]
                in_list_to_sort[j] = in_list_to_sort[j - 1]
                in_list_to_sort[j - 1] = temp_num

                j = j - 1

        i += 1

    return in_list_to_sort

def classic_binary_search(in_list, in_item):
    """
    Same input and output as the sequential search, but you will implement a binary search here
    """
    left = 0
    right = len(in_list)
    middle = (right - left) / 2

    while (right - left > 1):
        if in_item == in_list[middle]:
            return middle
        elif in_item < in_list[middle]:
            new_middle = left + (right - left) / 2
            right = middle
            middle = new_middle
        else:
            new_middle = left + (right - left) / 2
            left = middle
            middle = new_middle

    return -1

def recursive_binary_search(in_list, in_item, left, right):
    difference = right - left
    middle = left + (difference / 2)

    if difference <= 1:
        return -1
    if in_list[middle] == in_item:
        return middle
    elif in_list[middle] > in_item:
        return recursive_binary_search(in_list, in_item, left, middle)
    else:
        return recursive_binary_search(in_list, in_item, middle, right)

# Main
unsorted_list = generate_random_numbers_list(20)
sorted_list = insertion_sort(unsorted_list)
print "This is the sorted list of numbers: ", sorted_list, "\n"

# Let's try out our classic implementation of the binary search just to set a baseline for
# the expectded results
index = classic_binary_search(sorted_list, sorted_list[3])
print "%d is located at index: %d" % (sorted_list[3], index)

index = classic_binary_search(sorted_list, sorted_list[11])
print "%d is located at index: %d\n" % (sorted_list[11], index)

index = classic_binary_search(sorted_list, 120000)
print "The index returned is %d\n\n" % (index)

# Now, we're going to try out our binary search function implemented in a recursive manner
index = recursive_binary_search(sorted_list, sorted_list[8], 0 , len(sorted_list))
print "%d is located at index: %d" % (sorted_list[8], index)

index = recursive_binary_search(sorted_list, sorted_list[19], 0, len(sorted_list))
print "%d is located at index: %d\n" % (sorted_list[19], index)

index = recursive_binary_search(sorted_list, 120000, 0, len(sorted_list))
print "The index returned is %d" % (index)
