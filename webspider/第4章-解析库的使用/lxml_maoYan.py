import requests
from lxml import etree
import time
from random import randint

def getPage(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    request = requests.get(url, headers = headers)
    return request.text

def select(text):
    html = etree.HTML(text)
    items = html.xpath("//dd/div[1]/a/@href")
    items += html.xpath("//dd/div/@title")
    items1 = html.xpath("//dd/div[contains(@class, 'channel-detail-orange')]/i[1]/text()")
    items2 = html.xpath("//dd/div[contains(@class, 'channel-detail-orange')]/i[2]/text()")
    for j in range(0, len(items1)):
        items.append(items1[j] + items2[j])
    k = int((len(items) + 1) / 3)
    L = []
    for i in range(0, k):
        for j in [0, 1, 2]:
            L.append(items[int(j * k) + i])
    return L

def putIntoFile(items):
    with open('lxml_Films.txt', 'a', encoding = 'utf-8') as f:
        i = 0
        while i < len(items):
            f.write('url:https://maoyan.com' + items[i] + '\n')
            f.write('name:' + items[i + 1] + '\nscore:' + items[i + 2] + '\n\n')
            i += 3

def main():
    for offset in range(0, 808560, 30):
        t = getPage('https://maoyan.com/films?sortId=3&offset=' + str(offset))
        l = select(t)
        putIntoFile(l)
        print('%.4f%%' % (offset / 808530))
        time.sleep(randint(0, 5))

main()
