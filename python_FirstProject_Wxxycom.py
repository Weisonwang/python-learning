from bs4 import BeautifulSoup
import requests
url = 'https://ym28537981.jzfkw.net/'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}
content = requests.get(url=url,headers=headers,)
content.encoding='utf-8'
print(content.status_code)
html = content.text
soup = BeautifulSoup(html,"html.parser")
with open("./html.text","w",encoding="utf-8")as f:
    f.write(html)
