__author__ = 'ambli'

def mystery(L):
    """ (list of str) -> str
    >>> mystery( )
    'zz'
    >>> mystery( )
    'acdfgi'
    """
    result = ''
    for item in L:
        result = result + item[0] + item[-1]

    return result

# Test
print mystery(["ac", "df", "gi"])