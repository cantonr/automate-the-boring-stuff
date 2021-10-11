##! /usr/bin/env python3

# TODO: create a regex for phone numbers
# TODO: create a regex for email addresses
# TODO: get the text off the clipboard
# TODO: extract the email/phone from this text
# TODO: copy the extracted email/phone to the clipboard

import re
import pyperclip

phoneNumRegex = re.compile(r'\(?\d{3}\)?-\d{3}-\d{4}')
phoneNum = '312-555-9483 is 312-999-3245 also 899-920-3924'
# print(phoneNumRegex.findall(phoneNum))

emailRegex = re.compile(r'\S+@\S+\.\S+')
email = 'ema il-ex@blah.com'
print(emailRegex.search(email))

copiedText = pyperclip.paste()

extractedPhoneNums = '\n'.join(phoneNumRegex.findall(copiedText))
extractedEmail = emailRegex.findall(copiedText)
# print(extractedPhoneNums)
print(len(extractedEmail))
# extracted = '\n'.join(phoneNumRegex.findall(copiedText)) + '\n' + '\n'.join(emailRegex.findall(copiedText))

# pyperclip.copy(extracted)


# Course solution
# create a regex for phone numbers
phoneRegex = re.compile(r'''
# 414-555-0000, 555-9999, (412) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d{3})|(\(\d{3}\)))?      # area code (optional)
(\s|-)                      # first separator
\d{3}                       # first 3 digits
-                           # separator
\d{4}                       # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
 (\d{2.5}))?                # extension number-part (optional)
)
''', re.VERBOSE)

# create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name part
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNum in extractedPhone:
    allPhoneNumbers.append(phoneNum[0])

# TODO: copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

