import requests
import config
import json

def GetWeather(city):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    # 阿凡达api
    myconfig = config.Config()
    weather_url = 'http://api.avatardata.cn/Weather/Query?cityname={City}&key={Key}'.format(City=city, Key=myconfig.avadarWeather )

    wea = requests.get(weather_url, headers=headers)
    result = json.loads(wea.content)['result']
    if result == "null":
        return "无该城市天气信息"
    else:
        wea_cont = '<p>当前时间为：' + result["realtime"]["date"] + "（农历" + result["realtime"]["moon"] + '） ' + \
                   result["realtime"]["time"] + '''</p><p>
        当前温度：''' + result["realtime"]["weather"]["temperature"] + '℃   相对湿度' + result["realtime"]["weather"][
                       "humidity"] + "%   " + result["realtime"]["wind"]["direct"] + result["realtime"]["wind"]["power"] + '''</p><p>
        今日天气：''' + result["weather"][0]["info"]["day"][1] + '''</p><p>
        今日温度：''' + result["weather"][0]["info"]["night"][2] + "℃ -" + result["weather"][0]["info"]["day"][2] + '''℃ </p><p>
        日出时间：''' + result["weather"][0]["info"]["day"][5] + '''</p><p>
        日落时间：''' + result["weather"][0]["info"]["night"][5] + '''</p>
        '''
        return wea_cont