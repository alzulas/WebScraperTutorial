#####################################################################
#                                                                   #
#        This code writen by A. Leah Zulas                          #
#        Using the tutorial from Web Scraping with Python           #
#        You may use this code to retrieve information about        #
#           shows from IMDB and create a spread sheet               #
#        I then sorted using Excel, because it was simple           #
#        Please use this scraper carefully and don't overload       #
#           IMDB servers too much.                                  #
#        Thanks, enjoy!                                             #
#                                                                   #
##################################################################### 

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import json
import csv


'''
In case I ever decide to put error catching in
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
'''


#Retreieve all of the seasons from the show and return a list of the seasons
def getAllLinks(firstLink, allLinks):
    html = urlopen(firstLink)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/title/)(.)*(/episodes)(.)(season)(.)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            allLinks.append(link.attrs['href'])
    return(allLinks)

#Retreieve and copy the episodes to a CSV
def getDataPoints(allLinks, show, csvwriter):
    for link in allLinks:
        html = urlopen("https://www.imdb.com" + link)
        bs = BeautifulSoup(html, "html.parser")
        strong_tag = bs.find('div', {'id':'episodes_content'}).find_all('strong')
        airdates = bs.find_all(class_='airdate')
        #print (strong_tag)
        for i in range(0, len(airdates)):
            #print("Show = " + show + ", Season = " + strong_tag[len(airdates)].text + ", Episode " + str(i+1) + " = " + strong_tag[i].text + ', ' + airdates[i].text[13:-5])
            tmpRow = [show, strong_tag[len(airdates)].text, str(i+1), strong_tag[i].text, airdates[i].text[13:-5]]
            #print (tmpRow)
            csvwriter.writerow(tmpRow)
        #print("Season = " + strong_tag[len(airdates)].text + '\n')

#Header entry intot eh csv and open it. 
header = ['Show', 'Season', 'Episode Number', 'Episode Title', 'Airdate']
file_data = open('/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial/allDCUniverseEpisodes.csv', 'w')
csvwriter = csv.writer(file_data)
csvwriter.writerow(header)
print(header)

#Super Girl
allLinksSuperGirl = []
allLinksSuperGirl = getAllLinks('https://www.imdb.com/title/tt4016454/', allLinksSuperGirl)
getDataPoints(allLinksSuperGirl, 'Super Girl', csvwriter)

#Arrow
allLinksArrow = []
allLinksArrow = getAllLinks('https://www.imdb.com/title/tt2193021/', allLinksArrow)
getDataPoints(allLinksArrow, 'Arrow', csvwriter)

#Legends of Tomorrow
allLinksLegends = []
allLinksLegends = getAllLinks('https://www.imdb.com/title/tt4532368/', allLinksLegends)
getDataPoints(allLinksLegends, 'Legends of Tomorrow', csvwriter)

#Flash
allLinksFlash = []
allLinksFlash = getAllLinks('https://www.imdb.com/title/tt3107288/', allLinksFlash)
getDataPoints(allLinksFlash, 'Flash', csvwriter)

#Close file
file_data.close()
