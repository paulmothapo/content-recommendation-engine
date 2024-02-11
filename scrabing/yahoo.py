import requests
from bs4 import BeautifulSoup
import csv

class YahooFinanceSpider:
    def __init__(self):
        self.start_url = 'https://finance.yahoo.com/'

    def scrape(self, url=None):
        if url:
            response = requests.get(url)
        else:
            response = requests.get(self.start_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all('li', class_='js-stream-content')

        with open('yahoo_finance_articles.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'summary', 'link'])

            for article in articles:
                title = article.find('h3').get_text()
                summary = article.find('p').get_text()
                link = article.find('a')['href']

                writer.writerow({
                    'title': title,
                    'summary': summary,
                    'link': link
                })

        next_page_link = soup.find('a', class_='next')
        if next_page_link:
            next_page_url = 'https://finance.yahoo.com' + next_page_link.get('href')
            self.scrape(next_page_url)


spider = YahooFinanceSpider()
spider.scrape()
