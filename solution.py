#The program will use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the span tags
tags = soup('span')
count=0
sum=0
for tag in tags:
    # counts the number of comments
	count=count+1
	comment=tag.contents[0]
	sum=sum+int(comment)
	
print 'Count ',count
print 'Sum ',sum