import shutil
import os
import send2trash

shutil.copy('c:\\temp\\hello.txt', 'c:\\temp\\hello\\hello.txt')
shutil.copytree('C:\\temp\\hello', 'C:\\temp\\backup')
shutil.move('C:\\temp\\hello2.txt', 'C:\\temp\\hello3.txt')

os.unlink('C:\\temp\\hello3.txt')
os.rmdir('C:\\temp\\backup')
shutil.rmtree('C:\\temp\\backup')

os.chdir('C:\\temp\\backup')

for f in os.listdir():
    if f.endswith('.txt'):
        os.unlink(f)

send2trash.send2trash('C:\\temp\\hello2.txt')
