# Contributing to usefulib
Want to contribute? You rock! But first, read these contributing guidelines to ensure your pull request is merged!

## Contents
- [Creating a usefulib](#creating-a-usefulib)
  - [Typing your idea up](#typing-your-idea-up)
  - [Example of a usefulib](#example-of-a-usefulib)
- [Writing tests](#writing-tests)
  - [Creating a test](#creating-a-test)
  - [Example of a test](#example-of-a-test)
 - [Opening A Pull Request](#opening-a-pull-request)

## Creating a usefulib
First, you need to come up with an idea for a usefulib. You need to try and keep it short but still make a task that would've taken more than two lines into one line. Make sure your idea is original by checking that someone hasn't already used your idea [here](https://github.com/hamdivazim/usefulib/blob/main/ALLFUNCTIONS.md). If you need inspriation, take a look at some [ideas from the community](https://github.com/hamdivazim/usefulib/labels/usefulib-idea). Then, it's time to get coding!
### Typing your idea up
Before getting started, remember to fork and clone this repository (if this is your first time, [follow this guide](https://github.com/firstcontributions/first-contributions)). Then open `usefulib/_usefulibs.py` in your code editor. If your script needs any kind of setup (for example imports) then put them at the top here:
```python
""" Setup - add any setup scripts here remembering to put the function(s) they are for. """

# Put setup stuff here.

""""""
```
You should also put which usefulib(s) the setup is for:
```python
import setup_stuff # the_usefulib_this_is_for()
```
If you are importing anything from pip, mention the library in your pull request.
###
Then, write your usefulib! Name it anything you want (of course related to what you are adding) and get coding 😄. At the top of your usefulib, you should  write a multiline comment and type your username on GitHub, and what the usefulib does. As an example:
```python
def my_awesome_usefulib():
    """ @hamdivazim - A very awesome description of this awesome usefulib! """

    # Code goes here
```
If your usefulib is hard to understand without an example, make sure you include one.

### Example of a usefulib
```python
def reverse_string(string):
    """ @hamdivazim - Reverses a string. """

    return string[::-1]
```
When you have added your usefulib, remember to add it to the list of [all usefulibs](https://github.com/hamdivazim/usefulib/blob/main/ALLFUNCTIONS.md).

## Writing tests
Now that you've written your usefulib, you should test it! For this, naviagte to `tests.py` in the same directory. **Note:** this requires that you know how to write good unit tests in Python using `unittest`. If you don't know how to, watch this [awesome tutorial](https://www.youtube.com/watch?v=6tNS--WetLI) by Corey Schafer!
### Creating a test
In `tests.py` there will be a class called `TestUsefulibs` with numerous methods all beginning with 'test_' followed by the name of the usefulib they're for (apart from `setUp()` but we'll get to that later). This is how you should name your test. For example, this is what you would name a test for `reverse_string()`:
```python
def test_reverse_string(self):
    # Tests here
```
Now you should put your username in triple quotes at the top like this: `""" @hamdivazim """`. Then, write some tests! You will need to use the assert methods found in the [full list on Python's documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug). If your tests need any form of setup, write those in the `setUp()` method.
###
If you are generating external files in these tests, make sure these are written into the `temp_data/` directory. If you need one, an example is in the `test_external_verbose_output()` test.
### Example of a test
```python
def test_reverse_string(self):
    """ @hamdivazim """

    self.assertEqual(reverse_string("abc"), "cba")
    self.assertEqual(reverse_string("123abcdef456"), "654fedcba321")
```

## Opening a Pull Request
When your usefulib and tests are ready, it's time to contribute! Simply open a pull request, remembering to mention what you have added, whether you were able to add tests or not and anything else you think I need to know. Another note, do NOT change `setup.py` or your pull request will not be merged. Just for reference, your changes may not appear on the pip package immediately after it is merged. You may have to wait for a couple days.

**NOTE**: The [code of conduct](https://github.com/hamdivazim/usefulib/blob/main/CODE_OF_CONDUCT.md) must be followed during your contributions to usefulib.
