#string operations :

# Concatenate strings: use the + operator

name = 'ibaghouchene'
first_name = ' juba'
full_name = name + first_name  

print('The value of name: ' + name)
print('The value of first_name: ' + first_name)
print('The value of full_name: ' + full_name)

# Another example

name_gdcs = "gdsc"
full_name_gdcs = name_gdcs + ' club ensta'
print('The value of name_gdcs: ' + name_gdcs)
print('The value of full_name_gdcs: ' + full_name_gdcs)

# Get the length of the string : use the len function

len_name = len(name_gdcs)
print(len_name)

# Writing operations
print(name_gdcs.lower()) 
print(name_gdcs.upper())
print(name_gdcs.title())

# Get characters from string
    # Strings in Python are indexed from 0 to n

char_1 = name_gdcs[0]  # Get the first character
print(char_1)
char_last = name_gdcs[3]  # If the last index is unknown, use -1 to get the last character
char_last_method2 = name_gdcs[-1]
print("Value of char_last: " + char_last)
print("The value of char_last_method2: " + char_last_method2)

# Get a range of characters (slicing)
print('The 2 characters in the middle of gdsc: ' + name_gdcs[1:-1])  # Note: the last index isn't included
print('The first 2 characters of gdsc: ' + name_gdcs[:2])  # Note: the last index isn't included
print('The last 2 characters of gdsc: ' + name_gdcs[2:])  # No last index means it includes everything to the end
mystr = 'hello world'
print('the '+mystr[0:-1:2]) # the here is called the step which means it will take every second character within the range specified

# Replace a word or character
print(full_name_gdcs)
full_name_gdcs = full_name_gdcs.replace("gdsc", "light")
print(full_name_gdcs)

# Use \n to move to the next line and \t to add a tab space
space_line = ' hello\tworld\n*** '
print(space_line)

# Escaping special/reserved characters
# Use \ before the character
chr_special = 'I\'m a student in ensta'
print(chr_special)
