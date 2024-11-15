# if statments : if statemtns are used to Check a Condition . If the condition is true, the code inside the if block runs. If the condition is false, it skips to the next part of the code.

print('If Statements')



b = 10
# the case where the condition is true 
if b > 1 : # Here you write the condition to check then ":"
    print('the condition is satisfied') # the statement will execute if the condition is satisfied

# the case where the condition is false :
if b > 100 : 
    print('this part of the code will not run ') # the statement will not execute 


# else : 
if b == 20:  
    print('true')  # Notice the indentation;
else:
    print("false")  # the code inside Else statement will execute if the first condition is not satisfied

# elif is used to handle multiple conditions
if b < 10:
    print('b is smaller than 10')
elif b > 10:
    print()  # Placeholder for when b is greater than 10


# All in one line
c = 30
print("true") if c == 20 else print("false")  # Note 1: Use this method only for short statements
                                              # Note 2: This method requires an else statement and does not accept elif
                                              
# note you can use multiple elif but only one esle 
 #handling two conditions
## the key words or , and , not , not , in 
# and : both conditions are true 
num = 10 
num2 = 20
if num >= 10 and num2>20:
    print('both conditions are true this message will be displayed')
    
if num < 10 and num2>20:
    print('one of the conditions isnt true this message wont be displayed ')

    
# or : one for the conditions are true 
if num < 10 or num2>20:
    print('one of the conditions true this message will be displayed')
          
# not : the oposite/reverse of the condition 
if not num==2 :
    print('the reverse condition is true is message will be displayed ')

# in : used the check if an element is in the set/list/group....

if 2 in [1,2,3,4]:
    print('2 is in the set so the condition is true and this message will display ')
    



# Loops
# Explanation: Loops is a way to repeat a block of code multiple times.


# For loop: iterates over a given range
print('For Loop')

# Range of numbers : 
for itera in range(10):  # itera will take the values 0, 1, 2, ..., up to n-1, where n is the range (10), so here 0 to 9
    print(itera)  # This loop will print the numbers from 0 to 9
# in this case the for loop will go through all the numbers from 0 to 9
#The loop variable:(like itera in the example) represents each number during the loop.




# Starting value in the range : if we want to specifie the starting value in our loop we do as follows :
print('Range of numbers starting from 1')
for i in range(1, 11): # 1 is starting value , 11 range value 
    print(i)  # This will print from 1 to 10

# Step value in the range
print('Step in range')
for i in range(1, 11, 2):  # The third parameter is the step: controls how much i changes in each iteration
    print(i)  # This will print 1, 3, 5, 7, 9

# Iterating over a string (loop with string )
print('Range of characters')
for char in "python":
    print(char)


# While loop: works similarly to the for loop but uses a condition instead of a range
print('While Loop')
i = 0
while i < 9:
    print(i)
    i += 1  # Always update the parameter to verifie (loop variable , i in this case ) to avoid an infinite loop


# Break and Continue
# Break: used to stop the loop (for and while) at a certain iteration
print('Break example')
for i in range(5):
    if i == 2: # when the condition is true the loop will stop the the program will move to the next section of the code 
        break
    print(i)

# Continue: used to skip an iteration (for and while)
print('Continue example')
for i in range(5):
    if i == 2: # when the condition is true the loop will skip the iteration 
        continue
    print(i)






