# -*- coding:utf8 -*-
from urllib import request
from urllib.parse import urlencode
from urllib.request import urlopen
if __name__ == '__main__':
    params = urlencode({ 
        'Email' : '2473263557@qq.com',
        'api_key' : 't1P589L3I6OxOTgYTdimHajpOBLELSJNLqlTscCd',
        'text' : '我是中国人。',
        'pattern' : 'dp',
        'format' : 'plain'
    })
    url = "http://api.ltp-cloud.com/analysis/?" + params
    resp = urlopen(url)
    content = str(resp.read().decode('utf-8').strip())
    print(content)
