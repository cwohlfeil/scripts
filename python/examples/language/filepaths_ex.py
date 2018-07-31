import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)
print(os.getcwd())
os.chdir('C:\\')

# . in file path means current folder, .. means one level up

print(os.path.abspath('filepaths_ex.py'))
print(os.path.abspath('.\\filepaths_ex.py'))
print(os.path.isabs('.\\filepaths_ex.py'))
print(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))
print(os.path.dirname('.\\filepaths_ex.py'))
print(os.path.basename('.\\filepaths_ex.py'))
print(os.path.exists('.\\filepaths_ex.py'))
print(os.path.isfile('.\\filepaths_ex.py'))
print(os.path.isdir('.\\'))
print(os.path.getsize('.\\filepaths_ex.py'))
print(os.listdir('.\\'))
# os.makedirs()

totalSize = 0
for f in os.listdir('d:\\dropbox\\screenshots'):
    if not os.path.isfile(os.path.join('d:\\dropbox\\screenshots', f)):
        continue
    totalSize += os.path.getsize(os.path.join('d:\\dropbox\\screenshots', f))

print(totalSize)
