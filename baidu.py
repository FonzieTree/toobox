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
#! /usr/bin/python
# -*- coding:utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import re
def baidu(data):
    html = requests.post('http://hanyu.baidu.com/zici/s?wd='+data+'&query='+data+'&srcid=28232&from=kg0&from=kg0')
    html.encoding = html.apparent_encoding 
    html = html.text
    soup = BeautifulSoup(html,"lxml")
    result = soup.p.contents[0]
    result, num = re.subn(string = result,pattern = '1.',repl = '')
    return(data + '，' + result)
i = 0
with open(r'../input.txt','r',encoding='utf-8') as file:
    with open('../output.txt','w', encoding='utf-8') as baiducidian:
        chars = file.readlines()
        for char in chars:
            data = char.strip()
            line = baidu(data)
            baiducidian.write(line)
            baiducidian.write("\n")
            baiducidian.flush()
            i += 1
            print(i)
