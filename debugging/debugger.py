import random

# print('Enter the first number to add:')
# first = input()
# print('Enter the second number to add:')
# second = input()
# print('Enter the third number to add:')
# third = input()
# print('The sum is ' + first + second + third)

heads = 0

for i in range(1, 1001):
    if random.randint(0,1) == 1:
        heads += 1
    if i == 500:
        print('Halfway done!')

print(heads)