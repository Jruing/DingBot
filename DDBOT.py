#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    @@@@@@@@     @@@@@@@@@     @@@@@@@@@    @@@@@@@@@     @@@@@@@@@@@@
    @@      @@   @@      @@    @@     @@    @@      @@         @@
    @@       @@  @@       @@   @@    @@    @@        @@        @@
    @@       @@  @@       @@   @@   @@     @@        @@        @@
    @@       @@  @@       @@   @@  @@      @@        @@        @@
    @@      @@   @@      @@    @@ @@       @@        @@        @@
    @@     @@    @@     @@     @@  @@      @@        @@        @@
    @@    @@     @@    @@      @@   @@     @@        @@        @@
    @@   @@      @@   @@       @@  @@       @@      @@         @@
    @@ @@        @@ @@         @@           @@@@@@@@@          @@

'''

import requests, json


class DingDing():
    """
    Refer to official documentation: https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
    """

    def __init__(self, webhook):
        self.webhook = webhook
        self.session = requests.session()
        self.session.headers = {"Content-Type": "application/json;charset=utf-8"}

    def Send_Text_Msg(self, Content: str, atMobiles: list = [], isAtAll: bool = False) -> dict:
        """
        :param content: Text message to send
        :param atMobiles: contact list:Must be a mobile phone number
        :param isAtAll: @All members
        :return:
        """
        try:
            data = {
                "msgtype": "text",
                "text": {
                    "content": Content
                },
                "at": {
                    "atMobiles": atMobiles,
                    "isAtAll": isAtAll
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result

    def Send_Link_Msg(self, Content: str, Title: str, MsgUrl: str, PicUrl: str = ''):
        """
        :param Content: Summary of this link
        :param title: The title of this link
        :param MsgUrl: The target url to be redirected
        :param PicUrl: Picture of this link
        :return:
        """
        try:
            data = {
                "msgtype": "link",
                "link": {
                    "text": Content,
                    "title": Title,
                    "picUrl": PicUrl,
                    "messageUrl": MsgUrl
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result

    def Send_MardDown_Msg(self, Content: str, Title: str, atMobiles: list = [], isAtAll: bool = False):
        """
        :param Content: markdown formatted text
        '''
        标题
            # 一级标题
            ## 二级标题
            ### 三级标题
            #### 四级标题
            ##### 五级标题
            ###### 六级标题

            引用
            > A man who stands for nothing will fall for anything.

            文字加粗、斜体
            **bold**
            *italic*

            链接
            [this is a link](http://name.com)

            图片
            ![](http://name.com/pic.jpg)

            无序列表
            - item1
            - item2

            有序列表
            1. item1
            2. item2
        '''
        :param Title: The title of this link
        :param atMobiles: contact list:Must be a mobile phone number
        :param isAtAll: @All members
        :return:
        """
        try:
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": Title,
                    "text": Content
                },
                "at": {
                    "atMobiles": atMobiles,
                    "isAtAll": isAtAll
                }
            }
            response = self.session.post(self.webhook, data=json.dumps(data))
            if response.status_code == '200':
                result = {"status": True, "message": "Message has been sent"}
                return result
            else:
                return response.text
        except Exception as error:
            result = {"status": False, "message": f"Failed to send message,Error stack:{error}"}
            return result

from DingDingBot.DDBOT import DingDing
# dd = DingDing(webhook='https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx')
# print(dd.Send_Text_Msg(Content='test:测试数据'))
# print(dd.Send_Link_Msg(Content='test',Title='测试数据',MsgUrl='https://www.baidu.com',PicUrl='https://cn.bing.com/images/search?q=outgoing%e6%9c%ba%e5%99%a8%e4%ba%ba&id=FEE700371845D9386738AAAA51DCC43DC54911AA&FORM=IQFRBA'))
# print(dd.Send_MardDown_Msg(Content="# 测试数据\n" + "> testone", Title='测试数据'))
