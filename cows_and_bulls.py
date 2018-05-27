import random
global number

number = str(random.randint(1000,9999))

print(number)

def cowbull():
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

print('Guess a number')

while not cowbull():
    print('Guess again!')