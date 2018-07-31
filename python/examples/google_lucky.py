#! python3
# google_lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q={}'.format(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com{}'.format(linkElems[i].get('href')))
