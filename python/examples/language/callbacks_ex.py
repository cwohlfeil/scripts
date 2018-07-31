import asyncio
import functools

# need the functools module if we need to pass keywords to our event handler


def event_handler(loop, stop=False):
    print('Event handler called')
    if stop:
        print('stopping the loop')
        loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.call_soon(functools.partial(event_handler, loop))
        print('starting event loop')
        loop.call_soon(functools.partial(event_handler, loop, stop=True))

        loop.run_forever()
    finally:
        print('closing event loop')
        loop.close()

# There is a related function called call_soon_threadsafe. As the name implies, it works the same way as call_soon,
# but it’s thread-safe. If you want to actually delay a call until some time in the future, you can do so
# using the call_later function. In this case, we could change our call_soon signature to the following:

loop.call_later(1, event_handler, loop)

# This will delay calling our event handler for one second, then it will call it and pass
# the loop in as its first parameter. If you want to schedule a specific time in the future,
# then you will need to grab the loop’s time rather than the computer’s time. You can do so like this:

current_time = loop.time()

# Once you have that, then you can just use the call_at function and pass it the time that you want it
# to call your event handler. So let’s say we want to call our event handler five minutes from now.

loop.call_at(current_time + 300, event_handler, loop)
