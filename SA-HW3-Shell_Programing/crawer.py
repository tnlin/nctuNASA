#! /usr/local/bin/python
from bs4 import BeautifulSoup
import urllib2
import re
import os
import sys
from os.path import expanduser
try:
    page=urllib2.urlopen(sys.argv[1])
except:
    print "Cannot_Open_URL!"
    sys.exit(0)
#page=urllib2.urlopen('http://rss.cnn.com/rss/edition.rss')
#page=urllib2.urlopen('http://rss.slashdot.org/Slashdot/slashdot')
#page=urllib2.urlopen('http://www.phoronix.com/rss.php')
#page=urllib2.urlopen('http://www.36kr.com/feed/')
soup=BeautifulSoup(page)
home=expanduser("~")
if soup.find_all('item')==[]:
    print "Not_Rss_URL!"
    sys.exit(0)

mypath=home+'//.feed'
if not os.path.exists(mypath):
    os.makedirs(mypath)

fname=str(""+(soup.title.get_text()).encode('utf-8'))
f = open(mypath+"//"+fname,'w')
furl = open(mypath+"//."+fname,'w')
furl.write(sys.argv[1])
#print soup.prettify()
count=1
for each in soup.find_all('item'):
    f.write("item_" + str(each.title.get_text().encode('utf-8'))+"\n")
    f.write(str(each.guid.get_text().encode('utf-8'))+"\n")
    des = each.description.get_text().encode('utf-8')
    f.write(str(re.sub(r"<[^>]*>", "", des ))+"\n")
    count=count+1
