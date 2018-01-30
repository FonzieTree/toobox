# -*- coding: utf-8 -*-                  
import re                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
browser.get('http://ai.baidu.com/tech/nlp/lexical')  
inputElement = browser.find_elements_by_class_name("com-txt")[0]
inputElement.clear()
inputElement.send_keys('中文分词项目(开源/API接口)总结 - CSDN博客')
inputElement.send_keys(Keys.ENTER)
outputElement = browser.find_elements_by_class_name("result-tips")
output = [e.text for e in outputElement]
print(output)



# -*- coding: utf-8 -*-                  
import os
import time
import random                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
os.chdir(r'D:\wang\国家语委')
browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
i = 0
with open('result.txt','a') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        data = data[i:]
        for line in data:
            browser.get('https://www.sogou.com/')
            browser.get('http://ai.baidu.com/tech/nlp/lexical')
            inputElement = browser.find_elements_by_class_name("com-txt")[0]
            time.sleep(1)
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
            #if i % 500 == 0:
            #    time.sleep(3600)	
            print(i, output)
print('Done')
