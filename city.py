# -*- coding: utf-8 -*-
# filename: city.py



def isexist(all,one):
    '''查询当前是否已存在'''
    i=0
    for i in range(len(all)):
        if one['id'] in all[i]:
            #print(one['id'],all[i])
            return 1
        else:
            i=i+1
    return 0

alllist=[{"ovIvWvx8Vfi8NYNM6VsY3SFMnCzw":"https://d.yqb2017.com/activity/h5/lightenCity/index.html#/helpHand?yqb_disambiguity_uid=881168339112101101&cityNo=1&registerChannel=H-100328&yqb_disambiguity_channel=1",
"hw1":"wq",
"hw2":"wq",
"hw3":"wq",
"hw4":"wq",
"hw5":"wq",
"hw6":"wq",
"hw7":"wq",
"hw8":"wq",
"hw9":"wq",
"hw11":"wq"},{"hehe":"sss",},]
newone={"id":"hehe","url":"http://www.baidu.com"}

if isexist(alllist,newone)==1:
    pass
else:
    if len(alllist[-1]) < 11:
        alllist[-1].update({newone['id']:newone['url']})
    else:
        alllist.append({})
        alllist[-1].update({newone['id']:newone['url']})
#print(alllist)






for k in d.keys() :
    print(k , d[k])