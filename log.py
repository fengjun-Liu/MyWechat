# -*- coding: utf-8 -*-
# filename: log.py

class Mylog(object):
    def printToLog(self,content):
        with open('log.txt','a+') as f1:
            f1.write(content)

log=Mylog()

