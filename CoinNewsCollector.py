import urllib.request
import json
from pyquery import PyQuery as pq


class coin_info:
    index = 0
    name = ''
    name_en = ''
    name_cn = ''
    price_now = 0.0
    description = ''

    def __init__(self, index = 0, name = '', name_en = '', name_cn = '', price_now = 0.0, count = 0.0):
        self.index = int(index)
        self.name = name
        self.name_en = name_en
        self.name_cn = name_cn
        self.price_now = 0.0 if (price_now=='') else float(price_now)
        self.count = 0.0 if (count=='') else float(count)
        self.official_website = ''
        self.description = ''
    def print(self):
        print("index:%05d  full name:%28s  english name:%8s  chinese name:%8s  price now:%f\ndiscription:%s" %(self.index , self.name ,self.name_en ,self.name_cn ,self.price_now, self.description));
        print("website:%40s"%(self.official_website))


def get_basic_info(page_size = 100, page_start = 0, page_count = 1):
    for page_idx in range(page_start, page_count):
        url = "https://web-market.niuyan.com/web/v1/coins?pagesize="+str(page_size)+"&offset="+str(page_size*page_idx)+"&lan=zh-cn";
        response = urllib.request.urlopen(url)
        print(url)
        if response.status ==200:
            print('get_basic_info success!')
        else:
            print('get_basic_info faild!')
            return
        #print(response.read().decode('utf-8'))
        json_data = json.loads(response.read().decode('utf-8'))
        #print(json_data)
        info = json_data['data']['data']
        #print(info)
        for i in range(0, len(json_data['data']['data'])):
            coin = coin_info(info[i][2], info[i][0], info[i][1], info[i][4], info[i][5], info[i][7]);   
            coin.official_website = get_official_website(coin.name)
            coin.description = get_description(coin.name)
            if coin.description != None:
                filename = "./xxx.csv"
                #asdf = str(11.1)
                with open(filename, 'a') as f:
                    f.write(coin.name+"\t"+coin.name_en+"\t"+coin.name_cn+"\t"+str((coin.price_now*coin.count)/10000)+"\t"+coin.official_website+"\t"+coin.description+"\n") # 写入文件
            coin.print()

#通过coin_name拼接网址，获取官方网站
def get_official_website(coin_name):
    url = "https://niuyan.com/zh/currencies/"+coin_name
    response = urllib.request.urlopen(url)
    print(url)
    if response.status ==200:
        print('get_official_website seccess!')
    else:
        print('get_official_website faild!')
        return
    web_source = response.read().decode('utf-8')
    flag_str = '''"websites":"'''
    index_begin = web_source.find(flag_str, 0)+len(flag_str)
    if index_begin == -1:
        return
    index_end = web_source.find("\"", index_begin)
    if index_end == -1:
        return
    rtn = web_source[index_begin: index_end]
    rtn = rtn.replace("\\u002F", "\\")
    return rtn

def get_description(coin_name):
    url = "https://niuyan.com/zh/currencies/"+coin_name
    response = urllib.request.urlopen(url)
    print("========"+url)
    if response.status ==200:
        print('get_description seccess!')
    else:
        print('get_description faild!')
        return
    web_source = response.read().decode('utf-8')
    flag_str = '''"description":"'''
    index_begin = web_source.find(flag_str)
    if index_begin == -1:
        return
    index_begin += len(flag_str)
    index_end = web_source.find('''","''', index_begin)
    if index_end == -1:
        return
    rtn = web_source[index_begin: index_end]
    if rtn.find("通讯")!=-1:
        return rtn

#get_description("bitcoin")
#一共5000个币左右
#for i in range(0, 50):
#    get_basic_info(i, 100);
#filename = "./xxx.csv"
#with open(filename, 'w') as f:
#    f.write("全名\t英文名\t中文名\t市值\t官网\t简介\n") # 写入文件
get_basic_info(100,21,50)