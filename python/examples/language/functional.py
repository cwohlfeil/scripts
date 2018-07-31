from functools import reduce

# Blueprint: lambda argument: manipulate(argument)


def fahr(t):
    return (9/5)*t+32

temp = [0, 22.5, 40, 100]

map(fahr, temp)

map(lambda t: (9/5)*t+32, temp)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

map(lambda x, y, z: x+y+z, a, b, c)

lst = [47, 11, 42, 13]
reduce(lambda x, y: x+y, lst)

reduce(lambda x, y: x if (x > y) else y, lst)

lst = range(10)
filter(lambda x: (x % 2 == 0), lst)

l = ['a', 'b', 'c']
for count, item in enumerate(l):
    print(count, item)

lst = [True, True, False, True]
all(lst)
any(lst)


# List sorting
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

# Parallel sorting of lists

data = zip(list1, list2)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
