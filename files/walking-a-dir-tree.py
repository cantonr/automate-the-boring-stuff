import os
import shutil

for foldername, subfolders, filenames in os.walk('../files'):
    print('The folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are: ' + str(subfolders))
    print('The filenames in ' + foldername + ' are: ' + str(filenames))

    for subfolder in subfolders:
        if 'fish' in subfolder:
            # os.rmdir(subfolder)
            print('rmdir on ' + subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.path.join(foldername, file), os.path.join(foldername, file + '.backup'))

