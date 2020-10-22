import requests
import codecs
from bs4 import BeautifulSoup
import prettytable as pt

proxieslist = {
    'https':'https://140.227.71.217:3128',
    'https':'https://140.227.11.26:3128',
    'https':'https://158.69.22.224:3128'
}

r = requests.get(
	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Wed%20Oct%2014%202020%2014:37:51%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)",
# 	headers={
# 	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
# 	}
    proxies=proxieslist
)

b = BeautifulSoup(r.text,'html.parser')
bu = b.find_all('tr')

output_buffer = []
for i in range(0,len(bu)):
    buffer = []
    buffer.append(bu[i].find('th',{'scope':'row'}).get_text())
    buffer.append(bu[i].find('span',{'class':'tem-C'}).get_text())
    output_buffer.append(buffer)
    
MaxT_city = ''
MaxT = ''
for i in range(0,len(output_buffer)):
    if i == 0:
        MaxT_city = output_buffer[0][0]
        MaxT = output_buffer[0][1]
    else:
        if output_buffer[i][1] > MaxT:
            MaxT = output_buffer[i][1]
            MaxT_city = output_buffer[i][0]

for i in range(0,len(output_buffer)):
    if (output_buffer[i][0] == MaxT_city) and (output_buffer[i][1] == MaxT):
        output_buffer[i][0] = "\033[1;31m" + output_buffer[i][0] + "\033[0m"
        output_buffer[i][1] = "\033[1;31m" + output_buffer[i][1] + "\033[0m"

p = pt.PrettyTable(['城市','溫度'], encoding='utf8')
for d in output_buffer:
    p.add_row(d)

p.align['城市'] = 'l'
p.align['溫度'] = 'r'
print(p)
