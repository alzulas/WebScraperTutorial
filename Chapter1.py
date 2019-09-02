#Example 1

'''
from urllib.request import urlopen

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
'''
#Excerpt From: Ryan Mitchell. “Web Scraping with Python.” Apple Books. 


#Example 2 with Beautiful Soup 4

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
'''
#Excerpt From: Ryan Mitchell. “Web Scraping with Python.” Apple Books. 

#Example 3 with error handling

'''
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the  
    # exception catch, you do not need to use the "else" statement”
'''

'''
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
except HTTPError as e:
	print("The server returned an HTTP error")
except URLError as e:
	print("The server could not be found!")
else:
	print(html.read())
	'''

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

#Excerpt From: Ryan Mitchell. “Web Scraping with Python.” Apple Books. 


#Extra code exerts found at https://github.com/REMitchell/python-scraping/blob/master/Chapter01_BeginningToScrape.ipynb

