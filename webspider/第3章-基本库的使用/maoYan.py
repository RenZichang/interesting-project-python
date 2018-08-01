import requests
import re
import time

def getPage(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    request = requests.get(url, headers = headers)
    return request.text

def select(text):
    pattern = re.compile('''<dd>.*?href="(.*?)".*?title="(.*?)".*?integer">(.*?)<.*?fraction">(.*?)<.*?</div>''', re.S)
    items = re.findall(pattern, text)
    return items

def putIntoFile(items):
    with open('Films.txt', 'a', encoding = 'utf-8') as f:
        for item in items:
            f.write('url:https://maoyan.com' + item[0] + '\n')
            f.write('name:' + item[1] + '\nscore:' + item[2] + item[3] + '\n\n')

def main():
    for offset in range(0, 808560, 30):
        t = getPage('https://maoyan.com/films?sortId=3&offset=' + str(offset))
        l = select(t)
        putIntoFile(l)
        print('%.2f%%' % (offset / 808530))

main()
