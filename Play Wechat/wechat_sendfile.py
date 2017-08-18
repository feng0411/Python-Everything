import re
import time
import itchat
from itchat.content import *
import os
#import pypinyin
import easygui as g


first = g.msgbox(msg='''该程序的主要功能是微信手机端操纵电脑发送文件，基本步骤如下：

①：选择一个你常用文件的存放文件夹

②：选择完成后会弹出一个二维码，用手机扫描后即可完成微信登陆(仅限第一次使用，之     后将不需扫描二维码,但是不要删除自动生成的.pkl文件)

③：在微信中向自己的微信号(必须是向自己的账号)发送"文件"二字，即可获得选择路径下    所有的文件名

④：向自己的微信号发送任一文件名，文件传输助手即可收到该文件

⑤：若要结束程序，在手机端退出登录即可''',title='感谢使用python微信小助手')
second = g.diropenbox(msg='请选择一个你常用文件的存放文件夹')
@itchat.msg_register([TEXT])
def text_reply(msg):
    
    friend = itchat.search_friends(userName=msg['FromUserName'])
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    #两个条件同时成立，发件人和收件人都是自己
    if  msg['ToUserName'] == myUserName and msg['FromUserName'] == myUserName:
        if msg['Text'] == '文件':
            #获取当前目录所有文件
            b = os.chdir(second)
            r = os.listdir()
            for i in r:
                itchat.send(i,toUserName=myUserName)
        else:
            file_name = msg['Text']
            #中文换拼音
            q = '-'.join(pypinyin.lazy_pinyin(file_name))
            old_path = second+'//'+file_name
            new_path = second+'//'+q
            #改名字
            os.rename(old_path,new_path)
            #路径不能有中文
            itchat.send_file(new_path,toUserName='filehelper')
            #发送之后再改回来
            os.rename(new_path,old_path)
    
    
itchat.auto_login(hotReload=True)
itchat.dump_login_status()
itchat.run()

