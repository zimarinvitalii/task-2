'''
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
'''

import random

numbers = []
i = 0
while i < 10:
    numbers.append(random.randint (1, 10))
    i += 1
print(f'random numbers are: {numbers}')
print(f'the maximum number is: {max(numbers)}')