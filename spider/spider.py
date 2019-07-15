import urllib2
'''
response =  urllib2.urlopen("http://www.baidu.com")
html = response.read()
print html
'''
req = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(req)
my_page = response.read()
print my_page


