import requests
import bs4
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Удалённая работа', 'Программирование *']
URL = 'https://habr.com/ru/all/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(URL, headers=headers).text
soup = bs4.BeautifulSoup(response, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            name = article.find(class_='tm-article-snippet__title-link').text
            href = 'https://habr.com' + article.find(class_='tm-article-snippet__title-link').attrs['href']
            resp = requests.get(href).text
            soup_2 = bs4.BeautifulSoup(resp, features='html.parser')
            look = soup_2.find(class_='tm-icon-counter__value').text
            print(f"{date} - {name} - {href}")
            print(f'Число просмотров - {look}')