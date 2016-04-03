import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = raw_input('Enter count:')
pos = raw_input('Enter position:')
pos = int(pos) -1
html = urllib.urlopen(url).read()
temp_html = html

for x in range(0, int(count)):
	soup = BeautifulSoup(temp_html)

# Retrieve all of the anchor tags
	tags = soup('a')
	temp_url = tags[pos].get('href', None)
	temp_html = urllib.urlopen(temp_url).read()
	if x < int(count)-1:
		print 'Retrieving:', tags[pos].get('href', None)
	elif x == int(count)-1:
		print 'last url:', tags[pos].get('href', None)