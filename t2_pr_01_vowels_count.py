'''
Q1: Write a Python program to calculate the total number of Vowels and count each
individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"?
'''
'''
Input = string
logic = for loop with elif ladder
Output = print (vowels count and total number of vowels)
'''

# This is the given string
string = "Guvi Geeks Network Private Limited"

# Modifies the string to lower case
string = string.lower()

vowel_a = 0
vowel_e = 0
vowel_i = 0
vowel_o = 0
vowel_u = 0

# Counts each and every vowel in string 
for char in string:
    if char == 'a':
        vowel_a +=1
    elif char == 'e':
        vowel_e +=1
    elif char == 'i':
        vowel_i +=1
    elif char == 'o':
        vowel_o +=1
    elif char == 'u':
        vowel_u +=1

# Calculates the total number of vowels
total_vowels = vowel_a + vowel_e + vowel_i + vowel_o + vowel_u

# Displayis Total vowel count
print(f"The total number vowels is {total_vowels} ")

# Displays individual vowel count
print(f"The total number of vowel 'A' is {vowel_a}")
print(f"The total number of vowel 'E' is {vowel_e}")
print(f"The total number of vowel 'I' is {vowel_i}")
print(f"The total number of vowel 'O' is {vowel_o}")
print(f"The total number of vowel 'U' is {vowel_u}")