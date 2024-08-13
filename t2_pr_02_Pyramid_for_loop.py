'''
Q2: Create a Pyramid of numbers from 1 to 20 using for loop?
'''

'''
Input = integer
logic = for loop with range function
Output = print (pyramid of numbers from 1 to 20)
'''

# Defining the last number for creatng pyramid
n=int(20)

# Inializing for loop
for i in range(n):
      for j in range(n-i-1):#(here i value:start,stop,step:increment /decrement i value,here we are reversing the index of the column)
        print(" ",end="")
      for j in range(i+1):
        print(j+1,end=" ")
      print()      