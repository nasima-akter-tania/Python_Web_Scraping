from bs4 import BeautifulSoup 
from contextlib import closing
import requests
import time
import csv

def get_content(url):
    """ this function use for get url data and return the url data"""
    try:
       
        response = requests.get(url)
        time.sleep(15)
        if 200 == response.status_code:
            return response.content
    except RequestException as e:
        print("There have some Request error")

content=get_content("https://qianxi.baidu.com/")

soup_data = BeautifulSoup(content,"html.parser")
get_div_data = soup_data.find("div",{"class":"app-head"})
all_tr_data = get_div_data.find_all("tr",{"class":"undefined"})
print(get_div_data)




