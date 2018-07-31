# Coroutines are similar to generators with a few differences. The main differences are:
# generators are data producers
# coroutines are data consumers
# First of all let’s review the generator creation process.

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
# We then commonly use it in a for loop like this:

for i in fib():
    print(i)

# It is fast and does not put a lot of pressure on memory because it generates the values on the fly
# rather than storing them in a list. Now, if we use yield in the above example, more generally, we get a coroutine.
# Coroutines consume values which are sent to it. A very basic example would be a grep alternative in Python:

def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

# Wait! What does yield return? Well we have turned it into a coroutine.
# It does not contain any value initially, instead we supply it values externally.
# We supply values by using the .send() method. Here is an example:

search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Output: I love coroutines instead!

# The sent values are accessed by yield. Why did we run next()?
# It is required in order to start the coroutine.
# Just like generators, coroutines do not start the function immediately.
# Instead they run it in response to the __next__() and .send() methods.
# Therefore, you have to run next() so that the execution advances to the yield expression.

# We can close a coroutine by calling the .close() method:

search = grep('coroutine')
# ...
search.close()
