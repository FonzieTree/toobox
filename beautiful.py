#! /usr/bin/python
# -*- coding:utf-8 -*- 
# press f12, then change data and header
import requests
from bs4 import BeautifulSoup
import time
import random
result = []
data={
            'type':'all',
            'content':''
}
header={
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive',
            'Content-Length':'665',
            'Content-Type':'application/x-www-form-urlencoded',
            'Cookie':'JSESSIONID=2DC55A1B32F978B1FADDA926F5549F2D; JSESSIONID=ED74A28FAD51091385C4C959E2E8FA1B',
            'Host':'ictclas.nlpir.org',
            'Origin':'http://ictclas.nlpir.org',
            'Referer':'http://ictclas.nlpir.org/nlpir/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'X-Requested-With':'XMLHttpRequest'
}
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()
def cncorpus(args):
    data['TextBoxWord'] = args
    try:
        html1 = requests.post('http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do', data = data)
        html = html1.text    
        soup = BeautifulSoup(html,"lxml")
        return(eval(soup.get_text())['dividewords'])
fo = open("../prepare.txt", "r")
file=open('output.txt','w') 
for line in fo.readlines():                          
    time.sleep(random.randint(1,10))
    line = line.strip()                              
    args = line.split()[0]
    corpus = cncorpus(args)
    result.append(corpus)
    file.write(corpus)
    file.write("\n")
    file.flush()
    print(result)
fo.close() 
file.close()  
