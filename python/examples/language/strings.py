import os

names = ['Jeff', 'Gary', 'Jill', 'Samantha']

for name in names:
    print('Hello there ' + name)
    print(' '.join(['Hello there', name]))

print(', '.join(names))

location_of_file = 'C:\\Users\\wohlf_000\\Dropbox\\examples\\scripts'
filename = 'example.txt'

print(location_of_file + '\\' + filename)

with open(os.path.join(location_of_file, filename)) as f:
    print(f.read())

animals = ['bird', 'cat', 'dog']
print('The {} was eaten by the {} which was chased off by the {}'.format(*animals))

d = {'Arnold': 18, 'Bernard': 19, 'Ford': 21}
s = "They are {Arnold}, {Bernard}, {Ford} years old"
print(s.format(**d))
x = 42
s2 = "The cake is {}".format("the answer" if x == 42 else 'a lie')
print(s2)
d2 = {'Arnold': 181, 'Bernard': 192, 'Ford': 213}
# This is weird
print(s.format(**d if x == 43 else d2))