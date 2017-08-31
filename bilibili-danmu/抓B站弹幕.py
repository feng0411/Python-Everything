import re
import requests
from bs4 import BeautifulSoup
import pymysql


def get_url():
    #阅后即瞎列表
    url_list = ['https://www.bilibili.com/video/av13925037/',
                    'https://www.bilibili.com/video/av13638713/',
                    'https://www.bilibili.com/video/av13368026/',
                    'https://www.bilibili.com/video/av13072404/',
                    'https://www.bilibili.com/video/av12807059/',
                    'https://www.bilibili.com/video/av12538898/',
                    'https://www.bilibili.com/video/av12294146/',
                    'https://www.bilibili.com/video/av12079240/',
                    'https://www.bilibili.com/video/av11855371/',
                    'https://www.bilibili.com/video/av11643925/',
                    'https://www.bilibili.com/video/av11456402/',
                    'https://www.bilibili.com/video/av11274857/',
                    'https://www.bilibili.com/video/av11119815/'
                    ]
    #遍历列表
    for i in url_list:
        get_danmu(i)
    
 
def get_danmu(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',}
    #打开上面列表的地址
    r = requests.get(url=url,headers=headers)
    #获得cid参数值
    cid = re.findall(r'cid=(.*?)&aid=',r.text)[0]
    #获得弹幕文件的地址
    dmurl = 'http://comment.bilibili.com/'+str(cid)+'.xml'
    #分析弹幕文件
    dmhtml = requests.get(dmurl).text
    soup = BeautifulSoup(dmhtml,'xml')
    dmlist = soup.find_all('d')
    save_danmu(dmlist)    
    
def save_danmu(dmlist):
    for dm in dmlist:
        message = str(dm.string)
        connection = pymysql.connect(
                            host='XXXX',  # 连接你的数据库
                            user='XXXX',        # mysql用户名
                            passwd='XXXX',  # 密码
                            db='XXXX',      # 数据库名字
                            charset='utf8mb4',     # 编码方式
                            cursorclass=pymysql.cursors.DictCursor)
      
        with connection.cursor() as cursor:
        # 创建更新值的sql语句
            sql = "INSERT INTO 阅后即瞎弹幕(message) VALUES (%s)"
            cursor.execute(sql,(message))

        # 提交本次插入的记录
            connection.commit()
    
 
if __name__ == "__main__":
    get_url()
