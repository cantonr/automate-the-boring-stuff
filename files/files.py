import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)
print(os.getcwd())
# print(os.chdir('/Users/rcanton/Downloads'))
print(os.getcwd())

print(os.path.abspath('files.py'))
print(os.path.abspath('../../files.py'))
print(os.path.isabs('../../files.py'))
print(os.path.isabs('/Users/rcanton'))
print(os.path.relpath('/Users/rcanton/Development/python/automate-the-boring-stuff'), '/Users/rcatnon')
print(os.path.dirname('/Users/rcanton/spam.png'))
print(os.path.basename('/Users/rcanton/spam.png'))
print(os.path.basename('/Users/rcanton'))

print(os.path.exists('/Users/rcanton/spam.png'))
print(os.path.isfile('/Users/rcanton/spam.png'))
print(os.path.isdir('/Users/rcanton'))

print(os.path.getsize('/Users/rcanton/Development/python/automate-the-boring-stuff/files/files.py'))
print(os.listdir('/Users/rcanton/Downloads'))

totalSize = 0
for filename in os.listdir('/Users/rcanton/Downloads'):
    if not os.path.isfile(os.path.join('/Users/rcanton', filename)):
        continue
    totalSize += os.path.getsize(os.path.join('/Users/rcanton', filename))
print(totalSize)
