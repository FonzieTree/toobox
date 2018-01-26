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
