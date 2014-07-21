from bs4 import BeautifulSoup
import mechanize
import json


def getJSONData(filename):
    with open(filename) as readfile:
        data = json.load(readfile)
    return data    

def getSoup(url):
    br = mechanize.Browser()
    page = br.open(url)
    html = page.read()
    return BeautifulSoup(html)


