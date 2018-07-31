#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = 'http://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            # skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com{}'.format(prevLink.get('href'))
            continue

        # Save the image to ./xkcd.
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as imageFile:
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com{}'.format(prevLink.get('href'))

print('Done.')
