import requests
from bs4 import BeautifulSoup

class ParserSerie:
    def __init__(self, url):
        self.soup = None
        self.volume_urls = []
        
        r = requests.get(url)
        if r.status_code != 200:
            raise RuntimeError('ParserSerie: http request failed')
        self.soup = BeautifulSoup(r.text, 'html.parser')
        volume_tags = self.soup.findAll('h5', {'class': 'chapter-title-rtl'})
        for volume_tag in volume_tags:
            link_tags = volume_tag.findChildren('a', recursive=False)
            for link_tag in link_tags:
                volume_url = link_tag.get('href')
                if volume_url:
                    self.volume_urls.append(volume_url.strip())
        self.volume_urls.reverse()

    def get_volume_urls(self):
        return self.volume_urls
