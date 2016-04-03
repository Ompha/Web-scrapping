import re
num_org = []
searchtext = open('regex_sum_216065.txt')
for line in searchtext:
	line = line.rstrip()
	num = re.findall('[0-9]+',line)
	num_org.extend(num)
print "the num array is: ",num_org
length_array = len(num_org)
num_sum = 0
for i in range(0,length_array):
	num_sum = num_sum + int(num_org[i])
print "sum is ", num_sum
print "the length of array is: ", length_array
