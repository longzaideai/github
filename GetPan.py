import time
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url='https://pan.saipancloud.com/sitemap.xml'
res=requests.get(url)
html=res.text

with open('sitemap.xml', 'w') as f:
    f.write(html)

tree = ET.parse('sitemap.xml')

root = tree.getroot()
for stu in root:
    res = requests.get(stu[0].text)
    res.encoding = 'utf-8'  # 
    soup = BeautifulSoup(res.text, 'lxml')
    if(soup.title):
        Title = str(soup.title.text)
    else:
        print('获取失败，可能遇到反爬，休息十秒。')
        time.sleep(12) #休息十秒防止速率过快反爬
    print(Title)
    print (stu[0].text)
    with open('Result.txt', 'a+') as j:
        j.write('标题：' + Title + '网址：' + str(stu[0].text) + "\n")
    
    time.sleep(1) #休息一秒防止速率过快反爬