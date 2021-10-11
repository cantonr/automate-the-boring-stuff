import re

# non regex example
# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False  # not phone number-sized
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False  # no area code
#     if text[3] != '-':
#         return False  # missing dash
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False  # no first 3 digits
#     if text[7] != '-':
#         return False  # missing dash
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False  # no last 4 digits
#     return True
#
#
# print(isPhoneNumber('hello'))
#
# message = 'Call me at 415-555-1001 tomorrow, or at 415-555-9999 today'
# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i + 12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#         foundNumber = True
#
# if not foundNumber:
#     print('Could not find any phone numbers.')

message = 'Call me at 415-555-1001 tomorrow, or at 415-555-9999 today'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search(message)
print(mo)
print(mo.group())

moAll = phoneNumRegex.findall(message)
print(moAll)

# groups
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 234-555-2948')
print(mo.group())
print(mo.group(1))
print(mo.group(2))

# pipes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
# mo = batRegex.search('Batmotorcycle lost a wheel')
# print(mo.group()) # throws errors since no group is found


# patterns and greedy/nongreedy matching
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo = phoneRegex.search('This is my number 849-8923. Call me.')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')
print(batRegex.search('The adventures of Batman'))
print(batRegex.search('The adventures of Batwowowowoman'))

# escaping ?, *, +
regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))

phoneRegex = re.compile(r'((\d{3}-)?\d{3}-\d{4}(,)?){3}')
print(phoneRegex.search('My numbers are 111-222-3333,444-555-6666,777-888-9999'))

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('HaHaHaHa'))
print(haRegex.search('HaHaHaHaHaHaHaHa'))

# similar to slices in lists/str
haRegex = re.compile(r'(Ha){,5}')
haRegex = re.compile(r'(Ha){3,}')

# greedy match
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('123456789'))
# non-greedy match
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('123456789'))

# character classes and findall() method
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneRegex)
print(phoneRegex.findall(
    'This is my number 333-333-3333, but this is also my number 555-555-5555. Also this? 999-999-9999'))

phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print(phoneRegex.findall(
    'This is my number 333-333-3333, but this is also my number 555-555-5555. Also this? 999-999-9999'))

phoneRegex = re.compile(r'((\d{3})-(\d{3}-\d{4}))')
print(phoneRegex.findall(
    'This is my number 333-333-3333, but this is also my number 555-555-5555. Also this? 999-999-9999'))

# character classes
digitRegex = re.compile(r'\d')
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying'
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

# custom character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u'
print(vowelRegex.findall('Robocop eats baby food'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats baby food'))
# negative character class
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food'))

# regex dot-star and caret/dollar characters
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('He said Hello there!'))
endWithWorldRegex = re.compile(r'world!$')
print(endWithWorldRegex.search('Hello world!'))
print(endWithWorldRegex.search('Hello world! wide web'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('2398427827492839042948'))
print(allDigitsRegex.search('239842782x7492839042948'))

# dot character (any char except new line)
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sad on the flat mat'))
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sad on the flat mat'))
# dot-star pattern (uses greedy mode)
nameRegex = re.compile(r'First name: (.*) Last Name: (.*)')
print(nameRegex.findall('First name: Bat Last Name: Man'))
# use dot-star with non-greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent.\nUpload the law.'
print(prime)
dotstar = re.compile(r'.*', re.DOTALL)
print(dotstar.search(prime))

vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.search('Al, why does this ignore Stuff soo Much?'))
print(vowelRegex.findall('Al, why does this ignore Stuff soo Much?'))
vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.search('Al, why does this ignore Stuff soo Much?'))
print(vowelRegex.findall('Al, why does this ignore Stuff soo Much?'))

# sub method and verbose mode
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob'))

# group matches
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob'))

# verbose mode
phoneRegex = re.compile(r'''
\d\d\d      # area code
-           # first dash
\d\d\d      # first 3 digits
-           # second dash
\d\d\d\d    # last 4 digits
''', re.VERBOSE | re.DOTALL | re.IGNORECASE)
print(phoneRegex)
