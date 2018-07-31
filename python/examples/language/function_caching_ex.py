# Function caching allows us to cache the return values of a function depending on the arguments.
# It can save time when an I/O bound function is periodically called with the same arguments.
# In Python 3.2+ there is an lru_cache decorator which allows us to quickly
# cache and uncache the return values of a function.

from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# The maxsize argument tells lru_cache about how many recent return values to cache.
# We can easily uncache the return values as well by using:
fib.cache_clear()
