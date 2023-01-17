# artstation-scrape.py - Downloads the front page of artstation items

import requests, os, bs4, random
import lxml

# Ouptut: Image link + Title of Image + Author + Image.png
# Output in code: image_link + title_of_piece + author_name + artwork_id.png

#url = 'https://www.artstation.com/doczenith'  # starting url
file_path = 'artstation-front-page/'
os.makedirs(file_path, exist_ok=True)

url = "https://www.artstation.com/artwork.rss?page={}".format(random.randint(1,1000))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'
}
res = requests.get(url, headers=headers)

res.raise_for_status() # checks to see if that website works, if it doesn't will stop program

soup = bs4.BeautifulSoup(res.text, 'lxml-xml') # parse the xml page
list_of_images = soup.select('item > link')

random_image = random.randint(0,len(list_of_images)-1)
image_link = list_of_images[random_image].text
artwork_id = image_link.split("/")[-1]

new_url = "https://www.artstation.com/projects/{}.json".format("4X0n0l")

req = requests.get(new_url, headers=headers)
js = req.json()

# title

#print(js)
author_name = js['user']['full_name']
title_of_piece = js['title']
print("{} by {}".format(title_of_piece, author_name))

assets = js["assets"]
image_url = assets[0]["image_url"]


# Downloading the image
# image = requests.get(image_url, headers=headers)
# full_file_path = file_path + "{}.png".format(artwork_id)
# with open(full_file_path, "wb") as file:
#     file.write(image.content)
