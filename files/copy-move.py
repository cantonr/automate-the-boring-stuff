import shutil

name = shutil.copy('./hello.txt', '../')
print(name)

shutil.copytree('source', 'destination')
shutil.move('source', 'destination')
