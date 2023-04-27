from setuptools import setup, find_packages

VERSION = '1.0.4'
DESCRIPTION = 'A collection of assorted methods to make small tasks easier.'
LONG_DESCRIPTION = """
<div align="center">
  <img src="https://github.com/hamdivazim/usefulib/raw/main/logo.png">
</div>
<a style="display:inline;" href="#"><img src="https://img.shields.io/badge/Python- >= 2.7 -blue?style=plastic.svg" alt="python versions" /></a>
<a style="display:inline;" href="#"><img src="https://badge.fury.io/py/usefulib.svg" alt="pypi version" /></a>
<a style="display:inline;" href="#"><img src="https://img.shields.io/badge/first timer-friendly-4DC71F?style=plastic.svg" alt="first timer friendly" /></a>
<a style="display:inline;" href="https://github.com/hamdivazim/usefulib/labels/usefulib-idea"><img src="https://img.shields.io/github/issues-raw/hamdivazim/usefulib/usefulib-idea?color=4DC71F&label=usefulib%20ideas" alt="usefulib ideas" /></a>
<a style="display:inline;" href="#"><img src="https://img.shields.io/badge/tests- all passing -4DC71F?style=plastic.svg" alt="usefulib ideas" /></a>



<h1>usefulib v1.0.4</h1>
A useful library for Python with <em>a lot</em> of assorted functions to make numerous small tasks easier.

### GitHub Page: https://github.com/hamdivazim/usefulib

## How to install
Install with pip in your terminal, making sure Python is added to PATH:
```
$ pip install usefulib
```
Alternatively, you can use the git URL to do the same.
```
$ pip install "git+https://github.com/hamdivazim/usefulib.git@pip-install#egg=usefulib"
```

## How to use
All you need to do is import the package, and all usefulibs that you may want will come along with it! As an example:
```python
import usefulib

a_string = "abcdef123456"
reverse_string = usefulib.reverse_string(a_string)
```
If all you need is one usefulib:
```python
from usefulib import reverse_string

a_string = "abcdef123456"
reverse_string = reverse_string(a_string)
```

## What can it do?
As an open-source library and can be contributed to by anyone, it offers a lot of simple functions to make writing code easier and quicker. A complete list of all usefulibs that are available can be found [here](https://github.com/hamdivazim/usefulib/blob/main/ALLFUNCTIONS.md).

## Support usefulib
usefulib is full of contributions from the community! We're beginner-friendly here, so read the [contributing guidelines](https://github.com/hamdivazim/usefulib/blob/main/CONTRIBUTING.md) and give us your best usefulibs 😃!

## License
usefulib is licensed under the [GNU General Public License v3.0](https://github.com/hamdivazim/usefulib/blob/main/LICENSE).

"""

# Setting up
setup(
    name="usefulib",
    version=VERSION,
    author="Hamd Waseem",
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