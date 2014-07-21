from bs4 import BeautifulSoup
import mechanize
import json
import os 

filename = 'StateURLs'
url = 'http://quickfacts.census.gov/qfd/index.html'
data = {}

## Get <area> fields. These have the state url data
br = mechanize.Browser()
page = br.open(url)
html = page.read()
soup = BeautifulSoup(html)
tags = soup.findAll('area')

for tag in tags:
    data[tag.attrs['title']] = url + '/' + tag.attrs['href']

## Export to json
if not os.path.exists('./json'):
    os.makedirs('./json')

with open('./json/' + filename, 'wb') as outfile:
    json.dump(data, outfile, indent = 4)







