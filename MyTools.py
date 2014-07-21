from bs4 import BeautifulSoup
import mechanize
import json
import re

def getJSONData(filename):
    with open(filename) as readfile:
        data = json.load(readfile)
    return data    

def getSoup(url):
    br = mechanize.Browser()
    page = br.open(url)
    html = page.read()
    return BeautifulSoup(html)

def saveJSONData(data, filename):
    with open(filename, 'wb') as outfile:
        data = json.dump(data, outfile, indent = 4)

def getFloat(string):
    string = string.replace(",","")
    string = string.replace("%","")
    return re.findall(r"[-+]?\d*\.\d+|\d+", string)[0]
    
