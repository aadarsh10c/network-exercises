#retrieve the data for romeo.txt and compute the frequency of each word in the file
import urllib.request

host_name='http://data.pr4e.org/romeo.txt'

fHand = urllib.request.urlopen(host_name)

count={}

for line in fHand:
    line=line.decode().split()
    print(line)
    for word in line:
        count[word]=count.get(word,0)+1

print(count)    
