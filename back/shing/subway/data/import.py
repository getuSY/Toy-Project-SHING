import requests
import json
import time
import schedule

def renewal():
    start = 1
    end = 1000
    path = f'http://openapi.seoul.go.kr:8088/6a68516552746d6437395556596f4e/json/SeoulMetroFaciInfo/{start}/{end}/'
    response = requests.get(path)
    res = response.json()
    length = res['SeoulMetroFaciInfo']['list_total_count']
    data = res['SeoulMetroFaciInfo']['row']

    while end < length:
        start += 1000
        end += 1000
        if end >= length:
            end = length
        path = f'http://openapi.seoul.go.kr:8088/6a68516552746d6437395556596f4e/json/SeoulMetroFaciInfo/{start}/{end}/'
        response = requests.get(path)
        res = response.json()
        data = data + res['SeoulMetroFaciInfo']['row']

    with open('facility.json','w',encoding='utf-8') as make_file:
                json.dump(data,make_file,ensure_ascii = False)

schedule.every(10).minutes.do(renewal)
while True:
    schedule.run_pending()
    time.sleep(1)