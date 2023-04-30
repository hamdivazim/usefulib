"""
usefulib v1.0.4
Copyright Hamd Waseem (https://github.com/hamdivazim) under the GNU Public License 3.0.

https://github.com/hamdivazim/usefulib

Add your useful method here if you are contributing. Remember to add unit tests in tests.py :)
"""

""" Setup - add any setup scripts here remembering to put the function(s) they are for. """

import random # generate_random_string()
import string # generate_random_string()
import uuid # generateUUID()
import os # external_verbose_output()
import hashlib # get_hash()

""""""

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
        result.append((key, dictionary[key], i))

        i += 1

    return result

def find_nth_root(num, n):
    """ @hamdivazim - Returns the nth root of a number you provide. """

    if num < 0:
        raise ValueError("Cannot get root of a negative number.")

    return num ** (1 / n)

def filter_by_string(lst, stri):
    """ 
    @hamdivazim - Filters a list based on whether elements contain a specific string.
    Probably best used when filtering by a search query.
    """

    try:
        result = [x for x in lst if stri in x]

        return result
    except TypeError:
        raise TypeError("A non-string value was found while filtering. Maybe try using filter_by_condition()?")

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
        exec(f"if({condition}):result.append(i)")

    return result

def generate_random_string(word_length=18):
    """ @hamdivazim - generates a random string using ASCII chars, digits and special chars. """

    components = [string.ascii_letters, string.digits, "!@#$%&"]

    chars = []

    for clist in components:
        for item in clist:
            chars.append(item)

    result = []

    for i in range(word_length):
        rchar = random.choice(chars)
        result.append(rchar)

    return "".join(result)

def generateUUID(version=4):
    """ @hamdivazim - generates a UUID using version 4 by default but you can choose. """

    if version < 1 or version > 5:
        raise ValueError(f"{version} is not a valid UUID version number (valid values are 1-5).")
    else:
        if version == 1:
            return uuid.uuid1()
        elif version == 2:
            return uuid.uuid2()
        elif version == 3:
            return uuid.uuid3()
        elif version == 4:
            return uuid.uuid4()
        elif version == 5:
            return uuid.uuid5()
        
def external_verbose_output(data, path="data.log"):
    """ @hamdivazim - if you are printing a lot of data, you can use this method to write the output to log file. """

    if not os.path.exists(path):
        open(path, "x").close()

    with open(path, "w") as f:
        f.write("# Logged by usefulibs.external_verbose_output()\n\n")
        f.write(data)

def get_hash(string):
    """
    @MKM12345 + @hamdivazim - This function takes a string as input, hashes it using the SHA-256 algorithm, and returns the hexadecimal representation of the hash value. Useful for developers that want to store strings without actually having to store them.
    """

    if not isinstance(string, str):
        raise TypeError("get_hash() cannot get the hash of a non-string.")

    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def denary_to_ternary(n):
    """ @AtomicCodeLegend - Converts from denary to ternary base 3 """
    
    res = 0

    if n == 0:
        res = '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    res= ''.join(reversed(nums))
def calculate_fibonacci(n):
    """
    @TheCodingLedendofTheNether + MKM12345 - Returns the requested nth number in the Fibonacci sequence.
    """
    sys.setrecursionlimit(10**6) 
    if n <= 1:
        return n
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
def is_palindrome(s):
    """
    @TheCodingLedendofTheNether - Checks if a string is a palindrome using a numpy array.
    """
    a = numpy.array(list(s.lower()))
    a = a[numpy.char.isalnum(a)]
    return numpy.array_equal(a, a[::-1]) 
    return int(res)

    return int(res)
def convert_base():
    """@ShadowStrike-Atomiser - Converts a number from one base to another"""
    from_base = int(input("Type a base:"))
    to_base = int(input("Type another base (2-16): "))
    num = input("Type a number in base " + str(from_base) + ": ")

    base_10_num = 0
    power = 0
    for digit in num[::-1]:
        if digit.isdigit():
            base_10_num += int(digit) * (from_base ** power)
        else:
            base_10_num += (ord(digit.upper()) - 55) * (from_base ** power)
        power += 1

    new_num = ""
    while base_10_num > 0:
        digit = base_10_num % to_base
        if digit < 10:
            new_num = str(digit) + new_num
        else:
            new_num = chr(ord('A') + digit - 10) + new_num
        base_10_num //= to_base
    print("The number in base " + str(to_base) + " is:", new_num)
