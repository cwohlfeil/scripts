# Client 1, start second
import redis

conn = redis.Redis()
print('Washer is starting')
dishes = ['salad', 'bread', 'entree', 'dessert']
for dish in dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
print('Washer is done')


# Client 2
import redis
import os
import time
import multiprocessing


def dryer():
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print('Dryer process %s is starting' % pid)
    while True:
        msg = conn.blpop('dishes', timeout)
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val == 'quit':
            break
        print('%s: dried %s' % (pid, val))
        time.sleep(0.1)
    print('Dryer process %s is done' % pid)


DRYERS = 3
for num in range(DRYERS):
    p = multiprocessing.Process(target=dryer)
    p.start()

# This code waits for messages whose first token is “dishes” and prints that each one is dried.
# It obeys the quit message by ending the loop.

