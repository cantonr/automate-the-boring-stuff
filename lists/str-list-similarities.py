import copy

hi = list('Hello')
print(hi)

name = 'Zophie'
print(name[0])
print(name[1:3])
print('Zo' in name)

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

# this is copying the reference to spam, so changing the mutable list changes both variables
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)


def eggs(cheese):
    cheese.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
print(spam)
print(cheese)

cheese[1] = 42
print(spam)
print(cheese)

# line continuation
spam = ['apples',
        'oranges',
        'bananas']
print(spam)

print('Four score and seven' + \
      ' years ago')
