import urllib2
from bs4 import BeautifulSoup

page1 = urllib2.urlopen(raw_input("Page 1:"))
page2 = urllib2.urlopen(raw_input("Page 2:"))

soup_page1 = BeautifulSoup(page1.read())
soup_page2 = BeautifulSoup(page2.read())

a_page1 = [];a_page2 = []
p_page1 = [];p_page2 = []
print "From page 1"
for page in soup_page1.findAll('a',href = True):
    a_page1.append(page['href'])

print "From page 2"
for page in soup_page2.findAll('a',href=True):
    a_page2.append(page['href'])

same = 0
for a in a_page1:
    for b in a_page2:
        if (a == b):
            same+=1
print float(float(same)/float(len(a_page1)+len(a_page2)))
