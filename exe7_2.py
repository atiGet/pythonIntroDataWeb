# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    number=line.split()
    number=number[1]
    number=float(number)
    total=total+number
print 'Average spam confidence:',total/count
