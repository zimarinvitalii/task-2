'''
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”
'''

name = str(input('What is your name? '))
age = int(input('How old are you?'))

print(f'Hello {name}, on your next birthday you’ll be {age+1} years')