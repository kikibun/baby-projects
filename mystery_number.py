import random
global guess, high_count, low_count
guess = random.randint(1,99)
high_count = 0
low_count = 0

def guess_number(guess, high_count, low_count):
    print(guess)
    print('high count is', high_count)
    print('low count is', low_count)
    response = input('>')
    while response == 'too high':
        guess -= 10
        high_count += 1
        guess_number(guess, high_count, low_count)
    if response == 'too low' and high_count >=1:
        while response == 'too low':
            guess += 1
            guess_number(guess, high_count, low_count)
        else:
            guess(guess_number, high_count, low_count)
    while response == 'too low':
        low_count += 1
        guess += 10
        guess_number(guess, high_count, low_count)
    if response == 'too high' and low_count >= 1:
        while response == 'too high':
            guess -= 1
            guess_number(guess, high_count, low_count)
        else:
            guess(guess_number, high_count, low_count)
    elif response == 'yes':
        print('yay')
        exit(0)
    else:
        print("I'm not sure what that means.")
        print('>')
        guess_number(guess, high_count, low_count)

print('Please think of a number 1-99.')
print('I will attempt to guess your number.')
print('If the number I guess is too high, please type "too high".\nIf the number I guess is too low, please print "too low".')
print('If I guess the number correctly, please type "yes".')

guess_number(guess, high_count, low_count)