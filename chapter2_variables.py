# variable is a value that can change, depending on conditions or on information passed to the program.

# Define a variable (var stands for variable)
# A variable in Python is defined by directly assigning it a value
var = 13
print(var)
# Variable types mainly there is 4 var types : integers , floats , booleans and string

    # Integers and floats

int_var = 12  # int (integer) variables are finite variable numbers  that can be positive or negative
float_var = 12.45  # floats are variables that hold real numbers 
print(int_var)
print(float_var)
        # Math methods
a = 24 / 5  # This is a devision operation that returns a real number [float]
print(a)
b = 24 // 5  # The “//” operator is used to return the closest integer value
print(b)
c = 24 % 5  # The remainder of the division
print(c)
d = round(24 / 5)  # The result will be rounded
print(d)

'''
We'll talk more about math complexe operations later in the course

'''

    # Boolean (bool) :A Boolean is a type of variable that holds one of two values: either True or False (note: the T and F must be written in capital letters)
    # the bool var is used generally in condition 
bool_var = True
bool_var2 = False
print(bool_var)
print(bool_var2)

    # String: a set of characters
str_var = 'gdsc'
print(str_var)




# To get the type of a variable, use the type function
print(type(int_var))
print(type(float_var))
print(type(bool_var))

# Check the type of a variable
print(isinstance(int_var, str))  # Takes two arguments: the variable and the verified type; returns a boolean
print(isinstance(int_var, int))

# Constructor methods : this is an other methode for defining variables 
bool_constr = bool(True)
int_constr = int(123)
float_constr = float(12.45)

# Using constructor methods to convert between types
numbr = 123
print(numbr)
print(type(numbr))
str_numbr = str(numbr)
print(str_numbr)
print(type(str_numbr))  # Corrected this to show the type of str_numbr, not numbr


## there is other types of variables that arent usely used :
    # none type : its a variable without a type  
var = None 
    # complexe type: Numbers with a real and imaginary part
complex_number = 2 + 3j    