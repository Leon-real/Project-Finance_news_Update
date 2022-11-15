import requests
from bs4 import BeautifulSoup

def update_news():
    url = r'https://search.naver.com/search.naver?where=news&query=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0'
    info_list=[]
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')

    else : 
        print(response.status_code)

    tags = soup.find_all('a', class_='news_tit')
    for tag in tags:
        # print()
        # print(tag.text)
        # print(tag['href'])
        info_list.append([tag.text,tag['href']])


    return info_list
