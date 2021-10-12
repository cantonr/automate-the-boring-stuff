'''
The Requests module is a third-party module for downloading web pages and files.
requests.get() returns a Response object.
The raise_for_status() Response method will raise an exception if the download failed.
You can save a downloaded file to your hard drive with calls to the iter_content() method.
'''

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
# print(res.text[:500])

print(res.raise_for_status())
# badRes = requests.get('https://automatetheboringstuff.com/kajofiejaofiej')
# print(badRes.raise_for_status())

playfile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()
