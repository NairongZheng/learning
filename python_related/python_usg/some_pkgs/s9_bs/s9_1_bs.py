from bs4 import BeautifulSoup
import requests

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")

# 提取价格
all_prices = soup.findAll("p", attrs={"class": "price_color"}) # 所有价格都是p标签且有price_color属性，所以可以用可选参数attrs筛选出来
for price in all_prices:
    print(price.string[2:])

# 提取书名
all_titles = soup.findAll("h3") # 所有书名都是h3标签
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        print(link.string)
pass