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

#百度依存句法分词
# -*- coding: utf-8 -*-                  
import os
import time
import random                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
os.chdir(r'./')
browser = webdriver.Firefox('./Mozilla Firefox')
browser.get('http://ai.baidu.com/tech/nlp/lexical')  
inputElement = browser.find_elements_by_class_name("com-txt")[0]
i = 0
with open('result.txt','a') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        for line in data:
            time.sleep(random.uniform(1,5))
            line = ''.join(line[17:].strip().split())
            inputElement.clear()
            inputElement.send_keys(line)
            inputElement.send_keys(Keys.ENTER)
            outputElement = browser.find_elements_by_class_name("result-tips")
            output = ['/'.join(e.text.split('\n')) for e in outputElement]
            output = ' '.join(output)
            file1.write(output)
            file1.write('\n')
            file1.flush()
            i += 1
            if i % 500 == 0:
                time.sleep(360)	
            print(output)
            
print('Done')

#爬取百度翻译
# -*- coding: utf-8 -*-                  
import os
import requests
import json
url= 'http://fanyi.baidu.com/transapi/?aldtype=16047&from=zh&to=yue&query='
i = 0
with open('yueyu.txt','a') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        diction = []
        for line in data:
            line = ' '.join(line[17:].strip().split())
            diction.append(line)
        diction = ' '.join(diction).split(' ')
        diction = set(diction)
        for element in diction:
            r = requests.get(url+element)
            output = json.loads(r.text)['data'][0]['dst']
            file1.write(element+' '+output)
            file1.write('\n')
            file1.flush()
            print(i,' 原文: '+element+' 翻译：'+output)
            i += 1
print('Done')

#采用API+selenium爬取百度演示收费版的依存句法分词分析
# -*- coding: utf-8 -*-                  
import json                   
from selenium import webdriver              
browser = webdriver.Firefox('../Mozilla Firefox')
i = 0
with open('result.txt','a') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        data = data[i:]
        for line in data:
            try:
                line = ''.join(line[17:].strip().split())
                browser.get('http://ai.baidu.com/aidemo/?apiType=nlp&type=lexer&t1='+line)
                output= browser.find_elements_by_css_selector("pre")[0]
                output = json.loads(output.text)
                output = output['data']['items']
                output = [o['item']+'/'+o['pos'] for o in output]
                output = ' '.join(output)
            except:
                print('No')
print('Done')
