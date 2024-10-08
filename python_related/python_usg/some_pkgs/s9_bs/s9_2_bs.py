import requests
from bs4 import BeautifulSoup

# 定义请求头，有些网站防止爬虫，所以需要伪装浏览器进行请求
# User-Agent可以用浏览器打开个页面，然后`检查-网络-刷新一下网页-随便点击一个查看里面的请求标头的User-Agent`
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        title_string = title.string
        if "/" not in title_string:
            print(title_string)

pass