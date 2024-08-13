'''
Q5: Write a program that takes a string and returns True if it is a palindrome, False otherwise
'''

'''
Input = string
logic = reversed_string == string
Output = print (True or False)
'''

#Get user input
word = input("Enter the string to check whether it is plaindrome or not? ")

# Reversing the string
reversed_word = word[::-1]

# Checks for palindrome
if reversed_word == word:
    print("True")
else:
    print("False")