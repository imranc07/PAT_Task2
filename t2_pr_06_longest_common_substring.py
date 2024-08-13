'''
Q6: Write a program that takes two strings and returns the longest common substring between them.
'''

'''
Input =  2 strings
logic = 2D list, nested for loop with range function
Output = print (longest common substring)
'''


# Define input strings
input_string1 = "GuviGeeksNetworkPrivateLimited"
input_string2 = "GreatNetwork"

# Get lengths of input strings
m = len(input_string1)
n = len(input_string2)

# Initialize a 2D list for dynamic programming
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Initialize variables to store the maximum length of common substring
max_length = 0
end_index = 0

# Loop through the characters of both strings
for i in range(1, m + 1):
    for j in range(1, n + 1):
        # If characters at current positions match
        if input_string1[i - 1] == input_string2[j - 1]:
            # Update the length of common substring
            dp[i][j] = dp[i - 1][j - 1] + 1
            # Update maximum length and ending index of the common substring
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_index = i - 1  

# Extract the longest common substring using the ending index and its length
longest_substring = input_string1[end_index - max_length + 1:end_index + 1] 

# Print the longest common substring
print(f"The longest subtring is {longest_substring}")