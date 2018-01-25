#基本用法
import re
data = '你/n 在/nn 【干 啥】/yy 啊/yy '
s1 = re.findall(r'\w+/n ', data)
s2 = re.findall(r'\w+/nn ', data)
s3 = re.findall(r'\w+/yy ', data)
s4 = re.findall(r'\【.*\】/yy ', data) + re.findall(r'\w+/yy ', data)

#爬虫清晰
from bs4 import BeautifulSoup
import requests
import re
data={
'TextBoxCCkeywords':'你',
'__VIEWSTATE':'/wEPDwUKLTQzNTczMjk0OA9kFgICAw9kFgQCEw8PFgIeB1Zpc2libGVnZBYOAgEPDxYCHgRUZXh0ZWRkAgMPDxYCHwEFOuesrDHliLA1MDDmnaHvvIzlhbHmn6Xor6LliLA0Njk2NeadoeespuWQiOimgeaxgueahOS+i+WPpSFkZAIFDw8WAh8AaGRkAgcPDxYCHwBoZGQCCQ8PFgIfAGdkZAILDw8WAh8AZ2RkAg0PDxYCHwBnZGQCFg8PFgIfAGdkFg4CAQ8PFgIfAGhkZAIDDw8WAh8AaGRkAgUPDxYCHwBnZGQCBw8PFgIfAGdkZAIJDw8WAh8BBQExZGQCCw8PFgIfAQUCOTRkZAINDw8WAh8BBQU0Njk2NWRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYKBQtSQmluZGV4d29yZAUKUkJsaWtlbW9kZQUKUkJsaWtlbW9kZQUOUkJmdWxsdGV4dG1vZGUFDlJCZnVsbHRleHRtb2RlBQxSYWRpb0J1dHRvbjMFDFJhZGlvQnV0dG9uMwUMUmFkaW9CdXR0b240BQ5DaGVja0JveENodWNodQUQQ2hlY2tCb3hLV0lDbW9kZffW2g1Byq2U6t3CNdjnRknms8kcMgxOSrj6pzcEb7+L',
'__EVENTVALIDATION':'/wEWFQKqgaWNDwLYiuv/CwLzuO7zDQL3uO7zDQLV+YmkCgLZ+YmkCgKM54rGBgK8u9naBwKJlM7DBwKAg8rcDgKWzvT1CAKWzuCuBwK2q5qHDgK/xfDTAQLxqL+hAgLCpJSTBQKKn9X3AwKLlOLCBgLc/9LTBQL3t9jyBALZu+PjB8uMmbvu0DTNW/3q35pA7MluGRF8mSx4sI8DfX5BZszw',
'TextBoxCCkeywords':'不',
'DropDownListPsize':'10',
'Button1':'检  索',
'1':'RBindexword',
'2':'RadioButton4',
'CheckBoxChuchu':'on',
}
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '1108',
'Cache-Control': 'max-age=0',
'Origin': 'http://www.aihanyu.org',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://www.aihanyu.org/cncorpus/CnCindex.aspx',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': '__utma=199816254.2093234155.1513664693.1514527072.1516088538.12; __utmz=199816254.1516088538.12.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ASP.NET_SessionId=0iwbkavqypz0jjyd2dratwgv'
}
html = requests.post('http://www.aihanyu.org/cncorpus/CnCindex.aspx', data = data, headers = headers)
html = html.text    
soup = BeautifulSoup(html,"lxml")
text = soup.get_text()
re.findall(r'\n\n\d+(.*)',text)
