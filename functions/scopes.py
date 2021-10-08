spam = 42  # glabal variable


def breky():
    global spam # use global variable
    spam = 21  # local variable
    print(spam)


print('some code here')
print('some more here')
print(spam)
breky()
print(spam)


def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    ham = 101
    eggs = 0


spam()
