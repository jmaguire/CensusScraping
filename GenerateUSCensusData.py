from bs4 import BeautifulSoup
import mechanize
import re
import httplib
import time
import csv
import json
stateFilename = 'StateURLs'


def getJSONData(filename):
    with open(filename) as readfile:
        data = json.load(readfile)
    return data    

def getSoup(url):
    br = mechanize.Browser()
    page = br.open(state_url)
    html = page.read()
    return BeautifulSoup(html)



stateURLs = getJSONData(stateFilename)


for state, url in map.items():

    soup = getSoup()    
    options = soup.findAll('option')
    
    citylinks = dict()
    
    for option in options:
        if len(option['value']) == 15:
            citylinks[option.contents[0]] = url+option['value']
            
    data = dict()
     
    for city in citylinks:
        try:
            page = br.open(citylinks[city])
            #print citylinks[city]
            html = page.read()
            soup = BeautifulSoup(html)
            citydata = dict()
            tables = soup.findAll('table')
            for table in tables:
                try:
                    if 'Quick' in table['title']:
                        rows = table.findAll('tr')
                        for row in rows:
                            try:
                                if 'shaded' in row['class']:
                                    tds = row.findAll('td')
                                    citydata[tds[1].contents[0]] = tds[2].contents[0]
                            except KeyError:
                                pass
                except KeyError:
                    pass
            data[city] = citydata
        except httplib.IncompleteRead:
            time.sleep(3)
            page = br.open(citylinks[city])
            #print citylinks[city]
            html = page.read()
            soup = BeautifulSoup(html)
            citydata = dict()
            tables = soup.findAll('table')
            for table in tables:
                try:
                    if 'Quick' in table['title']:
                        rows = table.findAll('tr')
                        for row in rows:
                            try:
                                if 'shaded' in row['class']:
                                    tds = row.findAll('td')
                                    citydata[tds[1].contents[0]] = tds[2].contents[0]
                            except KeyError:
                                pass
                except KeyError:
                    pass
            data[city] = citydata
    
    out = csv.writer(open('States/'+name+'.csv','wb'))
    
    for city in data:
        for line in data[city]:
            if '<' not in str(data[city][line]):
                out.writerow([city,line,data[city][line]])

'''
