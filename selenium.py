# -*- coding: utf-8 -*-                  
import re                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
browser.get('http://ai.baidu.com/tech/nlp/lexical')  
inputElement = browser.find_elements_by_class_name("com-txt")[0]
inputElement.send_keys('慕尼黑再保险公司不仅是此类行动的倡议者，更是将其大量气候数据整合进保险产品中，并与公众共享大量天气信息，参与到新能源领域的保障中。')
inputElement.send_keys(Keys.ENTER)
outputElement = browser.find_elements_by_class_name("result-left")[0]
text = outputElement.text
