import math

EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.0, 0.0, 2)
    True
    >>> is_between(0, 1, 2)
    False
    """
   
    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
