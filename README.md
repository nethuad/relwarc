#爬虫
xpath : https://www.w3.org/TR/xpath/all/

https://zhuanlan.zhihu.com/p/26395979

http://www.cnblogs.com/cnkai/p/7400467.html

http://docs.python-requests.org/zh_CN/latest/


# scrapy
https://scrapy.org/
https://docs.scrapy.org/en/latest/
http://scrapy-chs.readthedocs.io/zh_CN/0.24
https://docs.scrapy.org/en/latest/topics/shell.html


# 开始
1.创建项目 tutorial
scrapy startproject tutorial

2.创建 Spiders
cd crawler/tutorial

scrapy genspider example example.com # 利用模板创建
crawler/tutorial/tutorial/spiders/quotes_spider.py # 教程示例
crawler/tutorial/tutorial/spiders/p2peye.py # p2peye.com

3. 执行
cd crawler/tutorial

scrapy crawl quotes

scrapy crawl p2peye
scrapy crawl p2peye -o p2peye.json 
scrapy crawl p2peye -o p2peye.jl

# scrapy shell

scrapy shell '<url>'
    


# jupyter
```py
import requests
from scrapy.http import TextResponse
r = requests.get('http://stackoverflow.com/')
response = TextResponse(r.url, body=r.text, encoding='utf-8')
```


# 实例


cookie：http://python.jobbole.com/88478/

https://www.cnblogs.com/lei0213/p/6957508.html

https://www.cnblogs.com/lilinwei340/p/6417689.html

http://www.cnblogs.com/lei0213/p/8393323.html

知乎： https://github.com/Andrew-liu/scrapy_example

https://segmentfault.com/q/1010000008566414



参考http://www.cnblogs.com/cnkai/p/7401526.html
http://bigwayseo.com