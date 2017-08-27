import requests
import re
import time
from bs4 import BeautifulSoup
import os

def open_html(url):
    try:
        r = requests.get(url)
        r.encoding = 'gbk'
        return r.text
    except:
        return " ERROR "

def download_pic(url):
    html = open_html(url)
    soup = BeautifulSoup(html, 'lxml')
    #找到所有吉他谱信息所在位置
    pu_list = soup.find_all('ul',class_='zhuantishuang')
    for pu in pu_list:
        song_list = pu.find_all('li')
        for song in song_list:
            #找到每一首歌的吉他谱的网址
            link = 'http://www.yinyuezj.com' + str(song.a['href'])
            #吉他谱名称
            title = song.a['title']
            #图片保存路径
            path = ('C:/Users/Administrator/Desktop/编程/jitapupic/'+title)
            #以path为路径新建一个文件夹
            os.makedirs(path)
            x = 0
            #开始分析每一个吉他谱的网址
            phtml = open_html(link)
            psoup = BeautifulSoup(phtml,'lxml')
            try:
                pic_list = psoup.find('ul',class_='tujishuchu')
                pics_list = pic_list.find_all('li')
                for pics in pics_list:
                    #找到图片信息
                    img = pics.find('a')['href']
                    #下载图片的模板
                    with open(path+'/'+str(x)+'.jpg','wb+') as f:
                        f.write(requests.get(img).content)
                        print('该吉他谱图片已下载')
                    #这里需要注意，因为一首歌的吉他谱可能有多张，
                    #但是如果图片重名，新下载的会覆盖前一张，所以要改名字，
                    #用x命名，每下载一张x都会加1
                    x+=1
            except:
                print('下载出错啦')

def main(base_url):
    content = download_pic(base_url)
    print('所有的吉他谱都下载完了！')
base_url = 'http://www.yinyuezj.com/jita/pu/wuyuetian.html'

if __name__ == '__main__':
    main(base_url)
