import requests


class BaseApi:
    """
    api的抽象类
    """

    def send_api(self, data: dict):
        """
        发送api
        """
        return requests.request(**data).json( )
