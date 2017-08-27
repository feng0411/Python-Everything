from danmu import DanMuClient
import pymysql

dmc = DanMuClient('https://www.douyu.com/688')

@dmc.danmu
def danmu_fn(msg):
    client = msg['NickName']
    message = msg['Content']
    connection = pymysql.connect(
            host='192.168.31.40',  # 连接的是本地数据库
            user='feng',        # mysql用户名
            passwd='19950411',  # 密码
            db='feng',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)
      
    with connection.cursor() as cursor:
        # 创建更新值的sql语句
        sql = "INSERT INTO 张大仙弹幕(client,message) VALUES (%s,%s)"
        cursor.execute(sql,(client,message))

        # 提交本次插入的记录
        connection.commit()
        

dmc.start(blockThread = True)
