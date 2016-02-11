__author__ = 'ambli'

def camel_to_pothole(camel):
    """ (str) -> str
    Precondition: len(camel) >= 1 and camel[0].isalpha() and camel.isalnum()
    Return a new string with camel converted to the pothole case naming style.
    >>> camel_to_pothole('computerScience')
    'computer_science'
    >>> camel_to_pothole('numVowels30')
    'num_vowels_3_0'
    """

    i = 0
    pothole_string = ""

    while (i < len(camel)):
        if camel[i].islower():
            pothole_string += camel[i]
        else:
            pothole_string += "_"
            pothole_string += camel[i].lower()

        i += 1

    return pothole_string

# Main app
camel_string = "computerScience"
pothole_string = camel_to_pothole(camel_string)

print "%s coverted to: %s" % (camel_string, pothole_string)

camel_string = "numVowels30"
pothole_string = camel_to_pothole(camel_string)

print "%s coverted to: %s" % (camel_string, pothole_string)