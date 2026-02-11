import random

letters = list('abcdefghijklmnopqrstuvwxyz')
numbers = list(range(10))
special_char = list('!@#$%^&*()_+-=')

print('Welcome to PyPassword Generator')

number_of_letters = int(input('How many letters do you want in a password?\n'))
number_of_numbers = int(input('How many numbers do you want in a password?\n'))
number_of_splchar = int(input('How many spl. chars do you want in a password?\n'))

password = []
for _ in range(number_of_letters):
    password.append(random.choice(letters))
for _ in range(number_of_numbers):
    password.append(str(random.choice(numbers)))
for _ in range(number_of_splchar):
    password.append(random.choice(special_char))

print('Easy Password: ', ''.join(password))

random.shuffle(password)
print('Hard Password: ', ''.join(password))