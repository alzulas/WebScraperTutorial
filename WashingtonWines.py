#############################################
#                                           #
#       This code writen by A.L.Zulas       #
#       Written in September 2019           #
#       Code pulls data from Washington     #
#           wines website and parses it     #
#           into a useful format            #
#                                           #
#############################################


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import json
import csv

#this method a test of error handling when pulling from the website
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h3
    except AttributeError as e:
        return None
    return title

#this method parses the JSON data into a csv
def writeToFile (all_wineries):
    # open a file for writing
    file_data = open('/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial/TestData.csv', 'w')
    csvwriter = csv.writer(file_data)
    count = 0
    for winery in all_wineries:
        if count == 0:
            header = winery.keys()
            csvwriter.writerow(header)
            count += 1
        csvwriter.writerow(winery.values())
    file_data.close()

#This method parses out the wine types defined in the file, and returns only unique elements
def getUniqueWineTypes(data):
    wineTypes = []

    for everything in data['data']:
        for wine in everything['wines']:
            wineTypes.append(wine['variety'])
    print(wineTypes)

    # insert the list to the set 
    list_set = set(wineTypes) 
    # convert the set to the list 
    unique_list = (list(list_set))
    unique_list.sort() 
    for x in unique_list: 
        print (x)
    return(unique_list)



html = urlopen('https://www.washingtonwine.org/api/queries/entities?getcount=true&types=Winery&getwines=true&getlogo=true&getregion=true&query=')

#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#bs = BeautifulSoup(html.read(), "html5lib")

data = json.load(html)
#print(json.dumps(data, indent = 4, sort_keys=True))
#/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial





#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#print(html.read())
