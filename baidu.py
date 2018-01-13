#爬取百度一下
url = "http://www.baidu.com/s?wd=" + '%E5%A4%AA%E8%B4%B5%E5%95%A6&oq'
resp = urlopen(url)
content = resp.read()
content = content.decode('utf-8')
soup = BeautifulSoup(content,"lxml")
