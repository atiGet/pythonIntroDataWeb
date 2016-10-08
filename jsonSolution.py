import json
import urllib

sum=0

url = raw_input('Enter URL: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data

info = json.loads(str(data))
print 'User count:', len(info["comments"])

for item in info["comments"]:	
	count=int(item["count"])
	sum=sum+count

print 'sum: ',sum