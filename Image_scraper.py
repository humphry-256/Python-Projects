# downloads XKCD comics
import requests
import os
import bs4
url = "http://xkcd.com"  # this is the starting URL
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
while not url.endswith("#"):
    # Download the page
    print("Downloading page %s..." % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,features="html.parser")

    #Find the URL of the comic page
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    # Save the Image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the prev button's URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print("done")
