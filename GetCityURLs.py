from bs4 import BeautifulSoup
import mechanize
import json
import MyTools as tools 
import re
import os


def extractNameAndDescriptor(string):
    valid = re.compile(r'(.+)\((\w+)\)')
    matches = valid.match(string)
    return matches.group(1), matches.group(2)

stateFilename = './json/StateURLs'
stateURLs = tools.getJSONData(stateFilename)
baseUrl = 'http://quickfacts.census.gov/qfd/states/'

## City URL in id = Places
for state, url in stateURLs.items():

    data = {}
    print state, url
    directory = './json/' + state

    if not os.path.exists(directory):
        os.makedirs(directory)

    soup = tools.getSoup(url)
    tags = soup.find('select', id = 'Place')

    for tag in tags.findAll('option'):
        city = {}
        cityUrl = baseUrl + tag.attrs['value']
        try:
            (name,descriptor) = extractNameAndDescriptor(tag.string)
        except:
            ## Some links are to the state/ demos
            continue 
        city['name'] = name
        city['descriptor'] = descriptor
        city['url'] = cityUrl
        data[name] = city 
    
    tools.saveJSONData(data, directory + '/cities') 

















