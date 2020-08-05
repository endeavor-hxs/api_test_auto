import pymysql
from config.conf import sql_conf
def get_sql(sql):
    '''
    :param:进行查询的SQL语句
    return：数据库查询的结果
    '''
    host,user,password,database,port,charset = sql_conf()
    db = pymysql.connect(host =host, user=user, database=database, port=port, charset=charset)

    #建立一个游标
    cursor = db.cursor()
    #运行sql语句
    cursor.execute(sql)
    #把SQL运行的数据保存到data中
    data = cursor.fetchall()    #获取查询出所有的值
    #关闭游标
    cursor.close()
    #关闭数据库
    db.close()
    return data
print(get_sql("select id from fname user where user name = 'admin'"))   #运行SQL语句
