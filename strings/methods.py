import pyperclip

spam = 'hello world!'
print(spam.upper())
print(spam)

print(spam.islower())
print(spam.isupper())

# check for string characters
print('hello'.isalpha())
print('hello123'.isalnum())
print('123'.isdecimal())
print('     '.isspace())
print('This Is Title Case'.istitle())

# startswith and endswith
print('Hello world'.startswith('Hello'))
print('Hello world'.startswith('ello'))
print('Hello world'.endswith('world'))
print('Hello world'.endswith('wor'))

# join
print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))
print('\n\n'.join(['cats', 'rats', 'bats']))

# split
print('My name is ryan'.split())
print('My name is ryan'.split('n'))

# just - add padding to begin/end
print('hello'.rjust(10))
print('hello'.ljust(10))
print('hello'.rjust(20, '*'))
print('hello'.ljust(25, '-'))
print('hello'.center(25, '-'))
print('whoooooooooo'.center(25, '-'))

# strip - remove chars from begin/end
print('     hello     '.strip())
print('     hello     '.rstrip())
print('     hello     '.lstrip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

# replace
print('Hello there!'.replace('e', 'XYZ'))

# pyperclip has copy and paste functions
pyperclip.copy('hello!!!!!!!!!')
print(pyperclip.paste())


# string formatting
name = 'Alice'
place = 'Main street'
time = '6 pm'
food = 'pizza'
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))