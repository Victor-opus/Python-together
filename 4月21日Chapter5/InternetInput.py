import urllib2
file = urllib2.urlopen('http://helloworldbook.com/sande2/data/message.txt')
message = file.read()
print message
