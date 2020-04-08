import requests
from bs4 import BeautifulSoup

url = "https://abbreviations.yourdictionary.com/articles/country-abbreviations.html"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')
all_a = soup.find_all("a")
all_href = []
for data in all_a:
    all_href.append(data.get("href"))
print(all_href)
