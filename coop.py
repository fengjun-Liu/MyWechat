# -*- coding: utf-8 -*-
# filename: yqb.py

import web
import data
import log

def replyHtml(type, index):
    if type == 'yqb':
        jsondata=data.MyData()
        contentlist=jsondata.readData("urls"+str(index)+".json")
        mylog = log.Mylog()
        
        num = 1
        Content = "<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /><h1>请点击以下链接助力:</h1>\n"
        for k in contentlist.keys() :
            #print("key is"+k+"\n")
            if num%10 == 1 :
                Content = Content + "<br />\n"
            Content = Content + "<p><a href=\""+contentlist[k]+"\">[No. "+str(num)+"]点这里助力~</a></p>\n"
            num = num + 1
        Content = Content + "<p>感谢使用！</p></html>"
        mylog.printToLog("********\n[info]Reply html is "+Content+"\n********\n")
        return(Content)
    else:
        return("<html><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" /><h1>互助页面，暂只支持壹钱包点亮城市</h1></html>")
class Coop(object):
   def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return replyHtml("yqb",0)
            else:
                index = int(web.input().index)
                type = str(web.input().type)
                return replyHtml(type,index)
        except Exception as Argument:
            return Argument

class Yqb(Coop):
   def GET(self, index):
        try:
            data = web.input()
            if len(data) == 0:
                return replyHtml("yqb",0)
            else:
                index = int(web.input().index)
                return replyHtml(index)
        except Exception as Argument:
            return Argument
    
