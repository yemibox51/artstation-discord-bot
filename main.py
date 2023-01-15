
# artstation-scrape.py - Downloads the front page of artstation items

import requests, os, bs4

url = 'https://www.artstation.com/doczenith'  # starting url
os.makedirs('artstation-front-page', exist_ok=True)  # store comics in ./xkcd

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
}
for i in range(0, 30):
  # Download the page.

  res = requests.get(url, headers=headers)
  res.raise_for_status()
  # checks to see if that website works, if it doesn't will stop program

  soup = bs4.BeautifulSoup(res.text, 'html.parser')  # parse the html page

  # Find the URL of the comic image.
  list_of_images = soup.select('channel-project-list')
  print(list_of_images)
  break
  comicElem = soup.select('#comic img')
  if comicElem == []:
    print('Could not find comic image.')
  else:
    comicUrl = 'https:' + comicElem[0].get('src')
    # Download the image.
    print('Downloading image %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
      imageFile.write(chunk)
    imageFile.close()

  # Get the Prev button's url.
  prevLink = soup.select('a[rel="prev"]')[0]
  url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
