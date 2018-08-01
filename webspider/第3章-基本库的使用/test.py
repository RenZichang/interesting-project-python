import requests

data = {'name' : 'Richard', 'age' : '22'}
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
r = requests.post("https://httpbin.org/post", headers = headers, data = data)
print(r.text)