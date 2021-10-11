import pprint

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat)
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

eggs = {'name': 'Jack', 'species': 'cat', 'age': 9}
ham = {'species': 'cat', 'name': 'Jack', 'age': 9}
print(ham == eggs)

print('name' in eggs)
print('name' not in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

if 'color' in eggs:
    print(eggs['color'])

print(eggs.get('age', 0))
print(eggs.get('color', ''))

picnicItems = {'apple': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' to the picnic')
# print('I am bringing ' + str(picnicItems['napkins']) + ' to the picnic')

print(eggs.setdefault('color', 'gray'))
print(eggs.setdefault('color', 'black'))

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}  # 'r': 12

for character in message.lower():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
text = pprint.pformat(count)
print(text)
