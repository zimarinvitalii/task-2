'''
Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
'''

import random

print('угадай число от 1 до 10')
num = int(input("Ваше число: "))
computer = random.randint(1, 10)
if num >= 11 or num == 0:
    print('Wrong number')
elif computer > num:
    print(f'Too low, I chose {computer} ')
elif computer < num:
    print(f'Too high, I chose {computer}')
else:
    print('Good')