helloFile = open('c:\\temp\\hello.txt')
content = helloFile.read()
print(content)
print(helloFile.readlines())
helloFile.close()
helloFile = open('c:\\temp\\hello2.txt', 'w')
helloFile.write('Hello!!!!\n')
helloFile.close()

import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()