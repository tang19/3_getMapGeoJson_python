#coding = utf-8
import re
import requests
from bs4 import BeautifulStoneSoup as bs
import json
import os

def save_text(areaCode, level, content):
    if(level == 'province'):
        areaCodePro = areaCode[0:2]
        with open('./map/province/' + areaCodePro + '.json', 'w', encoding='utf-8') as f:
            f.write(content)
    elif(level == 'city'):
        with open('./map/city/' + areaCode + '.json', 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        with open('china.json', 'w', encoding='utf-8') as f:
            f.write(content)


def getJson(areaCode, level = ''):
    url = 'http://datavmap-public.oss-cn-hangzhou.aliyuncs.com/areas/children/' + str(areaCode) + '.json'
    print('areaCode: ', areaCode)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://datav.aliyun.com',
        'Referer': 'http://datav.aliyun.com/tools/atlas/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    mapJson = r.text
    print(mapJson)
    if('Error' in mapJson):
        return
    save_text(str(areaCode), level, mapJson)
    areas = json.loads(mapJson)['features']
    if(areas):
        for area in areas:
            item = area['properties']
            if(item['level'] == 'province' or item['level'] == 'city'):
                getJson(item['adcode'], item['level'])

if __name__ == '__main__':
    getJson('100000', '')
    #getJson('820000', 'province')