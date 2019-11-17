# 区块链部分
## 采集所有区块链币种信息
运行
```
python3 CoinNewsCollector.py
```
能够采集到每个币种的
```
名称
英文名
中文名
市值排名
官方网站
介绍
```

## 采集区块链新闻
目前的新闻来源为
```
链闻
8btc
区势传媒
金色财经
链向财经
```
运行
```
python3 news_crawl.py
```
能够抓取到近期的所有新闻，其中包括
```
新闻标题
发布时间
简介
作者
媒体来源
新闻源地址
新闻内容
```


##  分析区块链新闻高频词
在抓取了币种信息和新闻信息后，能够对词进行频率分析

# 下版本目标
建立网站前端