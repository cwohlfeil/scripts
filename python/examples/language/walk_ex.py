import os

for folder, subfolders, filenames in os.walk('C:\\temp'):
    print('The folder is {}'.format(folder))
    print('The subfolders are {}'.format(subfolders))
    print('The filenames are {}'.format(filenames))
    print()

