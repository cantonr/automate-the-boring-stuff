for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

print(list(range(0, 100, 2)))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

size, color, disposition = cat

# quick sqap
a = 'AAA'
b = 'BBB'

a, b = b, a

# augmented assignment operators
spam = 42
spam = spam + 1
spam += 1

