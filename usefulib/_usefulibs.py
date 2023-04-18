"""
usefulib v1.0
Copyright Hamd Waseem (https://github.com/hamdivazim) under the GNU Public License 3.0.

https://github.com/hamdivazim/usefulib

Add your useful method here if you are contributing. Remember to add unit tests in tests.py :)
"""

def reverse_string(string):
    """ @hamdivazim - Reverses a string. """

    return string[::-1]

def loop_dict(dictionary):
    """ 
    @hamdivazim - Allows you to loop through a dictionary while having access to its value, key and current index.

    Example:

    ```
    my_dict = {'a':1, 'b':2, 'c':3}

    for key, val, i in loop_dict(my_dict):
        # Stuff here
    ```
    """

    result = []
    i = 0

    for key in dictionary.keys():
        result += (key, dictionary[key], i)

        i += 1

    return result

def find_nth_root(num, n):
    """ @hamdivazim - Returns the nth root of a number you provide. """

    return num ** (1 / n)

def filter_by_string(lst, string):
    """ 
    @hamdivazim - Filters a list based on whether elements contain a specific string.
    Probably best used when filtering by a search query.
    """

    result = []

    for element in lst:
        try:
            if string in element:
                result += element
        except TypeError:
            raise TypeError("A non-string value was found while using the usefulib.filter_by_string method. Maybe try using filter_by_condition?")
        
    return result

def filter_by_condition(lst, condition: str):
    """
    @hamdivazim - Filters a list based on a specific condition.

    How to use:
    condition property is a string. If you wanted to filter a list based on whether the element (suppose is going to be an integer) was even or not, you would:

    ```
    lst = [0,1,2,3,4,5,6,7,8,9,10]

    new_lst = usefulib.filter_by_condition(lst, "i % 2 == 0")
    ```

    The variable `i` is the element.
    """

    result = []

    for i in lst:
        exec(f"if({condition}):result+=i")

    return result