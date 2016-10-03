#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = raw_input("Enter file:")
emailDic=dict()
words=list()
bigEmail=None
bigValue=None

if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
handl=handle.read()
for line in handl:
    if not 'From'in line:continue
    lines=line.split()
    words.append(lines[1])
    
for word in words:
    emailDic[word]=emailDic.get(word,0)+1
    
for email,amount in emailDic.items():
    if bigValue is None or amount>bigValue:
        bigValue=amount
        bigEmail=email
        
print bigEmail,bigValue

