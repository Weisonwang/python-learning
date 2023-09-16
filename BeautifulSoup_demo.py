from bs4 import BeautifulSoup
import requests
content = requests.get("http://www.example.com").text
soup = BeautifulSoup(content,"html.parser")
