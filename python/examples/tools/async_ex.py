# A coroutine is a special function that can give up control to its caller without losing its state.
# A coroutine is a consumer and an extension of a generator.
# One of their big benefits over threads is that they don’t use very much memory to execute.
# Note that when you call a coroutine function, it doesn’tactuallyexecute.
# Instead it will return a coroutine object that you can pass to the event loop to have it executed
# either immediately or later on. One other term you will likely run across when you are using the asyncio module
# is future . A future is basically an object that represents the result of work that hasn’t completed.
# Your event loop can watch future objects and wait for them to finish. When a future finishes, it is set to done.
# Asyncio also supports locks and semaphores. The last piece of information I want to mention is the Task.
# A Task is a wrapper for a coroutine and a subclass of Future. You can even schedule a Task using the event loop.


# Very basic example
import asyncio

async def my_coro():
    await func()


# Example web file downloader
import aiohttp
import asyncio
import async_timeout
import os

async def download_coroutine(session, url):
    with async_timeout.timeout(10):
        # Call our session’s get() method which gives us a response object
        async with session.get(url) as response:
            filename = os.path.basename(url)
            # Technically still blocking because of file access, look in to aiofiles
            with open(filename, 'wb') as f_handle:
                while True:
                    '''
                    When you use the content attribute of the response object,
                    it returns an instance of aiohttp.StreamReader which allows us to
                    download the file in chunks
                    '''
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            # finish the response processing
            return await response.release()


async def main(loop):
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf", "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf", "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    '''
    Create a ClientSession object that we pass on to our download coroutine function
    for each of the urls we want to download
    '''
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            await download_coroutine(session, url)


if __name__ == '__main__':
    # Start event loop, call main
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
