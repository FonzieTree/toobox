# -*- coding: utf-8 -*-                  
import os
import time
import random                   
from selenium import webdriver              
from selenium.webdriver.common.keys import Keys 
os.chdir(r'...')
browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
browser.get('http://ai.baidu.com/tech/nlp/lexical')
i = 23745
with open('result.txt','a') as file1:
    with open('data.txt','r',encoding='utf-8') as file2:
        data = file2.readlines()
        data = data[i:]
        for line in data:
            try:
                inputElement = browser.find_elements_by_class_name("com-txt")[0]
                line = ''.join(line[17:].strip().split())
                inputElement.clear()
                inputElement.send_keys(line)
                inputElement.send_keys(Keys.ENTER)
                time.sleep(3)
                outputElement = browser.find_elements_by_class_name("result-tips")
                output = ['/'.join(e.text.split('\n')) for e in outputElement]
                output = ' '.join(output)
                print(i, output)
                file1.write(output)
                file1.write('\n')
                file1.flush()
                i += 1
                if output == '':
                    print('Null value')
                    browser.quit()
                    browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
                    browser.get('https://www.sogou.com/')
                    time.sleep(5)
                    browser.get('http://ai.baidu.com/tech/nlp/lexical')
            except:
                print('Exception')
                browser.get('https://www.sogou.com/')
                browser.quit()
                time.sleep(5)
                browser = webdriver.Firefox('D:/Program Files/Mozilla Firefox')
                browser.get('https://www.sogou.com/')
                browser.get('http://ai.baidu.com/tech/nlp/lexical')
print('Done')
