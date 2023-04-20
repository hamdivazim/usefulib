from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'A collection of assorted methods to make small tasks easier..'
LONG_DESCRIPTION = """
# usefulib v1.0
A useful library for Python with assorted functions to make small tasks easier.

## How to install
Install with pip in your terminal, making sure Python is added to PATH:
```
$ pip install usefulib
```

## How to use
All you need to do is import the package, and all usefulibs that you may want will come along with it! As an example:
```python
import usefulib

a_string = "abcdef123456"
reverse_string = usefulib.reverse_string(a_string)
```

## What can it do?
usefulib is open-source and can be contributed to by anyone. Therefore, it offers a lot of simple functions to make writing code easier and quicker. A complete list of all fuctions usefulib provides can be found [here](https://github.com/hamdivazim/usefulib/blob/main/ALLFUNCTIONS.md).

## Can I contribute?
Want to contribute? You rock! Before you do, make sure to read the [contributing guidelines](https://github.com/hamdivazim/usefulib/blob/main/CONTRIBUTING.md) and you should have your PR merged!
"""

# Setting up
setup(
    name="usefulib",
    version=VERSION,
    author="Hamdi Vazim",
    author_email="<codingboy.cw@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'useful', 'usefulib', 'collection'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)