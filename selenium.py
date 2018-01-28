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
import re
import os
import time                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
os.chdir(r'..')
browser = webdriver.Firefox('./Mozilla Firefox')
browser.get('http://ai.baidu.com/tech/nlp/lexical')  
inputElement = browser.find_elements_by_class_name("com-txt")[0]
inputElement.clear()
with open('result.txt','w') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        for line in data:
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
            print(output)
print('Done')
