

import requests
from config.conf import *   #*号表示模糊导入
from common.get_excel import *


def test_lo():
    url = server_ip()+'/register'   #调用函数，这里要注意需要添加括号

    username,password = get_excel_row(1)        #读取文件的信息，从第二行开始

    data = {
        'username':username,
        'password':password
        }
    r_regit = requests.post(url = url,data = data)
    print(r_regit.text)
    print(r_regit.status_code)

    url = server_ip() +'/login'
    json = {
        'username':123,
        'password':123456
        }
    r_login = requests.post(url = url,json = json)
    print(r_login.json())
    print(r_login.status_code)