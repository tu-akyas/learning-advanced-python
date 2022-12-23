import requests
from selectorlib import Extractor


class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage
    """
    website = 'https://www.timeanddate.com/weather'
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    

    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')
        
    def _build_url(self):
        url = f'{Temperature.website}/{self.country}/{self.city}'
        return url
    
    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file('temperature.yaml')
        response = requests.get(url, Temperature.headers)
        raw_value = extractor.extract(response.text)
        return raw_value
    
    def get(self):
        scraped_content = self._scrape()
        temperature = float(scraped_content['temp'].replace('\xa0°C', '').strip())
        return temperature


if __name__ == '__main__':
    temperature = Temperature(country='india', city='chennai').get()
    print(temperature)
