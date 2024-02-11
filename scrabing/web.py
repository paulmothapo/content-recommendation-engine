import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article elements on the page
        articles = soup.find_all('article')
        
        # Extract article titles and content
        article_data = []
        for article in articles:
            title = article.find('h2').text.strip()
            content = article.find('div', class_='content').text.strip()
            article_data.append({'title': title, 'content': content})
        
        return article_data
    else:
        print("Failed to retrieve page:", response.status_code)
        return None

# Example URL of the website containing articles
url = 'https://example.com/articles'
articles = scrape_articles(url)

if articles:
    for article in articles:
        print("Title:", article['title'])
        print("Content:", article['content'])
        print()
