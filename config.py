import json


def readCfg(name):
    with open('personal.json', 'r') as f:
        data = json.load(f)
        return data[name]

class Config:
    def __init__(self):
        self.mailUsername=readCfg('mailUser')
        self.mailPasswd=readCfg('mailPasswd')
        self.wechatAppid = readCfg('wechatFengAppid')
        self.wechatSecid = readCfg('wechatFengSecid')
        self.wechatNotify = readCfg('wechatNotify')
        self.avadarWeather = readCfg('avadarWeather')
        self.mailReceivers = readCfg('mailReceivers')
        self.webToken = readCfg('webToken')

