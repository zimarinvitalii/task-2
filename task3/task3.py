'''
Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case,
e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
'''




print('Ваше имя')
name = str(input())
if name == 'Виталий':
    print('True')
else:
    print('Wrong name')