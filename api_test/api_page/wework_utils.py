import requests

from api_test.api_page.base_api import BaseApi


class WeworkUtils(BaseApi):

    def get_token(self, corpsecret, corpid="wweb3d2aeb84039a81"):
        # 获取验证信息
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        }
        r = self.send_api(data)
        return r["access_token"]
