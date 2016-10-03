#looping through a string
fruit='banana'
index=0
while index<len(fruit):
	letter=fruit[index]
	print index,letter


#looping through a string and counting 'a'

word='banana'
count=0

for letter in word:
	if letter=='a':
	count=count+1
print count