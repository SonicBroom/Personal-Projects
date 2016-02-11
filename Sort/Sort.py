import random

__author__ = 'ambli'

def generate_random_numbers_list(in_size):
    """ (int) -> List
    This function will take in an integer representing the number of random
    numbers to generate and will return a List of that many random numbers
    between 0 and 1000.
    """
    list_of_numbers = []

    for i in range (0, in_size):
        list_of_numbers.append(random.randrange(1000))

    return list_of_numbers

def bubble_sort(in_list_to_sort):
    """ (List) -> List
    This function will take a list of random integers and then apply bubble
    sort on it.  It will return a sorted list of numbers.
    """
    list_is_sorted = False

    while (list_is_sorted is False):
        list_is_sorted = True           # Default to True... and set it to False if we make a swap
        i = 0

        while (i < len(in_list_to_sort) - 1):
            if (in_list_to_sort[i] > in_list_to_sort[i + 1]):
                temp_num = in_list_to_sort[i + 1]
                in_list_to_sort[i + 1] = in_list_to_sort[i]
                in_list_to_sort[i] = temp_num

                list_is_sorted = False

            i += 1

    return in_list_to_sort

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

            while (in_list_to_sort[j] < in_list_to_sort[j - 1]):
                temp_num = in_list_to_sort[j - 1]
                in_list_to_sort[j] = in_list_to_sort[j - 1]
                in_list_to_sort[j - 1] = temp_num

                j -= 1

        i += 1

    return in_list_to_sort

# Main
unsorted_list = generate_random_numbers_list(20)

print "Original list of numbers        : ", unsorted_list

sorted_list = bubble_sort(unsorted_list)

print "Bubble sorted list of numbers   : ", sorted_list

sorted_list = insertion_sort(unsorted_list)

print "Insertion sorted list of numbers: ", sorted_list