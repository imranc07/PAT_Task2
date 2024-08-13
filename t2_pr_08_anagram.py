'''
Q8: Write a program that takes a string and returns True if 
it is an anagram of another string, False otherwise.
'''
'''
Input =  2 strings
logic = sorted(), string.lower() and for loop
Output = print (Number of words in string)
'''

#Get user input
word1 = input("Enter the First string:  ")
word2 = input("Enter the Second string:  ")

# sorts and converts string into lower case
word1 = sorted(word1.lower())
word2 = sorted(word2.lower())

# Checks if both string matches
if word1 == word2:
    print("True")
else:
    print("False")