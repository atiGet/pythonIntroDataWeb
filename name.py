#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, 
#follow that link and repeat the process a number of times and report the last name you find.

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL - ')
count = raw_input('Enter Count - ')
count=int(count)

position = raw_input('Enter position - ')
position=int(position)
print "Retrieving ", url

while count !=0:
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	tags = soup('a')
	url=tags[position-1].get('href',None)
	print "Retrieving ", url
	
	count=count-1

