import requests
import data

def shorter(url):
    key = '5eb569e044bb356cc48c8b6d@4acf407d134129a14bee391d39051796'
    params = {"url":url, "key":key}
    apiurl = "http://suo.im/api.htm?format=json&expireDate=2020-05-21"
    response = requests.request("GET", apiurl,params=params)
    result=response.json()
    return result['url']

jsondata = data.MyData()
contentlist = jsondata.readData("urls0.json")
Content = ''
num = 1
for k in contentlist.keys():
    if num % 10 == 1:
        Content = Content + "<br />\n"
    Content = Content + "<a href=\"" + shorter(contentlist[k]) + "\">[No. " + str(num) + "]点这里助力~</a>\n"
    num = num + 1
Content = Content + "<p>感谢使用！</p></html>"
print(Content)