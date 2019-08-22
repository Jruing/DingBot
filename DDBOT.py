# encoding:utf-8
import requests


class DDbot():
    def __init__(self, webhook: str):
        self.webhook = webhook
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Content-Type": "application/json"
        }

    # Send text message
    def Send_Text_Msg(self, Msg: str, AtMobiles: list = None, AtAll: bool = False) -> dict:
        """
        :param Msg: 发送的文本消息
        :param AtMobiles: @需要注意此消息的用户手机号 单个用户格式'13888888888'，多个用户格式['13888888888','13999999999']
        :param AtAll: @全体成员
        :return:
        """
        try:
            message = {
                "msgtype": "text",
                "text": {
                    "content": Msg
                },
                "at": {
                    "atMobiles": [[Mobiles for Mobiles in AtMobiles] if isinstance(AtMobiles, list) else AtMobiles][0],
                    "isAtAll": AtAll
                }
            }
            response = requests.post(url=self.webhook, json=message, headers=self.header)
            return {"Status": response.status_code, "Msg": message}
        except Exception as error:
            raise Exception(error)

    # LinkMessage
    def Send_Link_Msg(self, Title: str, Text: str, MessageUrl: str, PicUrl: str = None) -> dict:
        """
        :param Title: 标题
        :param Text: 内容
        :param MessageUrl: 文章url
        :param PicUrl: 图片url 可为空
        :return:
        """
        try:
            message = {
                "msgtype": "link",
                "link": {
                    "text": Text,
                    "title": Title,
                    "picUrl": PicUrl,
                    "messageUrl": MessageUrl
                }
            }
            response = requests.post(url=self.webhook, json=message, headers=self.header)
            return {"Status": response.status_code, "Msg": message}
        except Exception as error:
            raise Exception(error)

    # MarkDown
    def Send_MD_Msg(self, Title: str, Text: str, AtMobiles: list = None, AtAll: bool = False) -> dict:
        """
        :param Title: 标题
        :param Text: 内容
        :param AtMobiles:  @需要注意此消息的用户手机号 单个用户格式'13888888888'，多个用户格式['13888888888','13999999999']
        :param AtAll: @全体成员
        :return:
        """
        try:
            message = {
                "msgtype": "markdown",
                "markdown": {
                    "title": Title,
                    "text": Text
                },
                "at": {
                    "atMobiles": [[Mobiles for Mobiles in AtMobiles] if isinstance(AtMobiles, list) else AtMobiles][0],
                    "isAtAll": AtAll
                }
            }
            response = requests.post(url=self.webhook, json=message, headers=self.header)
            return {"Status": response.status_code, "Msg": message}
        except Exception as error:
            raise Exception(error)

    # FeedCard类型
    def Send_FeedCard(self, Title: str, MessageUrl: str, PicUrl: str)->dict:
        """
        :param Title: 标题
        :param MessageUrl: 消息url
        :param PicUrl: 图片url
        :return:
        """
        if isinstance(Title, str) and isinstance(PicUrl, str) and isinstance(MessageUrl, str):
            message = {
                "feedCard": {
                    "links": [
                        {
                            "title": Title,
                            "messageURL": MessageUrl,
                            "picURL": PicUrl
                        }
                    ]
                },
                "msgtype": "feedCard"
            }
        elif isinstance(Title, list) and isinstance(PicUrl, list) and isinstance(MessageUrl, list):
            message = {
                "feedCard": {
                    "links": [{"title": t, "messageURL": m, "picURL": p} for t, m, p in zip(Title, MessageUrl, PicUrl)]
                },
                "msgtype": "feedCard"
            }
        response = requests.post(url=self.webhook, json=message, headers=self.header)
        print(response.text)


if __name__ == '__main__':
    dd = DDbot(
        webhook="https://oapi.dingtalk.com/robot/send?access_token=411155d7f69a0a5250c8c1b34a22130e0b836ab5de4769e367ff142d153b387e")
