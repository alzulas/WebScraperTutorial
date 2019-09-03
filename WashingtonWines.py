from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import json
import csv

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

# create the csv writer object
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


html = urlopen('https://www.washingtonwine.org/api/queries/entities?getcount=true&types=Winery&getwines=true&getlogo=true&getregion=true&query=')

#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#bs = BeautifulSoup(html.read(), "html5lib")

data = json.load(html)
#print(json.dumps(data, indent = 4, sort_keys=True))
#/Users/leahz/Documents/Developer/WebScraperTutorial/WebScraperTutorial


#employee_parsed = json.loads(employee_data)

all_wineries = data['data']





#html = urlopen('https://www.washingtonwine.org/api/queries/entities/')
#print(html.read())

'''<div class="uk-flex uk-flex-middle uk-width-1-1 entity-header">
      <figure class="entity-figure uk-flex uk-flex-center">
        <img src="https://wswc-1290.kxcdn.com/_assets/a7386707f7143d5f583a4f4b3084fbe2/FTH Winery Logo Color (430pix).jpg?t=small-thumb">
      </figure>
      <div class="uk-flex uk-flex-column uk-width-1-1">
        <h5>Prosser</h5>
        <h3 class="alternate"><a href="https://www.washingtonwine.org/wineries/14-hands-winery/" class="js-send-to-detail">14 Hands Winery</a></h3>
          <div class="uk-flex uk-flex-middle wines-toggle uk-accordion-title">
            <i class="icon-simple_wine_glass"></i>
            <h4 class="uk-margin-remove">14 wines</h4>
            <i class="icon-accordion-arrow"></i>
          </div>
      </div>
    </div>'''

    #id="list-switcher"

'''title = getTitle("https://www.washingtonwine.org/wineries")
if title == None:
    print("Title could not be found")
else:
    print(title.get_text())
    profileUrl
'''


# links = bs.find_all('id':'profileUrl')
# print(links)
# for link in links: 
#     print(link['href'])

#\.\.\/img\/gifts/img.*\.jpg
#print(bs.find('ul',{'id':'list-switcher'}).li.next_siblings)
# ul class="js-list-content list-content uk-list uk-flex uk-flex-column uk-width-5-6"
# class="uk-flex uk-flex-column entity uk-accordion uk-position-relative"

#for child in bs.find('ul',{'id':'list-switcher'}).li.next_siblings:
#    print(child)

#nameList = bs.findAll(class_="uk-flex uk-flex-middle uk-width-1-1 entity-header").children
#for name in nameList:
#    print(name)