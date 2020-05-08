# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import log
import custom_reply
import keyword_reply
import config
from urlshorter import shorter


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            myconfig = config.Config()
            token = myconfig.webToken  # 与公众平台官网\基本配置中信息一致
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode %s, signature: %s".format(hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            mylog = log.Mylog()
            mylog.printToLog("########\n[info]Handle Post webdata is " + webData.decode('utf-8') + "\n########\n")
            recMsg = receive.parse_xml(webData.decode())
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    replyMsg = keyword_reply.parse_keyword(recMsg.Content)
                    return replyMsg.send(toUser, fromUser)
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                if recMsg.MsgType == 'link':
                    replyMsg = custom_reply.parse_link(recMsg.Description)
                    replyMsg.update(toUser, shorter(recMsg.Url))
                    return replyMsg.send(toUser, fromUser)
                else:
                    return reply.Msg().send()
            else:
                mylog.printToLog("暂且不处理")
                return reply.Msg().send()
        except Exception as Argument:
            return Argument
