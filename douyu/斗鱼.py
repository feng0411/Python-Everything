import requests
import re
import time
from bs4 import BeautifulSoup
import pymysql
from datetime import datetime

def open_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text

def scrapy(url):
    infos = []
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('ul',id='live-list-contentbox')
    every = total.find_all('li',attrs={'data-rpos':'0','data-sub_rt':'0'})
    for li in every:
        #定义一个空字典
        info = {}
        info['title'] = li.find('h3').text.strip()#找到标题
        info['type'] = li.find('span',class_='tag ellipsis').text.strip()#找到直播版块
        info['host'] = li.find('span',class_='dy-name ellipsis fl').text.strip()#找到主播
        now = datetime.now()
        num = li.find('span',class_='dy-num fr').text
        if '万' in num:
            num1 = num.replace('万','')
            if '.' in num1:
                num2 = float(num1)*10000
                info['viewer'] = num2 
            else:
                num2 = int(num1)*10000
                info['viewer'] = num2
        else:
            info['viewer'] = num
        #直播间地址
        info['link'] = 'https://www.douyu.com/'+str(li.find('a',class_='play-list-link')['href'])
        #当前时间
        info['time'] = now
        infos.append(info)
        print ('一个房间的数据抓取完成')
    return infos

def PrintFile(dict):
    for want in dict:
        title = want['title']
        type = want['type']
        link = want['link']
        host = want['host']
        time = want['time']
        viewer = want['viewer']
        # 和本地的数据库建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',        # mysql用户名
            passwd='XXXX',  # 密码
            db='XXXX',      # 数据库的名字
            charset='utf8',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
      
        with connection.cursor() as cursor:
            # 创建更新值的sql语句
            sql = "INSERT INTO 斗鱼(title,type,link,host,viewer,time) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(title,type,link,host,viewer,time))

            # 提交本次插入的记录
            connection.commit()
        
    connection.close()
    print('所有直播间信息爬取完成')

def main(url):
    content = scrapy(url)
    PrintFile(content)
    print('所有的信息都已经保存完毕！')

url = 'https://www.douyu.com/directory/all'

if __name__ == '__main__':
    for i in range(1,20):
        main(base_url)
        #抓取一次之后休眠半个小时
        time.sleep(1800)
