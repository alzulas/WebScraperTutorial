from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import json
import csv


#Example 1 All links on page




'''
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


def getAllLinks(firstLink, allLinks):
    html = urlopen(firstLink)
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/title/)(.)*(/episodes)(.)(season)(.)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            allLinks.append(link.attrs['href'])
    return(allLinks)

def getDataPoints(allLinks, show, csvwriter):
    for link in allLinks:
        html = urlopen("https://www.imdb.com" + link)
        bs = BeautifulSoup(html, "html.parser")
        strong_tag = bs.find('div', {'id':'episodes_content'}).find_all('strong')
        airdates = bs.find_all(class_='airdate')
        #print (strong_tag)
        for i in range(0, len(airdates)):
            print("Show = " + show + ", Season = " + strong_tag[len(airdates)].text + ", Episode " + str(i+1) + " = " + strong_tag[i].text + ', ' + airdates[i].text[13:-5])
            tmpRow = [show, strong_tag[len(airdates)].text, str(i+1), strong_tag[i].text, airdates[i].text[13:-5]]
            #print (tmpRow)
            csvwriter.writerow(tmpRow)
        #print("Season = " + strong_tag[len(airdates)].text + '\n')

header = ['Show', 'Season', 'Episode Number', 'Episode Title', 'Airdate']
file_data = open('/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial/allDCUniverseEpisodes.csv', 'w')
csvwriter = csv.writer(file_data)
csvwriter.writerow(header)
print(header)


allLinksSuperGirl = []
allLinksSuperGirl = getAllLinks('https://www.imdb.com/title/tt4016454/', allLinksSuperGirl)
getDataPoints(allLinksSuperGirl, 'Super Girl', csvwriter)


allLinksArrow = []
allLinksArrow = getAllLinks('https://www.imdb.com/title/tt2193021/', allLinksArrow)
getDataPoints(allLinksArrow, 'Arrow', csvwriter)

allLinksLegends = []
allLinksLegends = getAllLinks('https://www.imdb.com/title/tt4532368/', allLinksLegends)
getDataPoints(allLinksLegends, 'Legends of Tomorrow', csvwriter)

allLinksFlash = []
allLinksFlash = getAllLinks('https://www.imdb.com/title/tt3107288/', allLinksFlash)
getDataPoints(allLinksFlash, 'Flash', csvwriter)

file_data.close()



            
'''
id="episodes_content"
find('div', {'id':'bodyContent'}).find_all

#for strong_tag in soup.find_all('strong'):
#    print(strong_tag.text, strong_tag.next_sibling)


#<a href="/title/tt4525842/?ref_=ttep_ep1" title="Pilot" itemprop="name">Pilot</a>

#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#bs = BeautifulSoup(html.read(), "html5lib")

#data = json.load(html)
#print(json.dumps(data, indent = 4, sort_keys=True))
#/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial

#listOfWineNames = getUniqueWineTypes(data)
#print (listOfWineNames)

#writeToFile(data, listOfWineNames)

'''