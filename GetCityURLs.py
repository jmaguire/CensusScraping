from bs4 import BeautifulSoup
import mechanize
import json
import MyTools as tools 


stateFilename = './json/StateURLs'
stateURLs = tools.getJSONData(stateFilename)

## City URL in id = Places
for state, url in stateURLs.items():
    print url
    soup = tools.getSoup(url)
    tags = soup.findAll(id = 'Places')
    print tags.text()
    
'''
tags = soup.findAll('area')

for tag in tags:
    data[tag.attrs['title']] = url + '/' + tag.attrs['href']

## Export to json
with open(filename, 'wb') as outfile:
    json.dump(data, outfile, indent = 4)
'''


















