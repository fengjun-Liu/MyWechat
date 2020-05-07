#!/usr/bin/python3 
# -*- coding: utf-8 -*-
import json
import wchatMessage
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from weather import GetWeather

def getCfg(name):
    filename = 'personal.json'
    with open(filename, 'r') as load_f:
        config = json.load(load_f)
    return config[name]


def mail2qq(att_con):
    """
    发送到我的qq邮箱
    格式为网络图片+文字
    """
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = getCfg('mailUser')  # 用户名
    mail_pass = getCfg('mailPasswd')  # 口令

    sender = mail_user
    receivers = getCfg('mailReceivers')  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEMultipart()
    message['From'] = sender
    # 邮件主题，正文
    message['Subject'] = Header(' 天气状况', 'utf-8')

    # 网络图片，正文发送
    content = MIMEText('<html><body>' + att_con + '</body></html>', 'html', 'utf-8')
    message.attach(content)
    try:
        smtp_Obj = smtplib.SMTP()
        smtp_Obj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtp_Obj.login(mail_user, mail_pass)
        smtp_Obj.sendmail(sender, receivers, message.as_string())
        smtp_Obj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as err:
        print(err)


if __name__ == '__main__':
    weather_content = GetWeather("海淀")
    mail2qq(weather_content)
    wchatMessage.pushmywchat('今日天气状况', weather_content)
