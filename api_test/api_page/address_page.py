from api_test.api_page.base_api import BaseApi
import requests

from api_test.api_page.wework_utils import WeworkUtils


class AddressPage(BaseApi):
    """
    通讯录管理，包括增删改查
    """

    def __init__(self):
        _corpsecret = "TWe_VHV7KXkdNUYL3R3cFIAYaJoLeG_O1nz5D7fEZVM"
        utils = WeworkUtils( )
        self.token = utils.get_token(_corpsecret)

    def incre_depart(self):
        # 添加部门
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create?",
            "params": {"access_token": self.token},
            "json": {
                "name": "测试开发研发部",
                "parentid": 1,
                "id": 2
            }
        }
        result = self.send_api(data)
        return result

    def update_depart(self):
        # 更新部门信息
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "json": {
                "id": 1,
                "name": "测试开发部"
            }
        }
        result = self.send_api(data)
        return result

    def del_depart(self):
        # 删除部门
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        }
        result = self.send_api(data)
        return result

    def getlist_derpart(self):
        # 获取部门列表
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id=ID"
        }
        result = self.send_api(data)
        return result
