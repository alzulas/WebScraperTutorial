#1
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, "html.parser")

nameList = bs.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
'''

'''
#2
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
#print([title for title in titles])
#3
allText = bs.find_all('span', {'class':{'green', 'red'}})
#print([text for text in allText])
'''

'''
#4
nameList = bs.find_all(text='the prince')
#print(len(nameList))
#5
title = bs.find_all(id='title', class_='text')
print([text for text in allText])
'''

'''
#6
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
'''


'''
#7
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)
'''

'''
#8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'})
      .parent.previous_sibling.get_text())
'''


#'''
#9
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
for image in images: 
    print(image['src'])
#10
something = bs.find_all(lambda tag: len(tag.attrs) == 2)
for thing in something:
	print(thing)
#'''

#'''
#11
bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
#'''

#'''
#12
bs.find_all('', text='Or maybe he\'s only resting?')
#'''

#Extra code found at https://github.com/REMitchell/python-scraping/blob/master/Chapter02-AdvancedHTMLParsing.ipynb