import time, datetime
import itchat
from itchat.content import *
import easygui as g
@itchat.msg_register([TEXT, PICTURE, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
    if msg['Type'] == 'Text':
        reply_content = msg['Text']
    elif msg['Type'] == 'Picture':
        reply_content = '图片: ' + msg['FileName']
    elif msg['Type'] == 'Note':
        reply_content = '通知'
    elif msg['Type'] == 'Sharing':
        reply_content = '分享'
    elif msg['Type'] == 'Recording':
        reply_content = '语音'
    elif msg['Type'] == 'Attachment':
        reply_content = '文件: ' + msg['FileName']
    elif msg['Type'] == 'Video':
        reply_content = '视频: ' + msg['FileName']
    else:
        reply_content = '消息'

    friend = itchat.search_friends(userName=msg['FromUserName'])
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    if not msg['FromUserName'] == myUserName:
        itchat.send(r'Friend:%s -- %s    '
                '时间:%s    '
                '信息:%s' % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),
                toUserName='filehelper')
        itchat.send(r"[自动回复]我已经收到你的消息，"+second+"，我看到信息的时候会马上回复你的。",toUserName=msg['FromUserName'])
#保持登录状态    
itchat.auto_login(hotReload=True)
itchat.dump_login_status()

#简陋的图形界面- -
first = g.multenterbox(msg='''该程序主要功能是当你不在手机旁时自动回复微信

                       请输入起始时间''',title='python微信小助手',fields=['起始时间(如23:45)'],values=['23:45'])
global second
second = g.choicebox(msg='请选择你的状态',title='python微信小助手',choices=['我在睡觉','我在上课','我在上班','我还在外面','我在忙'])
sh = first[0].split(':')[0]
sm = first[0].split(':')[1]
#获取现在时间
now = datetime.datetime.now()
m = now.month
d = now.day
#指定的开始时间
startTime = datetime.datetime(2017,int(m),int(d),int(sh),int(sm),0)
#当没有达到指定时间时，程序休眠
while datetime.datetime.now() < startTime:  
    time.sleep(1)
itchat.run()



