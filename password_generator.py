import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
spec_chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()<>?/'

length = int(input('Length of password: '))
special_char = input('Special characters Y/N: ')

for i in range(3):
    if special_char.lower() == 'y':
        password = ''
        for i in range(length):
           password += random.choice(spec_chars)
        print(password)
    else:
        password = ''
        for i in range(length):
           password += random.choice(chars)
        print(password)