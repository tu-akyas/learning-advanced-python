import requests
from pprint import pprint


class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "c96171ca2e1a434c8ca8d7674042c87e"
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body += f"{article['title']} \n {article['url']} \n\n"

        return (email_body)

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"apiKey={self.api_key}&" \
              f"language={self.language}"
        return url


if __name__ == '__main__':
    news_feed = NewsFeed(interest='nasa', from_date='2023-01-06', to_date='2023-01-08', language='en')
    print(news_feed.get())