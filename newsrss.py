#!/usr/bin/python

import urllib
from xml.dom import minidom

url = 'http://www.antaranews.com/rss/nas.xml'
xmldoc = minidom.parse(urllib.urlopen(url))  

itemList = xmldoc.getElementsByTagName('item')

print len(itemList) #len = length, banyaknya item, ada 20
for a in itemList : #a adalah iterasi 
	print a.childNodes[2].nodeName		#dapetin nama tag
	print a.childNodes[1].childNodes[0].nodeValue		#dapetin isi tag
	print a.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue 

# ./newsrss.py
# childNodes[0] spasi atau enter
# childNodes[1].nodeName = nama tag item <title>
# childNodes[1].nodeValue = ga ada apa2nya 
# childNode[1].childNode[0].nodeValue = isi dari title <MPR Blablabla>
# ganjil isi, genap spasi

#pr: cari 24 jam terakhir sama selalu update 5 menit sekali

