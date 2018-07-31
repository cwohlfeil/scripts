import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

res.status_code == requests.codes.ok
print(len(res.text))

print(res.text[:250])

res_error = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res_error.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        # The iter_content() method returns “chunks” of the content on each iteration through the loop.
        # Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
        # One hundred thousand bytes is generally a good size
        playFile.write(chunk)

