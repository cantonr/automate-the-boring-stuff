import os
import shutil
import send2trash

print(os.getcwd())

# os.unlink('some_path') # deletes a file
# os.rmdir('some_folder')  # folder must be empty

# shutil.rmtree('some_folder') # can be dangerous, be careful when using

for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unlink(filename)
        print(filename)


send2trash.send2trash('some_path')