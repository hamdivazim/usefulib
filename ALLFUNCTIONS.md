# usefulib - All usefulibs

## reverse_string() by @hamdivazim
Reverses a string.

## loop_dict() by @hamdivazim
Allows you to loop through a dictionary while having access to its value, key and current loop index.
Example:
```
my_dict = {'a':1, 'b':2, 'c':3}

for key, val, i in loop_dict(my_dict):
    # Stuff here
```

## find_nth_root() by @hamdivazim
Returns the nth root of the number you provide.

## filter_by_string() by @hamdivazim
Filters a list based on whether elements contain a specific string.

## filter_by_condition() by @hamdivazim
Filters a list based on a specific condition.<br>
How to use:
condition property is a string. If you wanted to filter a list based on whether the element (suppose is going to be an integer) was even or not, you would:

```
lst = [0,1,2,3,4,5,6,7,8,9,10]

new_lst = usefulib.filter_by_condition(lst, "i % 2 == 0")
```
The variable `i` is the element.

## generate_random_string() by @hamdivazim
Generates a random string using ASCII chars, digits and special chars.

## generateUUID() by @hamdivazim
Generates a UUID using version 4 by default but you can choose.

## external_verbose_output() by @hamdivazim
If you are printing a lot of data, you can use this method to write the output to log file.
## get_hash() by @MKM12345
This takes a string as input, hashes it using the SHA-256 algorithm, and returns the hexadecimal representation of the hash value.
