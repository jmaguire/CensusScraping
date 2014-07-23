from bs4 import BeautifulSoup
import mechanize
import re
import httplib
import time
import csv
import json
import os
import MyTools as tools 
import sys

'''
stateFilename = 'StateURLs'
stateURLs = tools.getJSONData(stateFilename)
'''

data = {}
try: 
    data = tools.getJSONData('us_census')
    print 'loaded'
except:
    data = {}


for subdir, dirs, files in os.walk('./json'):
    try:
        state = subdir.split('/')[-1]
        cities = tools.getJSONData(subdir + '/cities')
        print state
        for city in cities:
            key = city + '|' + state
            if key in data:
                continue
            else:
                print 'need to add'
            soup = tools.getSoup(cities[city]['url'])
            try:
                data[key] = cities[city]
                data[key]['state'] = state 
                for table in soup.findAll('table'):
                    if table.attrs.has_key('title') and 'QuickFacts' in table.attrs['title']:
                        for row in table.findAll('tr'):
                            if row.attrs.has_key('class') and 'shaded' in row.attrs['class'][0]:
                                tds = row.findAll('td')
                                field = tds[1].contents[0]
                                if 'Counties' in field:
                                    value = tds[2].contents[0].string
                                else:
                                    try:
                                        value = tools.getFloat(tds[2].contents[0])
                                    except:
                                        value = tds[2].contents[0]                                
                                data[key][field] = value
            except:
                print 'fatal'
            tools.saveJSONData(data, 'us_census')                
    except:
        continue
    

tools.saveJSONData(data, 'us_census')
