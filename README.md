# DingBot
DingDing robot interface
#Python第三方包之DingDingBot
这个是作者自己封装的一个钉钉机器人的包，目前只支持发文本格式、链接格式、markdown格式的消息,我们可以在很多场景用到这个，比如告警通知等
## 安装
> pip install DingDingBot

## 使用方法
```
from DingDingBot.DDBOT import DingDing
# 初始话DingDingBOt  webhook是钉钉机器人所必须的
dd = DingDing(webhook='https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxx')
# 发送文本消息
print(dd.Send_Text_Msg(Content='test:测试数据'))
# 发送链接消息
print(dd.Send_Link_Msg(Content='test',Title='测试数据',MsgUrl='https://www.baidu.com',PicUrl='https://cn.bing.com/images/search?q=outgoing%e6%9c%ba%e5%99%a8%e4%ba%ba&id=FEE700371845D9386738AAAA51DCC43DC54911AA&FORM=IQFRBA'))
# 发送Markdown格式的消息
print(dd.Send_MardDown_Msg(Content="# 测试数据\n" + "> testone", Title='测试数据'))
```
