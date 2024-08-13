'''
Q7: Write a program that takes a string and returns the most frequent character in it.
'''

'''
Input =  strings
logic = for loop with if statement
Output = print (most frequent character)
'''

#Defination : Most frequent character = character that appears the most number of times within a given string 

# Get user input
string = input("Enter the string ")

# Creates a dictionary
freq_chars = {}

# initializing the loop
for i in string:
    if i in freq_chars:
        freq_chars[i] += 1
    else:
        freq_chars[i] = 1

# Prtints each Frequest character in a dictionay
print(freq_chars)

# Prtints most Frequest character
print(max(freq_chars, key=freq_chars.get))