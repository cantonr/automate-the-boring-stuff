spam = ['hello', 'howdy', 'hi', 'heyas']
index = spam.index('hello')
print(index)

index = spam.index('heyas')
print(index)

# append and insert
spam.append('yo')
print(spam)

spam.insert(1, 'sup')
print(spam)

# remove
spam.remove('hi')
print(spam)

# spam.remove('dude') # ValueError

# sort
nums = [4, 24, 245, 2, 45, 12]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

names = ['Alice', 'Bob', 'ants', 'Carol', 'cats']
names.sort()
print(names)

letters = ['b', 'A', 'a', 'B']
letters.sort()
print(letters)

letters.sort(key=str.lower)
print(letters)
