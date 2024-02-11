import requests
from bs4 import BeautifulSoup
import csv

class IndeedSpider:
    def __init__(self):
        self.start_url = 'https://www.indeed.com/'

    def scrape(self, url=None):
        if url:
            response = requests.get(url)
        else:
            response = requests.get(self.start_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        jobs = soup.find_all('div', class_='jobsearch-SerpJobCard')

        with open('scrabing/data/indeed_jobs.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'company', 'location', 'description'])
            writer.writeheader()

            for job in jobs:
                title = job.find('h2', class_='title').find('a').get_text()
                company = job.find('span', class_='company').get_text()
                location = job.find('div', class_='recJobLoc')['data-rc-loc']
                description = job.find('div', class_='summary').get_text()

                writer.writerow({
                    'title': title,
                    'company': company,
                    'location': location,
                    'description': description
                })

        next_page_link = soup.find('a', attrs={'aria-label': 'Next'})
        if next_page_link:
            next_page_url = 'https://www.indeed.com' + next_page_link['href']
            self.scrape(next_page_url)


spider = IndeedSpider()
spider.scrape()
