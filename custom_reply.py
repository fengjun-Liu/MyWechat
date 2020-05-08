# -*- coding: utf-8 -*-
# filename: custom_reply.py

import reply
import data
import log
from urlshorter import shorter


def isexist(list,one):
    '''查询当前是否已存在'''
    i=0
    for i in range(len(list)):
        if one in list[i]:
           # print(one,list[i])
            return i
        else:
            i=i+1
    return -1

def parse_link(title):
    if len(title) == 0:
        return CustReply()
    if title.find('点亮') >= 0:
        return YqbReply("点亮城市")
    elif title.find('奇梦卡') >= 0:
        return YqbReply("送卡")
    elif title.find('京东') >= 0:
        return JdReply()
    else:
        return CustReply()


class CustReply(object):
    mylog = log.Mylog()
    jsondata=data.MyData()
    def __init__(self):
        pass

    def send(self, toUser, fromUserName):
        content = "您发送的链接暂时无法互助"
        replyMsg = reply.TextMsg(toUser, fromUserName, content)
        return replyMsg.send()
    def update(self, User, linkUrl):
        pass


class YqbReply(CustReply):
    def __init__(self, acttype):
        urlslist=[]
        urlslist.append(self.jsondata.readData("urls0.json"))
        self.__Urllist = urlslist
        self.__UserCount =len(urlslist)
        self.__ActionType = acttype

    def send(self, toUser, fromUserName):
        num = 1
        jsondata = data.MyData()
        contentlist = jsondata.readData("urls0.json")
        Content = ''
        for k in contentlist.keys():
            if num % 10 == 1:
                Content = Content + "\n"
            Content = Content + "<a href=\"" + shorter(contentlist[k]) + "\">[No. " + str(num) + "]点这里助力~</a>\n"
            num = num + 1
        replyMsg = reply.TextMsg(toUser, fromUserName, Content)
        #index=isexist(self.__Urllist, toUser )
        #print(index)
        #if index >=0:
        #    replyMsg = reply.NewsMsg(toUser, fromUserName, 'yqb', index, '点亮城市，请助力')
        return replyMsg.send()

    def update(self, User, linkUrl):
        index=isexist(self.__Urllist,User)
        print(index)
        if index >=0:
            self.__Urllist[index][User] = linkUrl
            filename="urls{}.json".format(str(index-1))
            self.jsondata.writeData(filename,self.__Urllist[index])
        else:
            if len(self.__Urllist[-1]) < 101:
               self.__Urllist[-1].update({User:linkUrl})
            else:
               self.__Urllist.append({})
               self.__Urllist[-1].update({User:linkUrl})
            self.jsondata.writeData("urls{}.json".format(str(self.__UserCount-1)),self.__Urllist[-1])
        self.mylog.printToLog("--------\n")
        self.mylog.printToLog("[info]now's yqbUrlsList is:{}\n".format(str(self.__Urllist)))
        self.mylog.printToLog("--------\n")


class JdReply(object):
    def __init__(self):
        pass

    def send(self):
        return "success"
    def update(self, User, linkUrl):
        pass
