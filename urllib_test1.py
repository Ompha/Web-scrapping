import urllib
fhand = urllib.urlopen('http://www.uclago.com/go-terms.html')

for line in fhand:
	line = line.rstrip()
	num = re.findall('-([a-z]+)',line)
	num_org.extend(terms)
print "the go terms are: ",terms
	print line.strip()	