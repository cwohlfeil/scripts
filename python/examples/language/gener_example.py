def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'

for i in simple_gen():
    print(i)

correct_combo = (1, 6, 1)

#for c1 in range(10):
#    for c2 in range(10):
#        for c3 in range(10):
#            if (c1, c2, c3) == correct_combo:
#                print('Found the combo: {}'.format((c1, c2, c3)))


def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c2, c3, c3)
    if (c1, c2, c3) == correct_combo:
        print('Found the combo: {}'.format((c1, c2, c3)))
        break


def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for x in range(n):
        yield a
        a, b = b, a+b

g = genfibon(100)

print(next(g))
print(next(g))
print(next(g))