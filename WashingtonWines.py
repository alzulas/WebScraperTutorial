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

WineVarietyColors = ['White', 'Red', 'Red', 'Red', 'White', 'Red', 'White', 'Red', 'White', 'Red', 'White', 'Red', 'Red', 'Red', 'White', 'White', 'Other', 
'Red', 'Red', 'White', 'Other', 'White', 'Red', 'White', 'White', 'Red', 'White', 'Other', 'Red', 'White', 'Red', 'Red', 'Other', 'Red', 
'Red', 'Red', 'White', 'White', 'White', 'Red', 'Red', 'White', 'Other', 'Red', 'Red', 'White', 'White', 'Red', 'Red', 'White', 'Other', 
'White', 'Red', 'Other', 'Red', 'White', 'White', 'White', 'Other', 'White', 'Red', 'Red', 'Red', 'Red', 'White', 'Red']


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
def writeToFile (data, listOfWineNames):
    # open a file for writing
    file_data = open('/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial/TestData.csv', 'w')
    csvwriter = csv.writer(file_data)
    count = 0
    wineriesGivenWines = []
    all_wineries = data['data']
    for winery in all_wineries:
        if count == 0:
            header = list(winery.keys())
            wineTotals = ["White Wines", "Red Wines", "Other Types"]
            header.extend(wineTotals)
            header.extend(listOfWineNames)
            #print(type(header))
            csvwriter.writerow(header)
            count += 1
        placeInWineList = 0
        numWhite = 0
        numRed = 0
        numOther = 0
        for wineType in listOfWineNames:
            wineriesGivenWines.append('No') #set element to no
            for wine in winery['wines']: #Check if element exists in wine varieties
                if (wine['variety'] == wineType):
                    wineriesGivenWines[placeInWineList] = 'Yes' #if it is in there
                    if (WineVarietyColors[placeInWineList] == "White"):
                        numWhite += 1
                    elif (WineVarietyColors[placeInWineList] == "Red"):
                        numRed += 1
                    else: 
                        numOther += 1
            placeInWineList += 1
            #Go for next
        #print("Whites = " + str(numWhite) + ", Reds = " + str(numRed) + ", Other = " + str(numOther))
        tmpRow = list(winery.values())
        #print("This is the tmp Row")
        #print(type(wineriesGivenWines))
        wineTotals = [numWhite, numRed, numOther]
        tmpRowExtended = tmpRow + wineTotals + wineriesGivenWines
        #print(tmpRowExtended)
        csvwriter.writerow(tmpRowExtended)
        wineriesGivenWines = []
    file_data.close()

#This method parses out the wine types defined in the file, and returns only unique elements
def getUniqueWineTypes(data):
    wineTypes = []

    for everything in data['data']:
        for wine in everything['wines']:
            wineTypes.append(wine['variety'])
            #because I wanted to know
            #if (wine['variety'] == "Muscat Noir"):
            #    print (everything['name'] + ", located in " + everything['region'] + ", carrying " + wine['variety'])
            #elif (wine['variety'] == "Blend - Bordeaux Style White" and everything['region'] == 'Walla Walla'):
            #    print (everything['name'] + ", located in " + everything['region'] + ", carrying " + wine['variety'])
            #elif (wine['variety'] == "Black Muscat"):
            #    print (everything['name'] + ", located in " + everything['region'] + ", carrying " + wine['variety'])
            #elif (wine['variety'] == "Blend - Rhone Style White" and everything['region'] == 'Walla Walla'):
            #    print (everything['name'] + ", located in " + everything['region'] + ", carrying " + wine['variety'])
    #print(wineTypes)

    # insert the list to the set 
    list_set = set(wineTypes) 
    # convert the set to the list 
    unique_list = (list(list_set))
    unique_list.sort() 
    print(unique_list)
    return(unique_list)



html = urlopen('https://www.washingtonwine.org/api/queries/entities?getcount=true&types=Winery&getwines=true&getlogo=true&getregion=true&query=')

#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#bs = BeautifulSoup(html.read(), "html5lib")

data = json.load(html)
#print(json.dumps(data, indent = 4, sort_keys=True))
#/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial

listOfWineNames = getUniqueWineTypes(data)
#print (listOfWineNames)

writeToFile(data, listOfWineNames)




#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#print(html.read())
