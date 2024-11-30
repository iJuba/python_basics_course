# There are 3 main data types discussed here:

# 1. Lists: Can store all variable types
# Define a list
nbr_list = [1, 2, 3]
print(nbr_list)
print(type(nbr_list))

# A list can contain multiple variable types
multi_vars_list = ['strings', 123, False]
print(multi_vars_list)

# Using the constructor method
constr_list = list(['gdsc', 20114, True])
print(constr_list)

# Operations on lists:
# Access an element or a range of elements
print(nbr_list[0])  # First element
print(nbr_list[-1])  # Last element
print(nbr_list[1:2])  # Range (end index is excluded)

# Get the index of an element
print(nbr_list.index(3))

# Check the existence of an element in a list
print(2 in nbr_list)
print('hello' in nbr_list)

# Add an element to a list
# Using the append method
nbr_list.append('run')
print(nbr_list)

# Add multiple elements to the list
nbr_list.extend(['hello', 'world'])
print(nbr_list)

# Add a list to another list
str_list = ['hi', 'bye', 'hello']
str_list += nbr_list
print(str_list)

# Insert an element at a given position
nbr_list.insert(0, 'start')  # Insert at the beginning
print(nbr_list)

# Remove elements:
   # Remove by value
nbr_list.remove(2)  # Removes the first occurrence of 2
    # Remove by index
del nbr_list[2]  # Removes the element at index 2
print(nbr_list)

# Get the length of a list
print(len(nbr_list))

# Clear all elements in a list
nums = [1, 2, 3, 4, 56, 78]
nums.clear()
print(nums)

# Sort a list
nbr_list = [3, 1, 4, 2]
nbr_list.sort()
print(nbr_list)

# Sort in reverse order
nbr_list.sort(reverse=True)
print(nbr_list)


# 2. Sets: Similar to lists but do not allow duplicates
# Define a set
num_set = {1, 3, 2}
numbers = {1, 1, True, False, 0, 2}
print(num_set)  # Sets do not guarantee order
print(numbers)  # True is a duplicate of 1, and False is a duplicate of 0
print(type(numbers))
print(len(num_set))
print(len(numbers))

# Sets share some methods with lists, but elements cannot be accessed by index.


# 3. Tuples: Immutable (cannot be modified)
# Define a tuple
tupl = tuple((1, 2, 3))
tuple1 = ("hello", 22, True)

print(type(tupl))
print(isinstance(tuple1, tuple))

# Add elements to a tuple (requires converting to a list first)
tubl_list = list(tupl)
tubl_list.append('dave')
tubl_list.extend(['hello', True])
tupl = tuple(tubl_list)
print(tupl)

# Unpacking a tuple into variables
(var1, var2, *var3) = tupl
print(var1)
print(var2)
print(var3)

# Count occurrences of a certain element
print(tupl.count(2))


# 4. Dictionaries: Key-value pairs
# Define a dictionary
music = {
    "lyrics": "by dave",
    "instrument": "by ellys",
    "edit": "by person"
}
print(music)

# Using the constructor method
band = dict(guitar="jake", violin="ellys")
print(band)

# Access items
print(band["guitar"])  # Direct access
print(band.get("guitar"))  # Using get method

# Get all keys
print(band.keys())

# Get all key-value pairs as tuples
print(band.items())

# Check for existence of keys
print("guitar" in band)
print("piano" in band)

# Add or change values
band["guitar"] = "alex"  # Change value
band.update({"piano": "brad"})  # Add new key-value pair
print(band)

# Remove items
print(band.pop("violin"))  # Remove by key
print(band.popitem())  # Remove the last inserted key-value pair
print(band)

# Clear and delete a dictionary
music = dict(lyric="none", instru="jazz")
music.clear()
print(music)

# Copy a dictionary
band2 = band.copy()
band2.update({'drums': 'mike'})
print(band)
print(band2)


# Nested dictionaries
member1 = {
    "name": "ellys",
    "instrument": "piano"
}
member2 = {
    "name": "dave",
    "instrument": "drums"
}
the_band = {
    "first": member1,
    "second": member2
}
print(the_band)
print(the_band["first"]["name"])


# Sets - Additional operations
# Merge two sets
set1 = {1, 2, 3}
set2 = {4, 3, 6}
set3 = set1.union(set2)
print(set3)

# Intersection (common elements)
set4 = set1.intersection(set2)
print(set4)

# Symmetric difference (elements not in both sets)
set2.symmetric_difference_update(set1)
print(set2)
