from danmu import DanMuClient
import pymysql

dmc = DanMuClient('https://www.douyu.com/688')

@dmc.danmu
def danmu_fn(msg):
    client = msg['NickName']
    message = msg['Content']
    connection = pymysql.connect(
            host='XXXX',  # 连接的是本地数据库
            user='XXXX',        # mysql用户名
            passwd='XXXX',  # 密码
            db='XXXX',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式,最好选这个，因为弹幕会出现表情
            cursorclass=pymysql.cursors.DictCursor)
      
    with connection.cursor() as cursor:
        # 创建更新值的sql语句
        sql = "INSERT INTO 张大仙弹幕(client,message) VALUES (%s,%s)"
        cursor.execute(sql,(client,message))

        # 提交本次插入的记录
        connection.commit()
        

dmc.start(blockThread = True)
