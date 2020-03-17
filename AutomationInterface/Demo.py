import requests

url='http://www.httpbin.org/post'
data={''}
header={'Connection': 'keep-alive',
        'Content-Length': '0',
        'accept': 'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Origin': 'http://www.httpbin.org',
        'Referer': 'http://www.httpbin.org/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9"'}
resp =requests.post(url=url,data=data,headers=header)
print(resp.text,resp.status_code)

print(1)