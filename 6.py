from unittest import result
from lxml import etree
import requests
import urllib.request
import time
 
for a in range(5):
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24'
    }
    url='https://movie.douban.com/subject/34925305/comments?start={}&limit=20&status=P&sort=new_score'.format(a*20)
    response = requests.get(url=url,headers=headers)
    html=etree.HTML(response.text)
    divs=html.xpath('//*[@id="comments"]/div')
    for div in divs:
        result=div.xpath('./div/p/span/text()')
        print(result)
        time.sleep(3)
        with open(r"dbmovie11.txt","a",encoding="utf-8") as f:
            f.write("{}".format(result))
            f.write("\n")
