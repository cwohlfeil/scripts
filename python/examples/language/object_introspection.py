# introspection is the ability to determine the type of an object at runtime

my_list = [1, 2, 3]
dir(my_list)
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
# '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__',
# '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

# type function returns the type of an object
print(type(''))
# Output: <type 'str'>
print(type([]))
# Output: <type 'list'>
print(type({}))
# Output: <type 'dict'>
print(type(dict))
# Output: <type 'type'>
print(type(3))
# Output: <type 'int'>


# id returns the unique ids of various object
name = "Yasoob"
print(id(name))
# Output: 139972439030304


# The inspect module also provides several useful functions to get information about live objects.
# For example you can check the members of an object by running:

import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...
