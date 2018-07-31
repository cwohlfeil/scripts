import memcache
import redis

db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
# True
db.get('marco')
# 'polo'
db.set('ducks', 0)
# True
db.get('ducks')
# 0
db.incr('ducks', 2)
# 2
db.get('ducks')
# 2

# redis.Redis('localhost') or redis.Redis('localhost', 6379)
conn = redis.Redis()
# List all keys
conn.keys('*')
# []
conn.set('secret', 'ni!')
# True
conn.set('carats', 24)
# True
conn.set('fever', '101.5')
# True
conn.get('secret')
# b'ni!'
conn.get('carats')
# b'24'
conn.get('fever')
# b'101.5'

# Here, the setnx() method sets a value only if the key does not exist:
conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
# False
# It failed because we had already defined 'secret':
conn.get('secret')
# b'ni!'
# The getset() method returns the old value and sets it to a new one at the same time:
conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')
# b'ni!'
# Let’s not get too far ahead of ourselves. Did it work?
conn.get('secret')
# b'icky-icky-icky-ptang-zoop-boing!'
# Now, get a substring by using getrange() (as in Python, offset 0=start, -1=end):
conn.getrange('secret', -6, -1)
# b'boing!'
# Replace a substring by using setrange() (using a zero-based offset):
conn.setrange('secret', 0, 'ICKY')
# 32
conn.get('secret')
# b'ICKY-icky-icky-ptang-zoop-boing!'
# Next, set multiple keys at once by using mset():
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
# True
# Get more than one value at once by using mget():
conn.mget(['fever', 'carats'])
# [b'101.5', b'24']
# Delete a key by using delete():
conn.delete('fever')
# True
# Increment by using the incr() or incrbyfloat() commands, and decrement with decr():
conn.incr('carats')
# 25
conn.incr('carats', 10)
# 35
conn.decr('carats')
# 34
conn.decr('carats', 15)
# 19
conn.set('fever', '101.5')
# True
conn.incrbyfloat('fever')
# 102.5
conn.incrbyfloat('fever', 0.5)
# 103.0
# There’s no decrbyfloat().
# Use a negative increment to reduce the fever:
conn.incrbyfloat('fever', -2.0)
# 101.0

