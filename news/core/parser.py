import bs4
import requests
import random


def get_link_osnmedia_ru() -> str:
    page = requests.get('https://www.osnmedia.ru/')
    pars = bs4.BeautifulSoup(page.content, 'lxml')
    bar = pars.find('div', class_='news-bar')
    bar_news_list = bar.find_all('div', class_='news-bar-article')
    random_new = random.choice(bar_news_list)
    link = random_new.find('a', class_='news-bar-article-title').get('href')
    return link


def get_data_new_osnmedia_ru() -> dict:
    new_link = get_link_osnmedia_ru()
    new_page = requests.get(new_link)
    pars = bs4.BeautifulSoup(new_page.content, 'lxml')
    post_content = pars.find('div', class_='postContent')
    title = post_content.find('h1', class_='page-title').text
    text = post_content.find('div', class_='maintext').text
    return {'title': title,
            'text': text}
