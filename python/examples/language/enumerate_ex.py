example = ['left', 'right', 'up', 'down']

for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]


y_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
# The optional argument allows us to tell enumerate from where to start the index.
# You can also create tuples containing the index and list item using a list. Here is an example:

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
