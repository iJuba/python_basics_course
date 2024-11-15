#A function is a block of code designed to perform a specific task. You can use the function whenever needed, allowing you to avoid repeating the same code multiple times.

# Defining a function
def hello():
    print('hello')

# calling the function \ executing the code definied above (code in the function)
hello()



# functions with a given input :
def sums(value):  
    result = 0
    for i in range(value):
        result += i
    return result  # return result means that this function will give the result of the var result 


 
zero_to_10 = sums(10)

print(f"zero_to_10: {zero_to_10}")


# Function with modification of a variable
def minus5(var):
    var -= 10
    return var

var = 15
var_minus = minus5(var)
print(f"Variable after using the function: {var}")
print(f"Return of minus function: {var_minus}")

# Notice that the variable 'var' did not change even though we performed an operation on it in the function.
# This is because a function operates on a copy of the data by default and does not change the original value.

# Function with default parameters
def sums(end_value, start_value=0):  # 0 is a default value; default values must be the last parameters
    result = 0
    for i in range(start_value, end_value):
        result += i
    return result

one_to_10 = sums(10, 1) 
print(f"one_to_10: {one_to_10}")


# Built-in functions and methods
# Built-in functions: These are functions available in the base Python library that return a value

# Example: 'type' function, which we used earlier, is a built-in function
msg = 'gdsc'
type_var = type(msg)
print(type_var)


# Methods: These are functions that are called on objects using dot notation and typically modify or interact with the data
# Example
var2 = msg.upper()
print(var2)



# Difference between a function and a method:
# - A method is a function that is bound to an object (specific to a class).
# - A function can be used independently of an object.
