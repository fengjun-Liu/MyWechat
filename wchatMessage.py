import requests
import config


def pushmywchat(text, desp):
    """
    发送到我的微信
    使用了第三方推送 https://sc.ftqq.com/3.version ，需提前申请自己的key
    """
    dd = {'text': text, "desp": desp}
    myconfig = config.Config()
    wechat_url = "https://sc.ftqq.com/{WechatSecid}.send".format(WechatSecid=myconfig.wechatNotify)
    payload = {}
    headers = {}
    try:
        response = requests.request("GET", wechat_url, params=dd, headers=headers, data=payload)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return (response.text)
    except:
        return "产生异常，发送微信消息失败"
