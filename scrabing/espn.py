import requests
from bs4 import BeautifulSoup
import csv

class EspnSportsSpider:
    def __init__(self):
        self.start_url = 'https://www.espn.com/'

    def scrape(self, url=None):
        if url:
            response = requests.get(url)
        else:
            response = requests.get(self.start_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all('article', class_='headlineStack__list-item')

        with open('scrabing/data/espn_sports_articles.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'summary', 'link'])

            for article in articles:
                title = article.find('a', class_='headline').get_text()
                summary = article.find('p', class_='headlineStack__summary').get_text()
                link = article.find('a', class_='headline')['href']

                writer.writerow({
                    'title': title,
                    'summary': summary,
                    'link': link
                })

        next_page_link = soup.find('a', class_='Pagination__next')
        if next_page_link:
            next_page_url = 'https://www.espn.com' + next_page_link['href']
            self.scrape(next_page_url)

spider = EspnSportsSpider()
spider.scrape()
