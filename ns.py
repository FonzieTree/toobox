# -*- coding:utf8 -*-
from urllib import request
from urllib.parse import urlencode
from urllib.request import urlopen
import urllib
response=urlopen("http://www.grcbank.com/")
page=response.read()
pos=page.find("<a href=\"")
while ~pos:
    page=page[pos+9:]
    lim=page.find('\"')
    print "You've found a link:%s"%page[:lim]
    pos=page.find("<a href=\"")
