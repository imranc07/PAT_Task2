'''
Q3: Write a program that takes a string and returns a new string with all the vowels removed?
'''
'''
Input = string
logic = list of vowels, for loop and str.replace()
Output = print (string without vowels)
'''

# Get user input
string = input("Enter the string: ")

# Vowels list
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Checks vowels in string
for i in vowels:
    string = string.replace(i, "") # replaces the vowels present in string

# Prints the string
print(string)