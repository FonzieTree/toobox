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
text = soup.get_text().split()


#爬取百度字典
#! /usr/bin/python
# -*- coding:utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import time
import random
result = []
html = requests.post('http://hanyu.baidu.com/zici/s?wd='+'百'+'&query='+'百'+'&srcid=28232&from=kg0&from=kg0')
html.encoding = html.apparent_encoding 
html = html.text
soup = BeautifulSoup(html,"lxml")
text = soup.find_all('div', class_='tab-content')
BeautifulSoup(content,"lxml")
