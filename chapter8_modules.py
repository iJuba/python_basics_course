
# 1. What is a module?
# A module is a collection of functions and methods that may not be available in the base Python library.
# Modules can be accessed by importing them into your code.

# Example: Importing the math module
import math

# Using a function from the math module
print(math.pi)  # Outputs the value of pi


# 2. Creating an abbreviation for a module
import math as mt  # 'mt' is now an alias for math
print(mt.pi)       # Same output as math.pi

# Note: You only need to import a module once per file.


# 3. Viewing the contents of a module
# Use 'dir()' to see a list of all functions and constants within a module.
print(dir(math))

# For a more readable output, you can loop through the items:
for item in dir(math):
    print(item)


# Examples of Standard Python Modules
# 1. The random module
import random as rd  # random can be used to generate random numbers, characters, etc.

# Generating a random integer between 1 and 9
print(rd.randint(1, 9))

# Selecting a random character from a given string
print(rd.choice('abcd'))


# 4. Installing new modules with pip
# You can use pip (Python's package installer) to install additional modules not included in the standard library.  

# Example command to install numpy:
# py -m pip install numpy [write this in the command line prompt]

# To install a specific version of a package, you can specify the version:
# py -m pip install numpy==1.21.0

# To view all installed packages, use:
# py -m pip list

# To learn more about a module, you can read its documentation online in its officiale site  or use the built-in help function in Python.
# Example on how to use the help function : help(math)
