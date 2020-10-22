import requests
import json
import os, sys, time
import prettytable as pt
import random

def get_data(search_text, p):
    proxieslist = {
        'https':'https://140.227.71.217:3128',
        'https':'https://140.227.11.26:3128',
        'https':'https://158.69.22.224:3128'
                  }

    search_address = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' +  search_text + '&page=' + str(p) + '&sort=sale/dc'

    r = requests.get(
            search_address,
            proxies=proxieslist
            )

    data = json.loads(r.text)
    return(data)

def show_table(data):
    output_buffer = []
    for d in data['prods']:
        buffer = []
        buffer.append(d['name'])
        buffer.append(d['price'])
        output_buffer.append(buffer)

    if len(output_buffer) == 0 :
        os.system('cls')
        print('！！！！沒有任何資料！！！！')
        return
        
    p = pt.PrettyTable(['品名','價格'], encoding='utf8')
    for d in output_buffer:
        p.add_row(d)

    p.align['品名'] = 'l'
    p.align['價格'] = 'r'
    os.system('cls')
    print(p)
    return

search_text = input('請輸入要搜尋的商品: ')
p = 1
show_table(get_data(search_text, p))

while True:
    function_number = input('輸入要查詢頁數或輸入0離開程式： ')
    try:
        function_number = int(function_number)
        if isinstance(function_number,int):
            if function_number == 0 :
                print('！！886！！\n')
                time.sleep(2)
                sys.exit()
            else:
                pass
    except Exception as e:
        print('！！你輸入的不是數字！！\n')
        time.sleep(2)
        continue
    time.sleep(random.randint(1,5))
    show_table(get_data(search_text, function_number))
