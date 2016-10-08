import urllib
import xml.etree.ElementTree as ET

sum=0

url = raw_input('Enter URL: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

#.// takes direcctly to the prefered node
counts = tree.findall('.//count')
for item in counts:	
	count=int(item.text)
	sum=sum+count

print 'sum: ',sum

