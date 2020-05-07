# -*- coding : utf-8 -*-
# filename: data.py
import json
 
class MyData(object):
    def writeData(self,file,data):
         with open(file, 'w') as f:
            json.dump(data,f)
    def readData(self,file):
        with open(file, 'r') as f:
            data = json.load(f)
            return data

jsondata=MyData()
