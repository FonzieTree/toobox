# -*- coding:utf8 -*-
import requests
import json
import csv
idx = '546724870335'
page = 1
with open('546724870335.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['date','content','rateId','user_nick','user_rank','user_vipLevel','auction_link','auction_aucNumId','auction_sku'])
    while(1):
        url = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+idx+'&currentPageNum=' + str(page)
        res = requests.get(url)
        jc = json.loads(res.text.strip().strip('()'))
        if jc['total'] == 0:
            print('Done')
            break
        else:
            jc = jc['comments']
            for j in range(len(jc)):
                date = jc[j]['date']
                content = jc[j]['content']
                rateId = jc[j]['rateId']
                user_nick = jc[j]['user']['nick']
                user_rank = jc[j]['user']['rank']
                user_vipLevel = jc[j]['user']['vipLevel']
                auction_link = jc[j]['auction']['link']
                auction_aucNumId = jc[j]['auction']['aucNumId']
                auction_sku = jc[j]['auction']['sku']
                writer.writerow([date, content, rateId, user_nick, user_rank, user_vipLevel, auction_link, auction_aucNumId, auction_sku])
        print(page, ' pages finished')
        page += 1
        
