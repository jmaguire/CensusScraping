import MyTools as tools
import csv
import os

def buildLine(fields, city):
    line = []
    for field in fields:
        if field not in city:
            print field
            print city
        line.append(city[field])
    return line


data = tools.getJSONData('us_census');
fields = data.itervalues().next().keys();

'''
states = []
for subdir, dirs, files in os.walk('./json'):
    state = subdir.split('/')[-1]
    if state == 'json':
        continue
    states.append(state)

for city_name in data:
    state = b3 = [val for val in data[city_name].keys() if val in states][0]
    data[city_name].pop(state, None)
    data[city_name]['state'] = state

tools.saveJSONData(data, 'us_census_fixed')
'''

with open('us_census.csv', 'wb') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(fields)
    for city_name in data:
        writer.writerow(buildLine(fields,data[city_name]))

