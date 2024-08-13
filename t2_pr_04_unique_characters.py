'''
Q4: Write a program that takes a string and returns the the number of unique characters in it.
'''

'''
Input =  strings
logic = for loop with if statement
Output = print (number of unique characters)
'''

#Defination : unique characters = characters that appear only once within that string

# Get user input
string = input("Enter the string: ")

unique_characters = 0

# checks for unique characters
for i in string:
    if string.count(i) == 1: 
        unique_characters = unique_characters + 1

# prints number of unique characters
print(f"The number of unique characters are : {unique_characters} ")   
