'''
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
'''

def phone(int):
    if len(int) == 10:
        return f'Your number is {int}'
    return 'wrong number'

print(phone('0664130589'))
print(phone('1111'))