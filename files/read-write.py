import shelve

helloFile = open('/Users/rcanton/Development/python/automate-the-boring-stuff/files/hello.txt')
content = helloFile.read()
print(content)

# contentList = helloFile.readlines()
# print(contentList)
helloFile.close()

helloFileW = open('/Users/rcanton/Development/python/automate-the-boring-stuff/files/hello2.txt', 'w')
helloFileW.write('Hello!!!!!')

helloFileW.close()

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

print(list(shelfFile.keys()))
print(list(shelfFile.values()))
