#! /usr/bin/python
# -*- coding:utf-8 -*- 
import requests
from bs4 import BeautifulSoup
data={
'type':'all',
'content':''
            }
header={
'Connection':'keep-alive',
'Content-Type':'text/html;charset=UTF-8',
'Server':'nginx/1.9.3',
'Transfer-Encoding':'chunked',
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length':'858',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'JSESSIONID=F59B0CD1162D1E5FB262E3FAE2E96E48; JSESSIONID=ED74A28FAD51091385C4C959E2E8FA1B',
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
    data['content'] = args
    try:
        html1 = requests.post('http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do', data = data)
        html = html1.text    
        soup = BeautifulSoup(html,"lxml")
        return(eval(soup.get_text())['dividewords'])
    except:
        return(args)
# process
fo = open("../input.txt", "r")
file=open('cas.txt','w')
i = 0 
for line in fo.readlines():                         
    line = line.strip()                              
    args = '正正正正正正正正正正正正正正正正正正正正正正正正正正正正正正'+line.split()[0]
    corpus = cncorpus(args)[120:]
    file.write(corpus)
    file.write("\n")
    file.flush()
    i += 1
    print(i)
fo.close() 
file.close()
