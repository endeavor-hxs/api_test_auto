import requests
from common.get_mysql import *
#查找用户参数信息

def test_update_info():
    user_id = get_sql("select id from fname_user where user name = 'admin'")[0][0]
    #查询数据库的信息，并通过[0][0]定位
    print(user_id,type(user_id))    #查询数据库返回的结果并打印数据类型

    url = ''
    data={
        'admin':user_id
    }

    r_sult = requests.post(url=url,data = data)


    #数据库参数化的应用：可以应用在调用短信验证码
