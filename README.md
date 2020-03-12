# Testing Example

Small project demonstrating:

* Unit testing
* Project structure
* Code style
* Property based testing

## Motivating example

Consider a simple word game where players make a word from letters available to them.

## Resources

Why do we unit test?

Code style PEP-8, docstrings

What is property based testing (advanced)

## Installation

This project has a `setup.py` file which allows it to be installed with pip.

To do that navigate to the project directory and call:

```
pip install -e .
```

Here `-e` dynamically links the installed package to the source files,
so updates to the source code will be reflected when the module is imported.

## Running tests

Options:

* From an IDE
* From the command line with `pytest`
* From the command line with `python setup.py test`
   