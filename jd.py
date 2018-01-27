# -*- coding:utf8 -*-
from urllib.request import urlopen
import json
import re
url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv7116&productId=10395413802&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
response = urlopen(url)
page = response.read().decode('gbk')
page = page[26:-2]
page = json.loads(page)
'''
for p in page:
	print(p)
'''
comments = page['comments']
