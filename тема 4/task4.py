'''
Write a program that asks the answer for a mathematical expression,
checks whether the user is right or wrong, and then responds with a message accordingly.
'''

import random
import operator

def askQuestion():
    answer = randomCalc()
    guess = float(input())
    return guess == answer

def randomCalc():
    ops = {
    '+':    operator.add,
    '-':    operator.sub,
    '*':    operator.mul,
    '/':    operator.truediv
    }
    num1 = random.randint(0,11)
    num2 = random.randint(1,11)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print(f'What is {num1} {op} {num2}?\n')
    return answer
    print(score)

def quiz():

    print('Welcome. This is a 10 question math quiz\n')
    score = 0
    times = 0
    while times < 9:
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!\n')
            print(score)
            times += 1
        elif not correct:
            times += 1
            print('Incorrect!\n')
            print(score)
    return print(f'Your score was {score}/10')



quiz()
askQuestion()
randomCalc()
