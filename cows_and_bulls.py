import random

numlist = ['1', '2', '3', '4', '5', '6', '7', '8','9', '0']

def number_generator():
    number = ''
    for i in range(0,4):
        new_number = random.choice(numlist)
        numlist.remove(new_number)
        number += new_number
    return number

def cowbull(number):
    cow = 0
    bull = 0
    guess = str(input('> '))
    if guess == "HACK":
        print(number)
    #print(guess[0], number[0])
    for i in range(0,4):
        if guess[i] == number[i]:
            cow += 1
        #elif guess[i] in number:
         #   bull += 1
        elif number[i] in guess:
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