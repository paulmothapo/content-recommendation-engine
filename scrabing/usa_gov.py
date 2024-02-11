import requests
from bs4 import BeautifulSoup
import csv

class DataGovSpider:
    def __init__(self):
        self.start_url = 'https://www.data.gov/'

    def scrape(self, url=None):
        if url:
            response = requests.get(url)
        else:
            response = requests.get(self.start_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        datasets = soup.find_all('div', class_='dataset-content')

        with open('scrabing/data/data_gov_datasets.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'description', 'resource_link'])
            writer.writeheader()

            for dataset in datasets:
                title = dataset.find('h3', class_='dataset-heading').find('a').get_text()
                description = dataset.find('div', class_='dataset-description').get_text()
                resource_link = dataset.find('div', class_='resource-url-analytics').find('a')['href']

                writer.writerow({
                    'title': title,
                    'description': description,
                    'resource_link': resource_link
                })

        next_page_link = soup.find('a', class_='next')
        if next_page_link:
            next_page_url = next_page_link['href']
            self.scrape(next_page_url)


spider = DataGovSpider()
spider.scrape()
