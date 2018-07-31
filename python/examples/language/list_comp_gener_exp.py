# List comprehension
xyz = [i for i in range(500000)]
print('done')
# Generator expression
xyz = (i for i in range(500000))
print(xyz)

input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]


def div_by_five(num):
    return num % 5 == 0

xyz = (i for i in input_list if div_by_five(i))
#Creates a generator object that is equal to
#xyz = []
#for i in input_list:
#    if div_by_five(i):
#        xyz.append(i)

for i in xyz:
    print(i)

xyz = (print(i) for i in xyz)
for i in xyz:
    i

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)

xyz = (((i, ii) for ii in range(5)) for i in range(5))
#for i in range(5):
#    for ii in range(5):
#        print(i, ii)
print(xyz)
for i in xyz:
    for ii in i:
        print(ii)