# gevent library is event-based and accomplishes a cool trick:
# you write normal imperative code, and it magically converts pieces to coroutines.
# The difference from a normal thread is that it doesn’t block.
# If something occurred that would have blocked a normal thread,
# gevent switches control to one of the other greenlets.

import gevent

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.antique-taxidermy.com']
# creates a greenlet (also known sometimes as a green thread or a microthread)
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# waits for all the spawned jobs to finish
gevent.joinall(jobs, timeout=5)

for job in jobs:
    print(job.value)

# Instead of the gevent version of socket, you can use its evocatively named monkeypatching functions.
# These modify standard modules such as socket to use greenlets rather than calling the gevent
# version of the module. This is useful when you want gevent to be applied all the way down,
# even into code that you might not be able to access.
#  this works only for Python code, not libraries written in C
gevent.monkey.patch_socket()
