import random
global guess
guess = random.randint(1,99)

def guess_number(guess):
    print(guess)
    response = input('>')
    if response == 'too high':
        guess -= 10
        print(guess)
        response = input('>')
        if response == 'too high' and guess > 10:
            guess -= 10
            guess_number(guess)
        elif response == 'too high' and guess < 10:
            guess -= 1
            print(guess)
            response = input('>')
        elif response == 'too low':
            guess_number(guess)
        elif response == 'yes':
            print('yay')
    elif response == 'too low':
        guess += 10
        print(guess)
        response = input('>')
        while response == 'too low':
            guess += 1
            print(guess)
        else:
            print('yay')
    elif response == 'yes':
        print('yay')
    else:
        print("I'm not sure what that means.")
        print('>')
        guess_number(guess)

print('Please think of a number 1-99.')
print('I will attempt to guess your number.')
print('If the number I guess is too high, please type "too high".\nIf the number I guess is too low, please print "too low".')
print('If I guess the number correctly, please type "yes".')

guess_number(guess)