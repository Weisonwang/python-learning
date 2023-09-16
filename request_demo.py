import requests
response = requests.get("http://1.116.127.12:5000/#")
if response.ok:
    print(response.text)
else:
    print("请求失败")