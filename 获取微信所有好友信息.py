import itchat
from pyecharts import Map #Bar柱状图，Pie饼图，Map地图
import pymysql
#保持登陆
itchat.auto_login(hotReload=True)
itchat.dump_login_status()
#获取好友信息
friends = itchat.get_friends(update=True)[:]
#总好友数
total = len(friends)-1
#各个参数
result=[('RemarkName','备注'),('NickName','微信昵称'),
        ('Sex','性别'),('City','城市'),('Province','省份'),
        ('UserName','用户名'),('Signature','个性签名')]
every = []
#male = female = other = 0
for user in friends:
    everys = {}
    everys['remarkname'] = user.get('RemarkName')
    everys['city'] = user.get('City')
    everys['nickName'] = user.get('NickName')
    everys['sex'] = user.get('Sex')
    everys['province'] = user.get('Province')
    everys['userName'] = user.get('UserName')
    everys['signature'] = user.get('Signature')
    every.append(everys)
for we in every:
    remarkname = we['remarkname']
    city = we['city']
    nickName = we['nickName']
    sex = we['sex']
    province = we['province']
    userName = we['userName']
    signature = we['signature']
    connection = pymysql.connect(
            host='192.168.31.40',  # 连接的是本地数据库
            user='feng',        # mysql用户名
            passwd='19950411',  # 密码
            db='feng',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
      
    with connection.cursor() as cursor:
        # 创建更新值的sql语句
        sql = "INSERT INTO wechat(remarkname,nickName,userName,sex,province,city,signature) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,(remarkname,nickName,userName,sex,province,city,signature))

        # 提交本次插入的记录
        connection.commit()
        
    connection.close()
print ('完成')


