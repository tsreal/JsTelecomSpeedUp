import time

import requests
import json

if __name__ == '__main__':
    #url 直接开始体验宽带提速
    url = 'http://ts.js.vnet.cn/speed/beginExperiences'
    #url1 走流程体验
    url1 = 'http://ts.js.vnet.cn/speed/experiencesSpeedModel'
    data = {
        'action': 'ExperiencesSpeedModel',
        'isPostBk': '1',
        'UserAccount': '02512237467',
        'AreaCode': '025'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url=url, data=data, headers=headers)
    print(response.text)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))