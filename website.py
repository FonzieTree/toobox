# -*- coding:utf8 -*-
import requests  
from bs4 import BeautifulSoup  
from urllib import request
import os
os.chdir('D:\\wang\\grcbank')
r=requests.get("...")  
r.encoding=r.apparent_encoding  
file = open('result.txt','w')
for link in soup.find_all('a'):
    link = link.get('href')
    if 'http://' in link or 'https://' in link:
        r = requests.get(link)
	elif link is not None and link != '###':
        r = requests.get('...' + link)
    r.encoding=r.apparent_encoding  
    text=r.text   
    soup = BeautifulSoup(text, "lxml")
    result = soup.get_text()
    result = result.split()
    for line in result: 
        try:
            file.write(line)
            file.write("\n")
            file.flush()
        except:
            pass
        i += 1
        print(i, '	finished!') 
