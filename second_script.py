
import requests
import time
import csv
from bs4 import BeautifulSoup
url = "https://www.rokomari.com/book/category/2407/book-fair-2020"

response = requests.get(url)

if 200 == response.status_code:
    content = response.content 
    soup_data = BeautifulSoup(content,"html.parser")
    paginate = soup_data.find("div",{"class":"pagination"})
    pages_num = paginate.find_all("a")
    last_page = int(pages_num[len(pages_num)-2].text)
    all_book_data = []
    for num in range(1,last_page+1):
        time.sleep(2)
        page_url = f"https://www.rokomari.com/book/category/2407/book-fair-2020-?page={num}"
        response_page = requests.get(page_url)
        if 200 == response_page.status_code:
            pages_content = response_page.content
            beatify_data = BeautifulSoup(pages_content,"html.parser")
            book_data = beatify_data.find_all("div",{"class":"book-list-wrapper"})
            
            for books in book_data:
                book_name = books.find("p",{"class":"book-title"}).text
                book_author = books.find("p",{"class":"book-author"}).text
                price = books.find("p",{"class":"book-price"})
                book_original_price = price.find("strike",{"class":"original-price"}).text if price.find("strike",{"class":"original-price"}) else  ''
                book_dis_price = price.find("span").text
                all_book_data.append([book_name,book_author,book_original_price,book_dis_price])
            print(f"Page {num} Write Successfull")
            with open('rokomari_books.csv', mode='w') as csv_file:
                fieldnames = ['BookName', 'BookAuthor','BookOriginalPrice','BookDiscountPrice']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()  
                writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')      
                writer.writerows(all_book_data)
                
            
            
            

 
    




    
    # pages = []
    # for single in paginate:
    #     page_num =  single.find("a").text
    #     pages.append(page_num)

    # print(pages)