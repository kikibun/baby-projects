import random

numlist = '1234567890'

def number_generator():
    number = ''
    for i in range(0,4):
        number += random.choice(numlist)
    print(number)
    return number

def cowbull(number):
    cow = 0
    bull = 0
    guess = str(input('> '))
    print(guess[0], number[0])
    for i in range(0,4):
        if guess[i] == number[i]:
            cow += 1
        elif guess[i] in number:
            bull += 1
    #print(guess)
    print(cow, 'cows, ', bull, 'bulls')

    if guess == number:
        print('You did it!')
        return True

random_number = number_generator()

print('Guess a number')

while not cowbull(random_number):
    print('Guess again!')