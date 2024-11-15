#in this chapter we will take a look to input methodes and deffirent ways of output 

print('a' + 'b', 'c')  # Concatenates 'a' and 'b', then prints 'c'

# to get data from the user use the input method
input_msg = input("Enter something: ")
input_number = input('Enter a number: ')
print(type(input_msg)) # notice that the input is always a str 
print(type(input_number))

# to convert the input use the constructor methods
var1 = int(input_number)
print(type(var1))

# different ways of output

coins = 45
person = 'juba'

## easy way to concatenate strings
print("\nThe person \"" + person + "\" has " + str(coins) + " coins.")

## the old way using placeholders like in C
print("\nThe person \"%s\" has %s coins." % (person, coins))

## using the format method
print('\nThe person \"{}\" has {} coins.'.format(person, coins))

# numbered placeholders in the format method
print('\nThe person {1} has not {0} coins.'.format(coins, person))

# shortcuts in the format method
print('\nThe person {var1} has {var2} coins.\n'.format(var1=person, var2=coins))

############### f-strings
# add 'f' before the string 
## its recomanded to always use the f stings for the outputs for is easy readability and syntax

print(f"The person {person} has {coins} coins...")
