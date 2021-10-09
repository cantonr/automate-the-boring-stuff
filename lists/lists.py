spam = ['cat', 'bat', 'rat', 'elephant']

print(spam[1])

spams = [['cat', 'bat'], [1, 2, 3, 4, 5]]

print(spams[1][-1])

print(spams[1][1:3])

spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)

del spam[2]
print(spam)

print(len('Hello'))
print(len([1, 2, 3]))

# concat lists
[1, 2, 3] + [4, 5, 6]  # [1, 2, 3, 4, 5, 6]

# list multiplications
[1, 2, 3] * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

list('Hello')

42 in [1, 23, 42]

'howdy' not in ['hi', 'hey', 'yo']