import requests
url="https://www.toutiao.com/a6725004119154622979/"
r=requests.get(url)
print(r.text)