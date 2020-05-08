import requests
import log

def shorter(url):
    mylog = log.Mylog()
    key = '5eb55591b1b63c4a8d3cc637@10a7d0aa6c326884b44da4db8e64ae53'
    params = {"url":url, "key":key}
    apiurl = "http://suo.im/api.htm?format=json&expireDate=2020-05-21"
    response = requests.request("GET", apiurl,params=params)
    result=response.json()
    linkUrl = result['url']
    mylog.printToLog("********\n[info]Shorter response " + response.content.decode() + "\n********\n")
    if len(linkUrl) == 0:
        return url
    return result['url']

