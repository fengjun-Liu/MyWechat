# -*- coding: utf-8 -*-
# filename: keyword_reply.py

import reply
import data
import log
from weather import GetWeather


def parse_keyword(content):
    if len(content) == 0:
        return None
    if content.find('天气') >= 0:
        return WeatherReply(content)
    elif content.find('每日一图') >= 0:
        return PicReply(content)
    else:
        return KeyWordReply(content)


class KeyWordReply(object):
    my_log = log.Mylog()
    json_data = data.MyData()

    def __init__(self, content):
        pass

    def send(self, toUser, fromUserName):
        content = '''请选择以下关键字进行回复：
【天气预报】：请发送“城市+天气”，如：“北京+天气”
【国家地理每日一图】：请发送“每日一图”
暂不支持其他关键字，感谢使用！
        '''
        reply_msg = reply.TextMsg(toUser, fromUserName, content)
        return reply_msg.send()


class WeatherReply(KeyWordReply):
    def __init__(self, content):
        self.__city = content.split('+')[0]

    def send(self, toUser, fromUserName):
        weather_content=GetWeather(self.__city).replace('<p>','').replace('</p>','')
        replyMsg = reply.TextMsg(toUser, fromUserName, weather_content)
        return replyMsg.send()


class PicReply(KeyWordReply):
    def __init__(self, content):
        pass

    def send(self, toUser, fromUserName):
        replyMsg = reply.TextMsg(toUser, fromUserName, " 每日一图，wait for develop")
        return replyMsg.send()
