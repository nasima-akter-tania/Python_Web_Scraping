from bs4 import BeautifulSoup 
import requests
import time
import csv

def get_content(url):
    """ this function use for get url data and return the url data"""
    try:
       
        response = requests.get(url)
        if 200 == response.status_code:
            return response.content
    except RequestException as e:
        print("There have some Request error")

content=get_content("https://www.worldometers.info/coronavirus/#countries")

soup_data = BeautifulSoup(content,"html.parser")
get_div_data = soup_data.find("table",{"id":"main_table_countries_today"})
all_tr_data = get_div_data.find_all("tr",{"style":""})

all_data = {}
for single_tr in all_tr_data:
    country = single_tr.find("a",{"class":"mt_a"}).text if single_tr.find("a",{"class":"mt_a"}) else 'no_country'
    all_td = single_tr.find_all("td")
    all_data[country] = all_td

csv_data=[] 
for key,get_td in all_data.items():
    valueslist = []
    if(key != 'no_country'):
        for values in get_td:
            valueslist.append(values.text)
        csv_data.append(valueslist)
            
           
 
with open('corona_update.csv', mode='w') as csv_file:
    fieldnames = ['Country', 'TotalCase','NewCases','TotalDeath','NewDeath','TotalRecover','ActiveCases','SeriousCritical','TopCases','Deaths','TotalTest','Tests']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()  
    writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    writer.writerows(csv_data)   


    
 





