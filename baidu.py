#爬取百度一下
# -*- coding:utf8 -*-
from urllib import request
from urllib.parse import urlencode
from urllib.request import urlopen
data = urlencode({'wd':'你'})
url = "http://www.baidu.com/s?" + data
resp = urlopen(url)
content = resp.read()
content = content.decode('utf-8')
soup = BeautifulSoup(content,"lxml")
