# This is a number guessing game

import random

print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

randNum = random.randint(1, 20)

print('DEBUG: Secret number is ' + str(randNum))

# guessMax = 6
# print('Take a guess.')
# guess = int(input())
# guessCount = 1
#
# while guess != randNum and guessCount < guessMax:
#     if guess < randNum:
#         print('Your guess is too low.')
#     else:
#         print('Your guess is too high')
#     print('Take a guess')
#     guessCount += 1
#     guess = int(input())
#
# if guess == randNum:
#     print('Great job, ' + name + '! You guessed my number in ' + str(guessCount) + ' guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(randNum))

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < randNum:
        print('Your guess is too low.')
    elif guess > randNum:
        print('Your guess is too high.')
    else:
        break  # this condition is for the correct guess!

if guess == randNum:
    if guessesTaken == 1:
        print('Great job, ' + name + '! You guessed my number on the first guess!')
    else:
        print('Great job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(randNum))
