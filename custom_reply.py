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
        return YqbReply("lighten")
    elif title.find('奇梦卡') >= 0:
        return YqbReply("card")
    elif title.find('点赞PK') >= 0:
        return YqbReply("PK")
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
        self.__ActionType = acttype
        if acttype == 'lighten':
            urlslist.append(self.jsondata.readData("urls0.json"))
        elif acttype =='PK':
            urlslist.append(self.jsondata.readData("pkurls0.json"))
        else:
            pass
        self.__Urllist = urlslist
        self.__UserCount = len(urlslist)


    def send(self, toUser, fromUserName):
        num = 1
        contentlist = self.__Urllist[0]
        if self.__ActionType == 'lighten':
            Content = '所有用户的点亮城市，请点击助力：\n'
        elif self.__ActionType == 'PK':
            Content = '点赞PK，请帮忙打call： \n'
        else:
            pass
        for k in contentlist.keys():
            Content = Content + "<a href=\"" + contentlist[k] + "\">[No. " + str(num) + "]点这里助力~</a>\n"
            if num % 10 == 0:
                Content = Content + "\n"
            num = num + 1
        replyMsg = reply.TextMsg(toUser, fromUserName, Content)
        return replyMsg.send()

    def update(self, User, Url):
        linkUrl = shorter(Url)
        index=isexist(self.__Urllist,User)
        #print(index)
        if self.__ActionType == 'lighten':
            filehead="urls{}.json"
        elif self.__ActionType == 'PK':
            filehead="pkurls{}.json"
        else:
            pass

        if index >=0:
            self.__Urllist[index][User] = linkUrl
            filename=filehead.format(str(index))
            self.jsondata.writeData(filename,self.__Urllist[index])
        else:
            if len(self.__Urllist[-1]) < 101:
               self.__Urllist[-1].update({User:linkUrl})
            else:
               self.__Urllist.append({})
               self.__Urllist[-1].update({User:linkUrl})
            self.jsondata.writeData(filehead.format(str(self.__UserCount-1)),self.__Urllist[-1])
        self.mylog.printToLog("--------\n")
        self.mylog.printToLog("[info]now's yqb{}UrlsList is:{}\n".format(self.__ActionType,str(self.__Urllist)))
        self.mylog.printToLog("--------\n")


class JdReply(object):
    def __init__(self):
        pass

    def send(self):
        return "success"
    def update(self, User, linkUrl):
        pass
